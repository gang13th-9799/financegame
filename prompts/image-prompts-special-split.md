# คลัง Prompt — ช่องพิเศษ (P026a–d, P027, P028a–b, P029) · เพิ่ม 2026-11-16

กติกาและสารบัญอยู่ที่ `claude/image-prompts.md`

- **เหตุที่แยก:** P026 (ศูนย์เรียนรู้) เดิมใช้ภาพเดียว 4 ช่อง และ P028 (ฟุ่มเฟือย) ใช้ภาพเดียว 2 ช่อง ขัดกับกติกาเจ้าของว่า "ไม่ชอบภาพซ้ำบนแผนที่" → แยกตามเขตเหมือน P024 (สวนสาธารณะ) · P026 และ P028 ตัวรวมถือว่าเลิกใช้
- เขตตามเลขช่อง (กระดาน 48): o0–o11 เกษตร · o12–o23 อุตสาหกรรม · o24–o35 ท่องเที่ยว · o36–o47 ชุมชน
- **วิธีใช้:** แนบภาพ P001 · สัดส่วน 1:1 · วาง "ส่วนหน้า v2" แล้วต่อท้ายด้วยประโยค Scene ของแต่ละเลข (ยกเว้นตัวที่เขียน prompt เต็มไว้แล้ว)
- **บทเรียนจากเจ้าของ (สำคัญ):** อาคารต้อง **ใหญ่ เต็มแผ่น และดูออกทันทีว่าเป็นอะไร** · ต้องมี **พื้นที่สีเขียว ต้นไม้** ด้วย ไม่ใช่ลานปูนโล่ง · ของที่เป็นหัวใจของช่อง (เช่น ตู้บริจาค) ต้อง **ใหญ่ เห็นชัด**
- **ยังไม่ได้ใส่กฎขนาด:** P025a–d (สถานีทางเข้าเมือง) และ P030a–d (จุดเชื่อม) ใน `claude/image-prompts.md` — ต้องทำเวอร์ชันใหม่ก่อนเจน
- **ธีมสีพิเศษ:** P027 (ตกงาน) เป็นช่องเดียวที่ใช้โทนมืดดำ — ช่องอื่นทุกช่องเป็นกลางวันสีอุ่น
- **ช่องบริจาค:** คลังมีบันทึกแค่ o35 ช่องเดียว · เจ้าของขอเพิ่มอีกจุด (P029b บริจาคโรงพยาบาล) — **ต้องยืนยันเลขช่องกับเจ้าของ/โค้ดเกม**

