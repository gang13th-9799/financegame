# คลัง Prompt — เมืองใหญ่ตรงกลางกระดาน P041 · เพิ่ม 2026-11-20

พื้นที่กลาง 7×7 ช่อง (grid แถว/คอลัมน์ 4–10 · `.cityc`) ทำเป็นภาพเดียว (เจ้าของตกลง)
- ภาพร่าง `sketch-center.png` (2048² · สคริปต์ `/home/claude/p/sketchCenter.py`) · แผ่นเพชร T(1024,830) R(1999,1415) L(49,1415)
- เจ้าของ: ถนนเฉพาะวงรอบนอก ด้านในไม่มีถนน · อาคารเยอะๆ เต็มพื้นที่ · มีสวนสาธารณะ วัด ตึกไฮเทคมีโลโก้
- **โลโก้:** ห้ามให้ AI วาด (CLAUDE.md) → Gemini เว้นแผงว่าง แล้ว Claude วางโลโก้จริงด้วย `logomask.npy` (เอียงตามผนัง shear −0.6 กว้าง 78% · ไล่แสงจากขวาบน · ขอบสว่าง/เงา · เงาตกซ้ายล่าง)
- v3 ใส่เกมแล้ว (commit 6f10de6) → ตึกสูงบังช่องเดินด้านหลัง
- **กฎความสูง (เจ้าของ):** ครึ่งบน/ด้านหลัง = ของเตี้ย (สวน วัด อาคารเตี้ย) ไม่บังช่องเดินด้านหลัง · แถบล่างฝั่งหน้า = ตึกสูงได้ (โดนช่องเดินวงในฝั่งหน้าบังอยู่แล้ว) · ตึกกลางเตี้ยลง 50%
- v6 ผัง: สวน+บ่อน้ำรูปตัว L มุมหลัง (แปลง 0,0 1,0 0,1) · วัดขาวด้านหลังขวา (แปลง 2,0) · ตึกกลางสูงครึ่งเดียว · ตึกเมืองครึ่งหน้า

### P041-v6 — แนบ `sketch-center.png` (v6) รูปเดียว · 1:1
```
Refine the attached sketch into a finished illustration. It is the isometric centerpiece of a game board, already laid out correctly. Keep EVERYTHING in the same place: the same square diamond-shaped slab with its thin gray edge, the same size, angle and position in the frame, and the ONE ring street with white dashed lines running around the outer edge exactly where it is. Inside the ring street there are NO streets: only narrow paved pedestrian lanes between buildings. The heart of a big, modern, prosperous Asian capital city like central Bangkok:
- BACK (top of the image): a lush green PUBLIC PARK exactly on the green L-shaped area — big shade trees, flower beds, a winding path, lawns, benches and the turquoise pond with a little wooden bridge. Everything in the back half stays LOW so it never blocks the view behind it.
- BACK RIGHT: a beautiful white THAI TEMPLE exactly where the small white building with the pointed roof stands — gleaming white with ornate silver and mirror-glass details and a white pointed spire, in a small garden.
- CENTER: the futuristic HIGH-TECH HEADQUARTERS exactly where the blue block stands, exactly as tall as the block (do NOT make it taller) — glass and white steel, flowing white curves, glowing light strips, sky gardens and a crown on top. Keep the plain white round panel on its right face exactly where it is, completely EMPTY and blank (a logo will be added later) — draw nothing inside it.
- FRONT half (bottom of the image, nearest the viewer): every small flat block becomes its own building, shoulder to shoulder — varied office towers, condo towers, hotels and shopping buildings of different colors, materials and shapes, with rooftop gardens and pools. These front buildings may be tall skyscrapers, the tallest in the front-right corner. Never plain boxes.
Isometric, soft painted manhwa / webtoon illustration style, gentle cel shading, hand-drawn clean ink outlines, painted textures, flat painted look (not a 3D render). Bright sunny daylight, warm, bright, cheerful colors — not dull. Pure white background, nothing outside the slab. No people, no vehicles, no utility poles, no wires. No text, no letters, no numbers, no logos, no signs with writing.
```
