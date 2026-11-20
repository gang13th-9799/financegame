# คลัง Prompt — แถบวงแหวนกลาง (ถนนวงแหวน · ทางเดิน · แม่น้ำ · หญ้า · ราง · หญ้า) เป็นภาพวาด · เพิ่ม 2026-11-17

**สถานะ: ✅ ใส่เกมแล้วทั้งวง (commit 9508854 · 2026-11-17)** · ไฟล์ `img/band-s` (ช่องตรงด้านหลัง) `band-f` (ด้านหน้า) `band-ct/cr/cb` (หัวมุม) `band-x-o6` (ทางข้ามชุด o6) · โค้ด `bandHTML()`, `BAND_ON`, `BANDX` ใน index.html · ช่องวงนอกด้านหลังถอยออก 6px + แถบด้านหลังยก translateZ ทับขอบดิน (เจ้าของเลือก)

## วิธีที่ได้ผล (บทเรียน)
- **Gemini วาดตามแม่แบบได้ดีเมื่องานง่าย:** ช่องแถบเปล่า (แถบขนานอย่างเดียว) ออกมาตรงแม่แบบ · แต่สั่งให้วาดแถบ + ถนนตัด/หัวมุมพร้อมกัน → แถบเลื่อน ถนนเลี้ยวผิด สะพานผิดทิศ
- **สูตรที่ใช้ได้:** (1) Gemini วาดฐานง่าย ๆ ให้สวย → (2) Claude สร้าง "ภาพแบบ" ทับฐานนั้นด้วยโค้ด (วาดถนน/สะพาน/ไม้กั้นตามตำแหน่งจริง หรือดัดลายเป็นหัวมุม) → (3) Gemini "เกลา" ภาพแบบรูปเดียว (prompt: Refine… keep EVERYTHING in the same place… only repaint…) · **อย่าแนบภาพสไตล์รูปที่ 2** — Gemini จะลอกเลย์เอาต์ของรูปนั้นมาแทน
- ระบุ "No vehicles" ชัด ๆ ถ้าไม่ต้องการรถ · ระบุ "T-junction … ring road runs unbroken" ถ้าเป็นสามแยก
- ใช้ภาพจาก Gemini แค่ช่องตรง 1 + หัวมุม 1 · Claude หมุนในระนาบ (คลายเป็นจัตุรัส → หมุน → บิดกลับ) ได้ครบ 4 ด้าน/4 มุม · ในเกมใช้เฉพาะผิวบนข้าวหลามตัด
- **ตำแหน่งแถบมาตรฐาน (สัดส่วนความลึกจากขอบนอก):** ถนนวงแหวน 0–.31 (เส้นประ ~.155) · ทางเดินครีม .31–.41 · แม่น้ำ .41–.62 + ขอบฟ้าอ่อน .62–.67 · หญ้า .67–.81 · ราง/กรวด .81–.91 · หญ้า .91–1 · ถนนตัดข้ามกว้าง u .335–.665
- แผ่นพื้นแม่แบบ: มุม T(1025,377) R(1948,927) L(101,935) ในภาพ 2048² (Gemini คงตำแหน่งนี้ทุกภาพ)

| เลข | ภาพ | สถานะ |
|---|---|---|
| P035a | ช่องตรง | ✅ ใส่เกมแล้ว |
| P035b | หัวมุม (เกลาจากภาพแบบที่ Claude ดัดลายช่องตรง) | ✅ ใส่เกมแล้ว |
| P034a-mid | ทางข้ามชุด o6 สามแยก+สะพาน+ไม้กั้น (เกลาจาก guide-P034a-cross) | ✅ ใส่เกมแล้ว |
| P034b/c/d-mid | ทางข้าม o18 / o30 / o42 | รอทำ · ใช้สูตรเดียวกัน: Claude วาดภาพแบบบน band-s → Gemini เกลา |