## ส่วนหน้า v2 (ใช้กับทุกเลขในไฟล์นี้)
- **เหตุที่แก้:** v1 ไม่ได้กำหนดขนาด → Gemini วาดอาคารเล็กกลางลานโล่ง · v2 เพิ่มประโยคบังคับให้อาคารใหญ่กินพื้นที่ 70–80% ของแผ่น
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). Bright sunny daylight. One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. IMPORTANT SIZE RULE: the main building is BIG and wide, covering about 70 to 80 percent of the tile, reaching close to the tile edges, with only narrow strips of ground around it — NOT a small building in the middle of an empty plaza. There is exactly ONE flat ground tile; only the building rises into the white space above. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people.
```

## P026 — ศูนย์เรียนรู้ (แยก 4 แบบ)

### P026a — ศูนย์เรียนรู้เกษตร
- **ช่อง:** o8 · **ไฟล์:** `img/sq-study-o8.webp` · **สถานะ:** มีแล้ว (ตัดพื้นขาวแล้ว)
```
Scene on the tile: a large modern agricultural learning center: a long one-story classroom building with a wooden roof along the back, a big glass greenhouse full of seedlings along one side, neat demonstration vegetable plots, and an outdoor classroom with benches facing a blank chalkboard under a shady tree.
```

### P026b-v2 — ศูนย์ฝึกอาชีพ
- **ช่อง:** o20 · **ไฟล์:** `img/sq-study-o20.webp` · **สถานะ:** มีแล้ว (ตัดพื้นขาวแล้ว) · prompt เต็มอยู่ในประวัติแชต 2026-11-16 · มีผู้ฝึกตัวเล็ก
- สรุปฉาก: อาคาร 2 ชั้นรูป L หลังคาฟันเลื่อย ฟ้า-ขาว · ห้องฝึกซ่อมรถ/เชื่อมเหล็ก/ไฟฟ้า เปิดประตูม้วน · ลานฝึกโฟล์คลิฟต์ กรวย รถขุดเล็ก · ผู้ฝึกชุดช่างน้ำเงิน หมวกเหลือง

### P026c-v2 — อควาเรียม
- **ช่อง:** o32 · **ไฟล์:** `img/sq-study-o32.webp` · **สถานะ:** มีแล้ว (ตัดพื้นขาวแล้ว) · prompt เต็มอยู่ในประวัติแชต 2026-11-16 · มีผู้ชมตัวเล็ก
- สรุปฉาก: อาคาร 2 ชั้นหลังคาลอนคลื่นฟ้าขาว โดมกระจก · ผนังทั้งด้านเป็นตู้ปลายักษ์ (เต่า กระเบน ฉลาม) อุโมงค์ใต้น้ำ · ประติมากรรมหางวาฬกับน้ำพุ · พุ่มไม้รูปโลมา

### P026d — ห้องสมุดชุมชน
- **ช่อง:** o44 · **ไฟล์:** `img/sq-study-o44.webp` · **สถานะ:** รอเจน
```
Scene on the tile: a large modern three-story public library: tall glass walls showing colorful bookshelves on every floor, a giant open-book sculpture at the entrance, a reading garden with tables and benches tucked along one side, a small colorful kids' corner.
```

## P027-v2 — ตกงาน (โทนมืดดำ)
- **ช่อง:** o11 · **ไฟล์:** `img/sq-jobless.webp` · **สถานะ:** มีแล้ว · Gemini ให้สีเทาเบจสว่าง → Claude ปรับสีหลังเจน (ลดความสด ~70%, มืดลง, อมฟ้าเย็น) จนได้โทนดำเทา
- สรุปฉาก: อาคารสำนักงาน 3 ชั้นร้าง ประตูม้วนปิด หน้าต่างแตก ป้ายถูกถอด รั้วล่ามโซ่ กองกล่อง เก้าอี้ทิ้ง แอ่งน้ำ เสาไฟดวงเดียว · prompt เต็มอยู่ในประวัติแชต 2026-11-17

## P028 — ฟุ่มเฟือย (แยก 2 แบบ)

### P028a — โชว์รูมรถหรู
- **ช่อง:** o23 · **ไฟล์:** `img/sq-splurge-o23.webp` · **สถานะ:** รอเจน
```
Scene on the tile: a flashy, large luxury car showroom: a sleek two-story glass building with gold trim showing shiny sports cars on round turntable platforms on both floors, a bright red supercar displayed on a podium at the front corner, polished stone forecourt with planters.
```

### P028b — บูติกแบรนด์เนม
- **ช่อง:** o47 · **ไฟล์:** `img/sq-splurge-o47.webp` · **สถานะ:** มีแล้ว (ตัดพื้นขาวแล้ว · มีป้ายตั้งพื้นตัวอักษรขยุกขยิกเล็กมาก ยอมรับได้)

## P029 — บริจาค

### P029-v3 — ศูนย์การกุศล
- **ช่อง:** o35 · **ไฟล์:** `img/sq-charity.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
- **เหตุที่แก้:** v2 อาคารยังไม่ใหญ่พอ พื้นเป็นลานปูนเทาโล่ง ไม่มีต้นไม้ ตู้บริจาคเล็ก → v3 อาคารใหญ่ขึ้น มีสนามหญ้า ต้นไม้ร่มรื่นรอบอาคาร ตู้บริจาคใสขนาดใหญ่เด่นหน้าทางเข้า · prompt เต็ม
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). Bright sunny daylight. One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. IMPORTANT SIZE RULE: the building is BIG and wide, covering about 70 percent of the tile, reaching close to the back edges — NOT a small building in the middle of an empty plaza. There is exactly ONE flat ground tile; only the building rises into the white space above. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Scene on the tile: a large, warm, green community charity center: a big two-story building with a cream and soft coral facade and a large heart emblem on the front wall, a wide open covered donation hall on the ground floor with long tables full of food boxes, rice bags, water bottles and folded clothes. In front of the entrance, a VERY LARGE clear glass donation box — taller than a door — filled with banknotes and coins, standing on a small stage with a red heart on top, clearly the eye-catching centerpiece. The ground around the building is lush and green: soft grass lawn, several shady leafy trees and a palm tree along the edges, flowering shrubs, and a big heart-shaped flower bed. Warm, kind, hopeful mood.
```

### P029b — บริจาคโรงพยาบาล (ซื้อเครื่องมือแพทย์)
- **ช่อง:** ⚠ ยังไม่ยืนยัน (คลังบันทึกช่องบริจาคไว้แค่ o35) · **ไฟล์:** `img/sq-charity-hospital.webp` (ชั่วคราว ตั้งตามเลขช่องเมื่อยืนยัน) · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
- **ที่มา:** เจ้าของขอช่องบริจาคอีกจุด ธีมบริจาคให้โรงพยาบาลซื้อเครื่องมือแพทย์ · prompt เต็ม
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). Bright sunny daylight. One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. IMPORTANT SIZE RULE: the hospital building is BIG and wide, covering about 70 percent of the tile, reaching close to the back edges — NOT a small building in the middle of an empty plaza. There is exactly ONE flat ground tile; only the building rises into the white space above. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Scene on the tile: a hospital fundraising scene for new medical equipment: a large modern four-story white hospital with light blue glass windows and a big red cross on the top of the facade. In front of the main entrance, a VERY LARGE clear glass donation box shaped like a heart with a red cross, filled with banknotes and coins, clearly the centerpiece. Beside it, a display of brand-new donated medical equipment tied with big red ribbon bows: a hospital bed, a ventilator machine on a stand, a heart monitor screen, a wheelchair, and a brand-new white ambulance with a red bow on its roof. A tall donation gauge shaped like a thermometer with a red heart on top, filled almost to the top (no numbers). Green lawn, shady trees and flower beds around the building. Warm, caring, hopeful mood.
```

