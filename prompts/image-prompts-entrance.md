# คลัง Prompt — ชุดทางเข้าเมือง P034 (แทน P025a–d + P030a–d) · เพิ่ม 2026-11-17

กติกาและสารบัญอยู่ที่ `claude/image-prompts.md` · วิธีทำช่องทางข้ามดู `claude/image-prompts-band.md`

## สูตรที่ใช้ได้ (สรุปจากชุด A)
1. **สถานีวงนอก** — แนบ P001 + prompt ช่องสถานี (มีกฎขนาด)
2. **สถานีวงใน** — แนบ P001 + prompt สถานีกลางเมืองหลวง **ใหญ่โตหรูหรากว่าวงนอก** (เจ้าของกำหนด)
3. **ทางข้าม** — Claude วาดภาพแบบบนช่องแถบ `band-s` ตามตำแหน่งจริง → Gemini เกลาภาพแบบรูปเดียว ("Refine… keep EVERYTHING in the same place")
- เลิกใช้: ภาพเดียวยาว 3 ส่วน (v1) · ช่องกลางบนแม่แบบเปล่า (v2) · ภาพอ้างอิง 3 ช่องให้วาดช่องกลาง (v3) — Gemini ล็อกตำแหน่งไม่ได้
- **ทิศ:** เกมกลับภาพซ้าย-ขวาให้ด้าน 1 และ 3 อัตโนมัติ · `SQIMG` ค่าที่ 3 = บังคับ `--m` (1 = ไม่กลับ) · ชุด B ใช้แบบไม่กลับ: ภาพวงนอก o18 ทางออกไปหาทางข้าม = **ขอบหลัง-ซ้าย** · ภาพวงใน i12 = **ขอบหน้า-ขวา** (แนวเดียวกัน ขนานกับขอบหน้า-ซ้าย)
- **บทเรียนชุด B:** เจ้าของไม่เอาทางโค้ง/ทางวนในช่อง · สถานีทั้งสองฝั่งต้องมี **ถนน/ทางยกระดับที่วิ่งไปชนขอบช่องฝั่งทางข้ามจริง** ไม่งั้นต่อกันไม่ได้ — prompt ต้องระบุว่าออกขอบไหน กึ่งกลางขอบ ที่ความสูงเท่าไร

## ชุด A — o6 ↔ i4 (เขตเกษตร · รถโดยสาร) ✅ ใส่เกมแล้ว (commit 9508854)
- วงนอก `sq-road-o6` c47.1 · วงใน `sq-road-i4` c45.8 · ทางข้าม `band-x-o6` (BANDX '2,7')

## ชุด B — o18 ↔ i12 (เขตอุตสาหกรรม · ทางด่วนยกระดับ 4 เลน)
- เจ้าของกำหนด: **ทางยกระดับ 4 เลน ตรง ไม่มีทางโค้ง** ทั้งสองฝั่ง · ช่องกลางเป็นทางยกระดับ 4 เลนต่อกัน (ข้ามถนนวงแหวน แม่น้ำ ราง) · ในช่องสถานีให้ทางยกระดับม้วน/ลาดลงมาที่ด่านได้
- ความสูงพื้นทางยกระดับที่ขอบช่อง: ประมาณ 1/4 ของความกว้างแผ่น (Claude ปรับให้ตรงกันตอนทำช่องกลาง)

| เลข | ส่วน | แนบ | สถานะ |
|---|---|---|---|
| P034b-out v2 | ด่านทางด่วน + ทางยกระดับออกขอบหลัง-ซ้าย | P001 | รอเจน |
| P034b-in v2 | ประตูทางด่วนเมืองหลวง + ทางยกระดับเข้าขอบหน้า-ขวา | P001 | รอเจน |
| P034b-mid | ทางยกระดับ 4 เลนข้ามแถบ | ภาพแบบจาก Claude | รอสถานีทั้งสอง |
| ~~P034b-out/in v1~~ | ด่านพื้นราบ / ประตูเมืองมีทางวนโค้ง | — | เลิกใช้ (ไม่มีถนนต่อกัน · ทางโค้งไม่เอา) |

### P034b-out v2
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). Bright sunny daylight. One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE; never stretch it into a rectangle. There is exactly ONE flat ground tile; only the structures rise into the white space above. Setting: modern suburban Thailand near Bangkok, clean and tidy. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Scene on the tile: an expressway toll plaza with a STRAIGHT elevated 4-lane expressway. The expressway runs in one perfectly straight line, parallel to the front-left edge of the tile, from the front-right edge to the BACK-LEFT edge. In the front half, a toll plaza at ground level: a row of toll booths under a long modern canopy, with cars, a container truck and a bus queued. After the booths, the 4-lane road rises on a straight ramp onto an elevated viaduct on tall concrete pillars, and the elevated deck leaves the tile exactly at the MIDDLE of the BACK-LEFT edge, cut off cleanly at the tile edge, high above the ground (deck height about one quarter of the tile width), so it can continue into the next tile. The viaduct has white side barriers and lane markings, with a few cars on it. No curves, no loops, no turning ramps — only straight lines. Around it, a small toll office, green embankments, rows of trees and flower beds.
```

### P034b-in v2
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). Bright sunny daylight. One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE; never stretch it into a rectangle. There is exactly ONE flat ground tile; only the structures rise into the white space above. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Scene on the tile: the GRAND EXPRESSWAY GATEWAY of the capital city — bigger, taller and more luxurious than a provincial toll plaza — with a STRAIGHT elevated 4-lane expressway. The expressway runs in one perfectly straight line, parallel to the front-left edge of the tile, from the back-left edge to the FRONT-RIGHT edge. At the MIDDLE of the FRONT-RIGHT edge, the elevated 4-lane deck enters the tile high above the ground (deck height about one quarter of the tile width), cut off cleanly at the tile edge so it continues from the next tile, carried on tall elegant white pillars with gold accents; it then descends on a straight ramp to ground level and passes under a monumental gateway arch of white stone and glass with gold accents and a row of sleek toll booths with a glass canopy, continuing straight toward the back-left edge. Shiny cars and a luxury coach on the lanes. A landscaped median with palm trees, trimmed hedges and colorful flower beds, a small fountain plaza in a corner. No curves, no loops, no turning ramps — only straight lines. Prestigious, modern, capital-city mood.
```

## ชุด C / D (รอ)
- C o30↔i20 สถานีรถไฟริมทะเล → สะพานรถไฟ → สถานีรถไฟกลางเมือง · D o42↔i28 สถานีรถไฟฟ้า → รางยกระดับ → สถานีรถไฟฟ้าใหญ่กลางเมือง
- วงนอกใช้ prompt P025c–d v3 ใน `claude/image-prompts-extra.md` (ต้องเพิ่มเรื่องทิศทางออกขอบแบบชุด B)