### P035a prompt (ช่องตรง · แนบ ref-band-plain.png)
```
Repaint the attached image in a hand-painted style, keeping its layout EXACTLY: the same square isometric tile, same size, same angle, same position in the frame, the same thick brown soil base. The tile is a PERFECT SQUARE. Keep all six parallel stripes exactly where they are, with the same widths, running straight from edge to edge parallel to the back-right edge so they continue seamlessly into neighboring tiles. From the back-right edge to the front-left edge: a gray asphalt ring road with a white dashed center line, a narrow cream footpath, a turquoise river with soft light-blue bank edges and gentle ripples, a green grass strip with a few tiny flowers, a beige gravel rail bed with a straight railway track (two steel rails on wooden sleepers), and a green grass strip. Do NOT add any crossing road, bridge, junction, curve or extra object — only these straight stripes. Pure white background, nothing outside the tile. Style: soft painted manhwa / webtoon illustration, gentle cel shading, warm natural colors, hand-drawn clean ink outlines, painted textures (not flat vector graphics, not a 3D render), bright sunny daylight. No text, no letters, no numbers, no logos, no people.
```

### P035b-v2 prompt (หัวมุม · แนบ guide-band-corner.png รูปเดียว)
```
Refine the attached image. It is an isometric game board CORNER tile that is already laid out correctly. Keep EVERYTHING in the same place: the same square tile, same size, same angle, same position in the frame, the same brown soil base. Every stripe bends in an L shape around the back corner of the tile and must stay exactly where it is, with the same widths: the gray ring road with its white dashed center line, the cream footpath, the turquoise river, the green grass, the railway on gravel, and the green grass in the front corner. Do not straighten, move, resize or remove any stripe, and do not add roads, bridges, buildings or objects. Only clean up the bend so it looks naturally hand-painted: make the river water, ripples and soft bank edges flow smoothly around the curve without any visible seam along the diagonal; make the railway a smooth curved track with sleepers evenly spaced along the curve; keep the dashed white line on the road smooth around the bend; scatter a few tiny flowers naturally on the grass. Do NOT add any vehicles or people. Style: soft painted manhwa / webtoon illustration, gentle cel shading, warm natural colors, hand-drawn clean ink outlines, painted textures, bright sunny daylight — exactly matching the existing painting. Pure white background, nothing outside the tile. No text, no letters, no numbers, no logos.
```

### P034a-mid v5 prompt (ทางข้าม · แนบ guide-P034a-cross.png รูปเดียว)
```
Refine the attached image. It is an isometric game board tile that is already laid out correctly. Keep EVERYTHING in the same place: the same square tile, same size, same angle, same position in the frame, the same brown soil base, and every stripe (gray ring road, cream footpath, turquoise river, green grass, railway track, green grass) exactly where it is. Do not move, rotate, resize or curve anything, and do not add new roads. The road layout is a T-junction: the gray ring road along the back edge runs straight and unbroken across the whole tile with its white dashed center line; a straight two-lane road branches off from it toward the front-left edge, with rounded curb corners where it meets the ring road. The branch road must NOT continue past the ring road to the back edge. Only repaint the newly added crossing parts so they look hand-painted in the same style as the rest of the tile: the branch road with painted asphalt texture, white edge lines, a yellow dashed center line, and a zebra crossing on the cream footpath; the bridge over the river: a charming low white concrete bridge with decorative railings on both sides and small pillars in the water, with a soft shadow on the water; the railway level crossing: rails set into the road and two red-and-white striped barrier arms raised up on poles with red lights, exactly where they are now. Do NOT add any vehicles: no bus, no cars, no trucks, no motorbikes. No people. Style: soft painted manhwa / webtoon illustration, gentle cel shading, warm natural colors, hand-drawn clean ink outlines, painted textures, bright sunny daylight — matching the river, grass and road already in the image. Pure white background, nothing outside the tile. No text, no letters, no numbers, no logos, no signs with writing, no utility poles, no wires.
```