## รุ่นที่เลิกใช้
- P029-v2 — ศูนย์การกุศล (ลานปูนโล่ง ไม่มีต้นไม้ ตู้บริจาคเล็ก · แทนด้วย P029-v3)
- P029 — บริจาค v1 (ศาลาเล็ก ไม่มีกฎขนาด · แทนด้วย P029-v2)
- P027 — ตกงาน v1 (ออฟฟิศเล็ก สีหม่นนิดเดียว · แทนด้วย P027-v2 โทนมืดดำ)
- ส่วนหน้า v1 (ไม่บังคับขนาดอาคาร → อาคารเล็กกลางลาน · แทนด้วยส่วนหน้า v2)
- P026c — ห้องสมุดพิพิธภัณฑ์ริมทะเล v1 (ศาลาเล็กกลางลานทราย · เปลี่ยนเป็นอควาเรียม P026c-v2)
- P026b — ศูนย์ฝึกอาชีพ v1 (กล่องกระจกเล็ก มีแขนกล ดูเหมือนห้องวิจัย · แทนด้วย P026b-v2)
- P026 — ศูนย์เรียนรู้ภาพเดียว 4 ช่อง (แยกเป็น P026a–d)
- P028 — ฟุ่มเฟือยภาพเดียว 2 ช่อง (แยกเป็น P028a–b)
