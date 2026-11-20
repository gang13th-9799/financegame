# คลัง Prompt — ภาพเพิ่มเติม (P033 ขึ้นไป + รุ่นแก้ล่าสุด) · เพิ่ม 2026-11-17

กติกาและสารบัญอยู่ที่ `claude/image-prompts.md` · บทเรียนเรื่องขนาดอาคาร/พื้นที่สีเขียว ดู `claude/image-prompts-special-split.md`

**สถานะใส่เกม (2026-11-17):** ภาพ P031a–d, P032a–d, P026a–d, P027-v2, P028a–b, P029b-v2 ใส่ลงเกมแล้ว (SQIMG/PROPIMG ใน index.html · commit 01d66f4) · ภาพกว้าง 420 · c = (ขอบล่างภาพ − 161px)/สูง ×100

## P036 — พื้นคอนกรีตเปล่า (ฐานแม่แบบสำหรับช่องวงใน / เมืองหลวง) · รอเจน
- **ที่มา:** เจ้าของเสนอ (2026-11-17) — ทำแผ่นพื้นเปล่าแบบ P001 แต่เป็นคอนกรีต ใช้แนบเป็นแม่แบบเวลาเจนภาพช่องวงในทุกช่อง (แทน P001 ที่เป็นหญ้า) ให้ช่องวงในดูเป็นเมืองหลวง และแผ่นพื้นมีขนาด/มุม/ความหนาเท่ากันทุกภาพ
- **แนบ:** ภาพ P001 (`img/tile-grass.webp`) เป็นแม่แบบรูปทรง · 1:1 · **ไฟล์:** `img/tile-concrete.webp`
- ใช้แล้ว: ช่องวงในที่เจนก่อนหน้า (i4, i12 v1) ใช้ P001 — ไม่ต้องเจนใหม่ · ใช้ P036 กับช่องวงในตัวต่อไป (เช่น P034b-in v2 เป็นต้นไป)
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position, same thickness of the base. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render), bright sunny daylight. One single square ground tile seen from an isometric angle: diamond-shaped top, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Change ONLY the materials: the top surface is a clean, empty modern city plaza of smooth light-gray concrete paving slabs with subtle seams and soft painted texture, a slightly lighter granite curb running along all four edges; the two visible front sides of the base are layered gray concrete and dark asphalt instead of brown soil, with the same thickness as the template. Completely empty: no grass, no plants, no buildings, no objects, no road markings, no puddles. No text, no letters, no numbers, no logos, no people.
```

## P025a–d v3 — สถานีทางเข้าเมือง (ช่องถนน o6 / o18 / o30 / o42)
- o6 ✅ ใช้แล้ว (ชุด P034a) · o18 แทนด้วย P034b-out v2 · o30/o42 ต้องเพิ่มเรื่องทิศทางออกขอบแบบชุด B ก่อนเจน (ดู `claude/image-prompts-entrance.md`)
- ส่วนหน้า + Scene เดิมเก็บไว้อ้างอิง:

### ส่วนหน้า สถานี
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). Bright sunny daylight. One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. IMPORTANT SIZE RULE: the station is BIG and wide, covering about 70 to 80 percent of the tile, reaching close to the tile edges — NOT a small building in the middle of an empty plaza. There is exactly ONE flat ground tile; only the structures rise into the white space above. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people.
```
- P025c-v3 สถานีรถไฟ (o30): `Scene on the tile: a big, charming, instantly recognizable seaside railway station: a grand station building with a red tiled roof, a clock tower (blank clock face, no numbers) and arched windows, two long covered platforms with a colorful passenger train standing at each, railway tracks crossing the tile, a small station plaza with a fountain; palm trees, green lawn and flower beds along the edges.`
- P025d-v3 สถานีรถไฟฟ้า (o42): `Scene on the tile: a big, sleek, instantly recognizable elevated skytrain station: a large modern station box on tall concrete pillars with a curved glass roof, a modern skytrain stopped at the platform, the elevated viaduct crossing the whole tile, wide escalators and stairs down to a busy plaza with a bus stop and bicycle racks underneath; green planters, shady trees and lawns along the edges.`

## P033 — วัดไทยสีขาว (แนวเดียวกับวัดร่องขุน)
- **ช่อง:** ⚠ ยังไม่ระบุ · **ไฟล์:** `img/sq-temple.webp` (อยู่ในโฟลเดอร์เกมแล้ว ยังไม่ผูกช่อง) · **สถานะ:** มีแล้ว (threshold ขาว 245)

## P029b-v2 — บริจาคซื้อเครื่องมือแพทย์ — ✅ ช่อง o35
- **ไฟล์ในเกม:** `img/sq-charity-o35.webp` · ชื่อช่อง o35 = "บริจาคซื้อเครื่องมือแพทย์"

## รุ่นที่เลิกใช้
- P025a–d v2 · P029-v3 · P029b v1
