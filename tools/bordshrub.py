"""สร้างภาพขอบสวนรอบนอกแบบไม่มีทางเดิน จาก img/bord-fl1.webp
ตัดพุ่มไม้ออกเป็นชิ้น ลบออกจากพื้น แล้วสุ่มวางใหม่หลายแบบ
  g1..g4 = แถบหญ้าอ่อนอยู่ขอบหน้า-ซ้าย (แบบ fl)
  k1..k4 = แถบหญ้าอ่อนอยู่ขอบหลัง-ซ้าย (แบบ bl · พื้นกลับแนวตั้ง พุ่มไม้ตั้งตรงเหมือนเดิม)
ใช้: python tools/bordshrub.py <ภาพต้นฉบับ fl1> <โฟลเดอร์ปลายทาง>
"""
import sys, random
import numpy as np, cv2
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
a = np.array(Image.open(src).convert('RGBA'))
H, W = a.shape[:2]
al = a[..., 3]
rgb = a[..., :3].copy()
rgb_fill = rgb.copy()
rgb_fill[al < 250] = np.median(rgb[al > 250], axis=0)  # ขอบโปร่งใสเป็นสีหญ้า กันสีขาวไหลเข้าตอนลบพุ่ม

# หาพุ่มไม้: ต่างจากพื้นรอบข้างชัด และไม่ใช่เส้นขาวยาว
bg = cv2.medianBlur(rgb, 31)
d = np.abs(rgb.astype(int) - bg.astype(int)).sum(2)
m = ((d > 45) & (al > 200)).astype(np.uint8)
m2 = ((d > 28) & (al > 200)).astype(np.uint8)
n, lab, st, cen = cv2.connectedComponentsWithStats(m)
ids = [i for i in range(1, n) if 120 < st[i, 4] and st[i, 2] < 60]

sprites = []
holes = np.zeros((H, W), np.uint8)
for i in ids:
    x, y, w, h, _ = st[i]
    blob = (lab == i).astype(np.uint8)
    # เติมรูในพุ่ม + ขยายนิดให้ติดขอบเส้นและเงา
    cnts, _ = cv2.findContours(blob, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    blob = cv2.drawContours(np.zeros_like(blob), cnts, -1, 1, -1)
    blob = cv2.dilate(blob, np.ones((5, 5), np.uint8))
    holes |= cv2.dilate(blob, np.ones((11, 11), np.uint8)) | (cv2.dilate(blob, np.ones((15, 15), np.uint8)) & m2)
    p = 4
    x0, y0, x1, y1 = max(x - p, 0), max(y - p, 0), min(x + w + p, W), min(y + h + p, H)
    spr = a[y0:y1, x0:x1].copy()
    am = cv2.GaussianBlur(blob[y0:y1, x0:x1].astype(np.float32), (3, 3), 0)
    spr[..., 3] = (np.minimum(am, 1) * spr[..., 3]).astype(np.uint8)
    # จุดยึด = กึ่งกลางล่างของพุ่ม (จุดแตะพื้น)
    core = a[y:y + h, x:x + w][blob[y:y + h, x:x + w] > 0, :3].astype(int)
    sprites.append((Image.fromarray(spr), (x + w / 2 - x0, y + h - 2 - y0), core.mean()))

# ตัดพุ่มที่ซีด (ภาพต้นฉบับบางต้นจาง) ออก
lum = np.array([t[2] for t in sprites])
sprites = [t[:2] for t in sprites if t[2] < np.median(lum) + 12]

lid = [i for i in range(1, n) if st[i, 2] >= 60][0]
holes = cv2.dilate(holes, np.ones((3, 3), np.uint8)) & (1 - cv2.dilate((lab == lid).astype(np.uint8), np.ones((7, 7), np.uint8)))
ground = cv2.inpaint(rgb_fill, holes, 9, cv2.INPAINT_TELEA)
base = np.dstack([ground, al])

# พื้นที่วางพุ่ม: ในข้าวหลามตัด (หดขอบ) และอยู่ฝั่งหญ้าเข้ม (เหนือเส้นขาว)
lm = st[[i for i in range(1, n) if st[i, 2] >= 60][0]]
lx0, ly0, lw, lh = lm[0], lm[1], lm[2], lm[3]
L0, L1 = np.array([lx0, ly0]), np.array([lx0 + lw, ly0 + lh])  # เส้นขาว ซ้ายบน → ขวาล่าง
cx, cy = W / 2, H / 2


def side(px, py, flip):
    a0, a1 = (L0, L1) if not flip else (np.array([L0[0], H - 1 - L0[1]]), np.array([L1[0], H - 1 - L1[1]]))
    e, q = a1 - a0, np.array([px, py]) - a0
    v = (e[0] * q[1] - e[1] * q[0]) / np.hypot(*e)  # ระยะตั้งฉาก (px) มีเครื่องหมาย
    return -v if not flip else v


def ok(px, py, flip):
    u = abs(px - cx) / (W / 2) + abs(py - cy) / (H / 2)
    if u > 0.80:
        return False
    # ทั้งโคนพุ่มและยอดพุ่ม (สูง ~24px) ต้องอยู่ฝั่งหญ้าเข้ม ห่างเส้นขาว >= 10px
    return side(px, py, flip) > 10 and side(px, py - 26, flip) > 10


def make(seed, flip):
    rnd = random.Random(seed)
    img = Image.fromarray(base[::-1].copy() if flip else base.copy())
    pts = []
    tries = 0
    want = rnd.randint(12, 16)
    while len(pts) < want and tries < 5000:
        tries += 1
        px, py = rnd.uniform(0, W), rnd.uniform(0, H)
        if not ok(px, py, flip):
            continue
        if any((px - x) ** 2 + ((py - y) * 1.6) ** 2 < 34 ** 2 for x, y, _ in pts):
            continue
        pts.append((px, py, rnd.randrange(len(sprites))))
    for px, py, k in sorted(pts, key=lambda t: t[1]):
        spr, (ax, ay) = sprites[k]
        s = rnd.uniform(0.85, 1.15)
        if rnd.random() < 0.5:
            spr = spr.transpose(Image.FLIP_LEFT_RIGHT)
            ax = spr.width - ax
        spr = spr.resize((round(spr.width * s), round(spr.height * s)), Image.LANCZOS)
        img.alpha_composite(spr, (round(px - ax * s), round(py - ay * s)))
    # คงขอบโปร่งใสเดิมของแผ่น
    arr = np.array(img)
    arr[..., 3] = al[::-1] if flip else al
    return Image.fromarray(arr)


for j in range(4):
    make(100 + j, False).save(f'{out}/bord-g{j+1}.webp', quality=90)
    make(200 + j, True).save(f'{out}/bord-k{j+1}.webp', quality=90)
print(len(sprites), 'พุ่ม')
