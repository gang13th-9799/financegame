# คลัง Prompt — วงในเมืองหลวง · เพิ่ม 2026-11-18

วงนอกมีภาพครบทุกช่องแล้ว + ทางเข้าเมือง 4 ชุด · วงใน 28 ช่อง (i4 i12 i20 i28 = สถานี มีแล้ว)
- **ฐาน P036** `P036-city-base.png` (Downloads · 2048 จัตุรัส · แผ่นคอนกรีตเทาอ่อน เว้นขอบขาว) — ภาพเตี้ย/กลาง
- **ฐาน P036b** `P036b-city-base-tall.png` (Downloads · 1536×2048 แนวตั้ง · แผ่นอยู่ล่าง) — **ตึกสูง**
- ธีม: ใจกลางเมืองหลวงทันสมัย หรู สะอาด (แบบกรุงเทพฯ ชั้นใน) · ตึกซ้อน/บังกันได้ · ห้ามรถ ห้ามคน ห้ามตัวหนังสือ
- **วงในต้องยิ่งใหญ่กว่าวงนอกเสมอ** · **ตัวอาคารเต็มแผ่น 100%** (กติกาเจ้าของ) — ผนังขึ้นจากขอบแผ่นทั้ง 4 ด้าน · ของประกอบวางบนหลังคา/ระเบียง · ช่องที่ไม่ใช่ตึก (พักผ่อน) ใช้อาคาร/โดมเต็มแผ่น
- ด้าน 1 และ 3 (i8–i15, i24–i31) เกมกลับภาพซ้าย-ขวาเอง
- ช่องชนิดเดียวกันทำแบบไม่ซ้ำ (เงินเดือน i0/i16 · ศูนย์ธุรกิจ i2/i18 · ศูนย์เรียนรู้ i6/i22 · พักผ่อน i10/i26)
- ใส่เกม: ตัดภาพ `/root/sk/procD.py`/`procT.py` (ภาพ Gemini 1792×2390 · มุมแผ่นซ้าย x≈170 y≈1715) → ช่องพิเศษ `SQIMG.iX=[ไฟล์,c]` · ที่ดิน `PROPIMG.iX=c` + `PROPR.iX=.603` · ช่องวงในที่มีภาพยก translateZ .7px อัตโนมัติ
  - วิธีตัดแบบไม่มีสคริปต์ข้างบน (แชตคลังภาพ ชุด F): มุมแผ่น L(170,1720) R(1621,1725) → ตัด x 170–1622 ย่อกว้าง 420 · c = (1722 − ขอบบนภาพ)/สูง × 100 · ลบพื้นขาวแบบ flood จากขอบ (เกณฑ์ 228 · ภาพกระจก/โดม 238–242)
- Gemini ชอบเติมคน/รถเล็กๆ ในภาพ (i5 มีรถใต้ตึก · i6 มีคนในห้องสมุด — เจ้าของยังไม่ว่า) → ส่วนหน้า v5 เพิ่มประโยค interior empty

## ชุด E — ย่านที่พักหรู (i0–i7) ✅ ครบแล้ว (commit 6f4aa62)

| เลข | ช่อง | ชื่อ | ไฟล์ · c |
|---|---|---|---|
| P037a-v3 | i0 | เงินเดือน · สำนักงานใหญ่ธนาคาร | `sq-pay-i0` 73.9 |
| P037b | i1 | คอนโดติดรถไฟฟ้า | `prop-i1` 71.2 |
| P037c | i2 | ศูนย์ธุรกิจ | `sq-bizc-i2` 70.8 |
| P037d | i3 | เซอร์วิสอพาร์ตเมนต์ | `prop-i3` 71.0 |
| P037e | i5 | ทาวน์โฮมกลางเมือง | `prop-i5` 67.4 (ตัดเงานอกแผ่น) |
| P037f | i6 | ศูนย์เรียนรู้ ห้องสมุดหลังคาไม้ | `sq-study-i6` 71.5 |
| P037g | i7 | บ้านหรูริมแม่น้ำ | `prop-i7` 72.9 |

## ชุด F — ย่านช้อปปิ้ง (i8–i15) ✅ ครบแล้ว (commit dd4debd · 2026-11-20)

| เลข | ช่อง | ชื่อ | ฐาน | ไฟล์ · c |
|---|---|---|---|---|
| P038a | i8 | ตลาดหลักทรัพย์ (ช่องเทรด) | P036b | `sq-exch-i8` 73.9 |
| P038b | i9 | ร้านอาหารในห้าง | P036 | `prop-i9` 71.0 |
| P038c | i10 | พักผ่อน (แบบ 1) · สวนพฤกษศาสตร์ในโดมแก้ว | P036 | `sq-rest-i10` 71.5 |
| P038d | i11 | คอมมูนิตี้มอลล์ | P036 | `prop-i11` 68.7 (มีป้าย "Café" ในภาพ — รอเจ้าของตัดสินว่าจะเจนใหม่ไหม) |
| P038e | i13 | ห้างสรรพสินค้า | P036b | `prop-i13` 70.8 |
| P038f | i14 | ข่าวตลาด · ตึกสื่อจอยักษ์ | P036b | `sq-news-i14` 72.6 |
| P038g | i15 | ศูนย์การค้าใหญ่ | P036b | `prop-i15` 71.9 |

### ส่วนหน้า v5 (ใช้ทุกภาพวงใน — ต่อท้ายด้วย Scene)
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position in the frame, the same thin gray concrete slab. The tile is a thin flat slab exactly like in the attached image: its top is a perfect diamond with SHARP POINTED left and right corners — never cut off or flatten the corners, never make the base thicker or the tile bigger, and keep the white margin all around the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, hand-drawn clean ink outlines, painted textures, flat painted look (not a 3D render). Bright sunny daylight, warm, bright, cheerful colors — not dull. Setting: the dense downtown of a modern, prosperous Asian capital city like central Bangkok — luxurious and clean. MOST IMPORTANT: the building fills the ENTIRE tile — its outer walls rise straight up from all four edges of the tile, covering 100 percent of the tile top, like one massive city block. No open ground, no plaza, no garden, no sidewalk on the tile. Put any decorations, pools and trees on the podium roof, terraces or rooftop instead. The building is empty: no people anywhere, not even tiny figures inside the windows. Do NOT add any vehicles (no cars, no trains, no parking), no utility poles, no wires. No text, no letters, no numbers, no logos, no signs with writing. Pure white background, nothing outside the tile. Scene on the tile:
```

### Scene ชุด F (วางต่อท้ายส่วนหน้า v5)
- **P038a · i8 ตลาดหลักทรัพย์ (แนบ P036b):** `the national STOCK EXCHANGE tower: a grand modern skyscraper of dark blue glass and white stone filling the whole tile, a huge glass trading-hall podium with giant wall screens showing colorful rising and falling chart lines and candlestick graphs (graphics only, no numbers or letters), a golden bull sculpture on the podium roof terrace, a sharp crown at the top.`
- **P038b · i9 ร้านอาหารในห้าง:** `a stylish dining mall block filling the whole tile: several floors of glass-fronted restaurants with warm lights, colorful awnings and hanging plants on the terraces, a rooftop dining terrace with string lights, umbrellas and tables.`
- **P038c · i10 พักผ่อน · โดมแก้ว:** `a huge glass-and-white-steel botanical dome filling the whole tile, full of tropical trees, waterfalls and flowers visible through the glass, curved glass terraces and a sky walkway inside.`
- **P038d · i11 คอมมูนิตี้มอลล์:** `a trendy low-rise community mall block filling the whole tile: two to three floors of boutique shops and cafés with wooden and glass facades, terraces with plants and café umbrellas, a rooftop garden with a small playground.`
- **P038e · i13 ห้างสรรพสินค้า (แนบ P036b):** `a luxurious multi-storey department store filling the whole tile: elegant cream stone and glass facade with tall gold-framed display windows, stacked floors with curved glass corners, a grand glass atrium, a rooftop terrace with palm trees.`
- **P038f · i14 ข่าวตลาด (แนบ P036b):** `a sleek media and news tower filling the whole tile, covered with giant curved LED screens showing colorful abstract graphics and chart shapes (no text, no numbers), satellite dishes and broadcast antennas on the roof, glass sky-lobby.`
- **P038g · i15 ศูนย์การค้าใหญ่ (แนบ P036b):** `a gigantic mega shopping mall filling the whole tile: a massive futuristic white building with flowing curved glass bands, a huge glass atrium, a tall glass hotel tower rising on top, rooftop garden with palms and an infinity pool.`

## ชุดถัดไป (รอ) — i16–i31
- ชุด G i16–i23 · ชุด H i24–i31 (ยกเว้นสถานี i20 i28) · ยังไม่ได้เขียน prompt

### เลิกใช้
- ~~P037a v1~~ ศาลาไพรเวตแบงก์เตี้ย · ~~P037a-v2~~ ตึกระฟ้าผอม ลานโล่งเยอะ
