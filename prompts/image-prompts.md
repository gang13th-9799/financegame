# คลัง Prompt ทำภาพ — financegame

ไฟล์นี้รวม prompt สำหรับทำภาพทั้งหมดของโปรเจกต์ แต่ละ prompt มีหมายเลขประจำตัว เวลาพูดถึงให้อ้างหมายเลข เช่น "แก้ P003" หรือ "ใช้ P012 แต่เปลี่ยนพื้นหลัง"

## กติกาการตั้งหมายเลข
- รูปแบบ: **P + เลข 3 หลัก** เช่น P001, P002, P003 … เรียงตามลำดับที่เพิ่ม
- หมายเลขเป็นของถาวร: ลบ prompt แล้วจะไม่นำเลขนั้นกลับมาใช้ใหม่ (ทำเครื่องหมาย ~~ยกเลิก~~ แทน)
- ถ้าแก้ไข prompt เดิม ให้ใส่เป็นเวอร์ชัน: **P003-v2**, **P003-v3** (เวอร์ชันล่าสุดคือตัวที่ใช้งาน)
- ถ้าแตกแบบย่อยจาก prompt เดิม ให้ใส่ตัวอักษรต่อท้าย: **P003a**, **P003b**

## ไฟล์คลัง
- ไฟล์นี้: กติกา สารบัญ และ prompt ที่ **ยังรอเจน**
- `claude/image-prompts-tiles.md`: prompt ช่องที่ดิน P001–P021 ที่มีภาพแล้ว
- `claude/image-prompts-special.md`: prompt ช่องพิเศษ P022 ขึ้นไปที่มีภาพแล้ว
- `claude/image-prompts-48.md`: prompt ช่องใหม่ของกระดาน 48 ช่อง (P031–P032) ที่ยังรอเจน
- รุ่นที่เลิกใช้เก็บไว้แค่หัวข้อ

## สารบัญ
| หมายเลข | ชื่อ | หมวด | ช่อง | ไฟล์ปลายทาง | สถานะ |
|---|---|---|---|---|---|
| P001 | พื้นหญ้าเปล่า (ฐานช่องพิเศษ) | ภาพช่องกระดาน · พื้นฐาน | o0,o2,o6,o8,o11… ทุกช่องที่ไม่ใช่ที่ดิน | `img/tile-grass.webp` | มีแล้ว |
| P002 | นาข้าว | ภาพช่องกระดาน · เขตเกษตรกรรม | o1 | `img/prop-o1.webp` | มีแล้ว |
| P003 | สวนยางพารา | ภาพช่องกระดาน · เขตเกษตรกรรม | o3 | `img/prop-o3.webp` | มีแล้ว |
| P004 | ไร่มันสำปะหลัง | ภาพช่องกระดาน · เขตเกษตรกรรม | o4 | `img/prop-o4.webp` | มีแล้ว |
| P005 | ฟาร์มไก่ | ภาพช่องกระดาน · เขตเกษตรกรรม | o7 | `img/prop-o7.webp` | มีแล้ว |
| P006 | สวนทุเรียน | ภาพช่องกระดาน · เขตเกษตรกรรม | o9 | `img/prop-o9.webp` | มีแล้ว |
| P007 | ลานจอดรถบรรทุก | ภาพช่องกระดาน · เขตอุตสาหกรรม | o13 | `img/prop-o13.webp` | มีแล้ว |
| P008 | ห้องเช่าคนงาน | ภาพช่องกระดาน · เขตอุตสาหกรรม | o15 | `img/prop-o15.webp` | มีแล้ว |
| P009 | โกดังสินค้า | ภาพช่องกระดาน · เขตอุตสาหกรรม | o16 | `img/prop-o16.webp` | มีแล้ว |
| P010 | โรงงานแปรรูปอาหาร | ภาพช่องกระดาน · เขตอุตสาหกรรม | o19 | `img/prop-o19.webp` | มีแล้ว |
| P011-v3 | นิคมอุตสาหกรรม (ใหญ่โต อาคารแน่น ไม่มีต้นไม้ สูงขึ้น 50%) | ภาพช่องกระดาน · เขตอุตสาหกรรม | o21 | `img/prop-o21.webp` | มีแล้ว |
| P012-v2 | ร้านของฝาก (ปริมณฑล) | ภาพช่องกระดาน · เขตท่องเที่ยว | o25 | `img/prop-o25.webp` | มีแล้ว |
| P013-v2 | โฮมสเตย์ (ปริมณฑล) | ภาพช่องกระดาน · เขตท่องเที่ยว | o27 | `img/prop-o27.webp` | มีแล้ว |
| P014-v4 | ร้านอาหารซีฟู้ด (แนบภาพ P001 · จัตุรัส) | ภาพช่องกระดาน · เขตท่องเที่ยว | o28 | `img/prop-o28.webp` | มีแล้ว |
| P015-v4 | เรือนำเที่ยว (แนบภาพ P001 · จัตุรัส) | ภาพช่องกระดาน · เขตท่องเที่ยว | o31 | `img/prop-o31.webp` | มีแล้ว |
| P016-v4 | รีสอร์ตริมทะเล (แนบภาพ P001 · จัตุรัส) | ภาพช่องกระดาน · เขตท่องเที่ยว | o33 | `img/prop-o33.webp` | มีแล้ว |
| P017-v4 | ร้านขายของชำ (แนบภาพ P001 · จัตุรัส) | ภาพช่องกระดาน · เขตชุมชน | o37 | `img/prop-o37.webp` | มีแล้ว |
| P018-v4 | ตลาดนัดชุมชน (แนบภาพ P001 · จัตุรัส) | ภาพช่องกระดาน · เขตชุมชน | o39 | `img/prop-o39.webp` | มีแล้ว |
| P019-v4 | ทาวน์โฮม (แนบภาพ P001 · จัตุรัส) | ภาพช่องกระดาน · เขตชุมชน | o40 | `img/prop-o40.webp` | มีแล้ว |
| P020-v4 | หอพัก (แนบภาพ P001 · จัตุรัส) | ภาพช่องกระดาน · เขตชุมชน | o43 | `img/prop-o43.webp` | มีแล้ว |
| P021-v6 | ปั๊มน้ำมัน (แนบภาพ P001 · จัตุรัส) | ภาพช่องกระดาน · เขตชุมชน | o45 | `img/prop-o45.webp` | มีแล้ว |
| P022-v2 | จุดเริ่ม · สำนักงานใหญ่ธนาคาร (แนบภาพ P001) | ภาพช่องกระดาน · ช่องพิเศษ | o0 | `img/sq-start.webp` | มีแล้ว |
| P023a | เงินเดือน · ธนาคารสาขาอิฐแดง (แนบภาพ P001) | ภาพช่องกระดาน · ช่องพิเศษ | o12 | `img/sq-pay-o12.webp` | มีแล้ว |
| P023b | เงินเดือน · ธนาคารกระจกฟ้า (แนบภาพ P001) | ภาพช่องกระดาน · ช่องพิเศษ | o24 | `img/sq-pay-o24.webp` | มีแล้ว |
| P023c | เงินเดือน · ธนาคารหินขาวลานน้ำ (แนบภาพ P001) | ภาพช่องกระดาน · ช่องพิเศษ | o36 | `img/sq-pay-o36.webp` | มีแล้ว |
| P024a | พักผ่อน · สวนสาธารณะเขตเกษตร | ภาพช่องกระดาน · ช่องพิเศษ | o2 | `img/sq-rest-o2.webp` | มีแล้ว |
| P024b | พักผ่อน · สวนสาธารณะเขตอุตสาหกรรม | ภาพช่องกระดาน · ช่องพิเศษ | o14 | `img/sq-rest-o14.webp` | มีแล้ว |
| P024c | พักผ่อน · สวนสาธารณะเขตท่องเที่ยว | ภาพช่องกระดาน · ช่องพิเศษ | o26 | `img/sq-rest-o26.webp` | มีแล้ว |
| P024d | พักผ่อน · สวนสาธารณะเขตชุมชน | ภาพช่องกระดาน · ช่องพิเศษ | o38 | `img/sq-rest-o38.webp` | มีแล้ว |
| P025a | ถนน · สถานีขนส่ง (แนบภาพ P001) | ภาพช่องกระดาน · ช่องพิเศษ | o6 | `img/sq-road-o6.webp` | รอเจน |
| P025b | ถนน · ด่านทางด่วน (แนบภาพ P001) | ภาพช่องกระดาน · ช่องพิเศษ | o18 | `img/sq-road-o18.webp` | รอเจน |
| P025c | ถนน · สถานีรถไฟ (แนบภาพ P001) | ภาพช่องกระดาน · ช่องพิเศษ | o30 | `img/sq-road-o30.webp` | รอเจน |
| P025d | ถนน · สถานีรถไฟฟ้า (แนบภาพ P001) | ภาพช่องกระดาน · ช่องพิเศษ | o42 | `img/sq-road-o42.webp` | รอเจน |
| P026 | ศูนย์เรียนรู้ | ภาพช่องกระดาน · ช่องพิเศษ | o8, o20, o32, o44 | `img/sq-study.webp` | รอเจน |
| P027 | ตกงาน | ภาพช่องกระดาน · ช่องพิเศษ | o11 | `img/sq-jobless.webp` | รอเจน |
| P028 | ฟุ่มเฟือย | ภาพช่องกระดาน · ช่องพิเศษ | o23, o47 | `img/sq-splurge.webp` | รอเจน |
| P029 | บริจาคการกุศล | ภาพช่องกระดาน · ช่องพิเศษ | o35 | `img/sq-charity.webp` | รอเจน |
| P030a | จุดเชื่อม · สะพานรถโดยสาร (แนบภาพ P001) | ภาพช่องกระดาน · จุดเชื่อมแถบกลาง | แถบกลางข้าง o6 | `img/link-o6.webp` | รอเจน |
| P030b | จุดเชื่อม · ทางด่วนลอยฟ้า (แนบภาพ P001) | ภาพช่องกระดาน · จุดเชื่อมแถบกลาง | แถบกลางข้าง o18 | `img/link-o18.webp` | รอเจน |
| P030c | จุดเชื่อม · สะพานรถไฟ (แนบภาพ P001) | ภาพช่องกระดาน · จุดเชื่อมแถบกลาง | แถบกลางข้าง o30 | `img/link-o30.webp` | รอเจน |
| P030d | จุดเชื่อม · รางรถไฟฟ้าลอยฟ้า (แนบภาพ P001) | ภาพช่องกระดาน · จุดเชื่อมแถบกลาง | แถบกลางข้าง o42 | `img/link-o42.webp` | รอเจน |
| P031a | ที่ดินใหม่ · โรงสีข้าว (แนบภาพ P001) | ภาพช่องกระดาน · เขตเกษตรกรรม | o10 | `img/prop-o10.webp` | รอเจน |
| P031b | ที่ดินใหม่ · ท่าเรือขนส่งสินค้า (แนบภาพ P001) | ภาพช่องกระดาน · เขตอุตสาหกรรม | o22 | `img/prop-o22.webp` | รอเจน |
| P031c | ที่ดินใหม่ · สวนน้ำ (แนบภาพ P001) | ภาพช่องกระดาน · เขตท่องเที่ยว | o34 | `img/prop-o34.webp` | รอเจน |
| P031d | ที่ดินใหม่ · คลินิกเอกชน (แนบภาพ P001) | ภาพช่องกระดาน · เขตชุมชน | o46 | `img/prop-o46.webp` | รอเจน |
| P032a | สถานบันเทิง · ร้านคาราโอเกะ (แนบภาพ P001) | ภาพช่องกระดาน · เขตเกษตรกรรม | o5 | `img/sq-ent-o5.webp` | รอเจน |
| P032b | สถานบันเทิง · สนามไดรฟ์กอล์ฟ (แนบภาพ P001) | ภาพช่องกระดาน · เขตอุตสาหกรรม | o17 | `img/sq-ent-o17.webp` | รอเจน |
| P032c | สถานบันเทิง · บีชคลับ (แนบภาพ P001) | ภาพช่องกระดาน · เขตท่องเที่ยว | o29 | `img/sq-ent-o29.webp` | รอเจน |
| P032d | สถานบันเทิง · โรงภาพยนตร์ (แนบภาพ P001) | ภาพช่องกระดาน · เขตชุมชน | o41 | `img/sq-ent-o41.webp` | รอเจน |

## หลักร่วมของภาพช่องกระดาน (P001–P021)
- **หมวด:** ฉาก-พื้นหลัง (ภาพช่องกระดาน isometric)
- **เครื่องมือ:** Gemini · **สัดส่วน:** 1:1 (ภาพเดี่ยว หรือรวม 4 ภาพเป็นตาราง 2×2 ก็ได้)
- ทุกภาพใช้ส่วนหน้าเหมือนกัน ต่างกันแค่ประโยค Scene · มุมกล้องเดียวกับชุดเกษตร · **ไม่ต้องมีถนนในภาพ** (ถนนวาดในเกมแล้ว)
- ส่งภาพให้ Claude แล้วบอกหมายเลข — Claude ตัดพื้นขาว วัดจุดวาง ใส่ช่องให้

### ส่วนหน้ามาตรฐาน (ไม่มีเลข — ใช้ต่อท้ายด้วย Scene)
ใช้ตอนต้องการภาพช่องใหม่ที่ยังไม่มีในรายการ: วางข้อความนี้ แล้วพิมพ์ฉากที่ต้องการต่อท้ายเป็นภาษาอังกฤษ จากนั้นเพิ่มเป็นเลขใหม่ (P022, P023 …) ในสารบัญ · ถ้าแก้ข้อความส่วนนี้ ทุก prompt ด้านล่างต้องแก้ตามด้วย
```
Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. Modern-day Thailand setting. No text, no letters, no logos, no signs with writing, no people. Scene on the tile: 
```

## ช่องพิเศษวงนอก (P022–P029) — แนบภาพ P001 ทุกครั้ง
- เจ้าของไม่ชอบภาพซ้ำบนแผนที่ → ช่องชนิดเดียวกันหลายช่องให้ทำแบบแยก (a/b/c…) · กระดาน 48 ช่องไม่มีช่องว่างหัวมุมแล้ว · ช่องที่ยังไม่มีภาพใช้หญ้า P001

### P022 / P023 — ธนาคาร (v2 · แยก 4 แบบ)
- **เหตุที่แก้:** เจ้าของอยากให้เป็นอาคารธนาคารตึกสูง ดูดีระดับปริมณฑล · เงินเดือน 3 ช่องไม่ซ้ำแบบ · **เก็บเหรียญทองยักษ์ + ถุงเงิน** ไว้ทุกภาพ · ภาพ v1 (ซุ้มเหรียญ/ตู้ ATM ชั้นเดียว) เลิกใช้
- **สัดส่วน:** 3:4 แนวตั้ง (ให้ตึกมีที่สูง) — ถ้าแผ่นพื้นซ้อน 2 ชั้น ให้เจนใหม่แบบ 1:1

### P025 / P030 — ทางเข้าเมืองหลวง 4 ทาง + จุดเชื่อมแถบกลาง (v2)
- **เหตุที่แก้:** ไม่ให้ซ้ำ 4 ช่อง → สถานีขนส่ง (o6 เกษตร) · ด่านทางด่วน (o18 อุตสาหกรรม) · สถานีรถไฟ (o30 ท่องเที่ยว) · สถานีรถไฟฟ้า (o42 ชุมชน) · ภาพต้องต่อกันเป็นเส้นทางเดียวจากวงนอกเข้าเมือง
- **ทิศในภาพ:** ขอบหน้า-ซ้าย = ด้านนอกกระดาน · ขอบหลัง-ขวา = ด้านในเมือง (ด้าน 1 และ 3 เกมกลับภาพซ้ายขวาให้เอง) · ทางเชื่อมออกจาก **กึ่งกลางขอบหลัง-ขวา** ของช่องสถานี แล้วเข้า **กึ่งกลางขอบหน้า-ซ้าย** ของภาพจุดเชื่อม
- **ภาพจุดเชื่อม (P030):** วางบนแถบกลางกว้าง 1 ช่อง ติดช่องสถานี · มีถนนเส้นเล็ก (เทา เส้นประขาว) → แม่น้ำ (ฟ้าอมเขียว ตลิ่งทราย) → รางรถไฟ (หมอนไม้น้ำตาล) เรียงจากขอบนอกเข้าใน ให้ตรงกับที่เกมวาดไว้ · ต้องใส่โค้ดวางภาพบนแถบกลางเพิ่ม (Claude ทำตอนได้ภาพ)
- **สัดส่วน:** 1:1

### P025a — ถนน · สถานีขนส่ง
- **ช่อง:** o6 · **ไฟล์:** `img/sq-road-o6.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Orientation (important): the front-left edge of the tile faces the outside of the board; the back-right edge faces the city center, where a small road runs right alongside it just outside the tile. The main entrance faces the back-right edge, and the transport link leaves the tile exactly at the middle of the back-right edge. Scene on the tile: a modern provincial bus terminal: a long curved white canopy over bus bays with three colorful intercity coaches, a glass waiting hall, and a short access road from the bays leading straight to the middle of the back-right edge.
```

### P025b — ถนน · ด่านทางด่วน
- **ช่อง:** o18 · **ไฟล์:** `img/sq-road-o18.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Orientation (important): the front-left edge of the tile faces the outside of the board; the back-right edge faces the city center, where a small road runs right alongside it just outside the tile. The main entrance faces the back-right edge, and the transport link leaves the tile exactly at the middle of the back-right edge. Scene on the tile: an expressway toll plaza: a row of toll booths under a wide canopy, an elevated expressway on concrete pillars rising from the toll plaza and leaving the tile at the middle of the back-right edge, a few cars and a container truck, landscaped slopes.
```

### P025c — ถนน · สถานีรถไฟ
- **ช่อง:** o30 · **ไฟล์:** `img/sq-road-o30.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Orientation (important): the front-left edge of the tile faces the outside of the board; the back-right edge faces the city center, where a small road runs right alongside it just outside the tile. The main entrance faces the back-right edge, and the transport link leaves the tile exactly at the middle of the back-right edge. Scene on the tile: a charming modern seaside railway station: a station building with a red tiled roof and a long covered platform, a passenger train standing at the platform, two railway tracks running out of the tile at the middle of the back-right edge, a few palm trees.
```

### P025d — ถนน · สถานีรถไฟฟ้า
- **ช่อง:** o42 · **ไฟล์:** `img/sq-road-o42.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Orientation (important): the front-left edge of the tile faces the outside of the board; the back-right edge faces the city center, where a small road runs right alongside it just outside the tile. The main entrance faces the back-right edge, and the transport link leaves the tile exactly at the middle of the back-right edge. Scene on the tile: an elevated skytrain station: a sleek station box on tall concrete pillars with a curved glass roof, a modern skytrain stopped at the platform, escalator stairs down to a small plaza, and the elevated viaduct leaving the tile at the middle of the back-right edge.
```

### P030a — จุดเชื่อม · สะพานรถโดยสาร
- **ช่อง:** แถบกลางข้าง o6 · **ไฟล์:** `img/link-o6.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. This tile is a connector piece between the outer ring and the city. Three parallel strips run across the whole tile, parallel to the front-left edge, in this order from the front-left edge to the back-right edge: (1) right along the front-left edge, a narrow two-lane gray asphalt road with a dashed white center line; (2) in the middle, a turquoise river with sandy banks; (3) near the back-right edge, a single railway track with brown sleepers on gravel; green grass in between. Each strip runs fully from edge to edge so it continues seamlessly into the neighboring tiles. Crossing these strips straight from the middle of the front-left edge to the middle of the back-right edge: a two-lane road starting from a T-junction with the small road, with a city bus on it, crossing the river on a low concrete bridge and passing the railway at a level crossing with red-and-white barriers.
```

### P030b — จุดเชื่อม · ทางด่วนลอยฟ้า
- **ช่อง:** แถบกลางข้าง o18 · **ไฟล์:** `img/link-o18.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. This tile is a connector piece between the outer ring and the city. Three parallel strips run across the whole tile, parallel to the front-left edge, in this order from the front-left edge to the back-right edge: (1) right along the front-left edge, a narrow two-lane gray asphalt road with a dashed white center line; (2) in the middle, a turquoise river with sandy banks; (3) near the back-right edge, a single railway track with brown sleepers on gravel; green grass in between. Each strip runs fully from edge to edge so it continues seamlessly into the neighboring tiles. Crossing these strips straight from the middle of the front-left edge to the middle of the back-right edge: an elevated expressway on tall concrete pillars passing high above the road, the river and the railway, with a container truck and two cars on it.
```

### P030c — จุดเชื่อม · สะพานรถไฟ
- **ช่อง:** แถบกลางข้าง o30 · **ไฟล์:** `img/link-o30.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. This tile is a connector piece between the outer ring and the city. Three parallel strips run across the whole tile, parallel to the front-left edge, in this order from the front-left edge to the back-right edge: (1) right along the front-left edge, a narrow two-lane gray asphalt road with a dashed white center line; (2) in the middle, a turquoise river with sandy banks; (3) near the back-right edge, a single railway track with brown sleepers on gravel; green grass in between. Each strip runs fully from edge to edge so it continues seamlessly into the neighboring tiles. Crossing these strips straight from the middle of the front-left edge to the middle of the back-right edge: a double railway track coming from the middle of the front-left edge, crossing the small road at a level crossing with red-and-white barriers, crossing the river on a steel truss railway bridge, and joining the railway near the back-right edge with a switch.
```

### P030d — จุดเชื่อม · รางรถไฟฟ้าลอยฟ้า
- **ช่อง:** แถบกลางข้าง o42 · **ไฟล์:** `img/link-o42.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. This tile is a connector piece between the outer ring and the city. Three parallel strips run across the whole tile, parallel to the front-left edge, in this order from the front-left edge to the back-right edge: (1) right along the front-left edge, a narrow two-lane gray asphalt road with a dashed white center line; (2) in the middle, a turquoise river with sandy banks; (3) near the back-right edge, a single railway track with brown sleepers on gravel; green grass in between. Each strip runs fully from edge to edge so it continues seamlessly into the neighboring tiles. Crossing these strips straight from the middle of the front-left edge to the middle of the back-right edge: the elevated skytrain viaduct on tall slim pillars passing high above the road, the river and the railway, with a short skytrain on it.
```

### P026 — ศูนย์เรียนรู้
- **ช่อง:** o8, o20, o32, o44 · **ไฟล์:** `img/sq-study.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Scene on the tile: a modern community learning center / small library: glass-front building with bookshelves visible, outdoor reading tables, a tree with a bench.
```

### P027 — ตกงาน
- **ช่อง:** o11 · **ไฟล์:** `img/sq-jobless.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Scene on the tile: a quiet closed-down small office: shutter half closed, cardboard boxes stacked outside, a lonely bench, wilted potted plant, slightly muted colors.
```

### P028 — ฟุ่มเฟือย
- **ช่อง:** o23, o47 · **ไฟล์:** `img/sq-splurge.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Scene on the tile: a flashy luxury boutique corner: a shiny sports car on display, shopping bags piled up, a glamorous glass shop front with gold trim.
```

### P029 — บริจาคการกุศล
- **ช่อง:** o35 · **ไฟล์:** `img/sq-charity.webp` · **สถานะ:** รอเจน · **แนบ:** ภาพ P001
```
Use the attached image as the exact template for the ground tile: same square shape, same size, same angle, same position. Only change what is on top of the tile. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, warm natural colors, clean ink outlines, flat painted look (not a 3D render). One single square ground tile seen from an isometric angle: diamond-shaped top, thin brown soil edge visible on the two front sides, centered on a pure white background, nothing outside the tile. The ground tile is a PERFECT SQUARE: all four sides equal length, the diamond is symmetric — left and right corners at exactly the same height, front corner exactly centered below the top corner. Never stretch the tile into a rectangle; fit the scene inside the square. Setting: modern suburban Thailand near Bangkok, clean and tidy, NOT rural. No utility poles, no power lines, no overhead wires. No text, no letters, no numbers, no logos, no signs with writing, no people. Scene on the tile: a warm charity point: a small pavilion with donation boxes, food and clothes boxes being shared, a heart-shaped garden bed, gentle colors.
```

## กระดาน 48 ช่อง (เพิ่ม 2026-11-16) — ช่องใหม่ 8 ช่อง · แนบภาพ P001
- วงนอกเปลี่ยนจาก 40 เป็น 48 ช่อง → **เลขช่องวงนอกเลื่อนทั้งหมด** (คลังนี้แก้เลขเป็นเลขใหม่แล้ว · ไฟล์ภาพเปลี่ยนชื่อตาม)
- เขตละ 2 ช่องใหม่: ที่ดิน 1 (P031) + สถานบันเทิง 1 (P032 · พักผ่อนแบบเสียเงิน ฿1,000–20,000)
- prompt ทั้ง 8 ภาพ (P031a–d ที่ดินใหม่ · P032a–d สถานบันเทิง) อยู่ที่ `claude/image-prompts-48.md`

## ย้ายไปไฟล์อื่น (มีภาพแล้ว)
- `claude/image-prompts-tiles.md`: P014-v4, P015-v4, P016-v4, P017-v4, P018-v4, P019-v4, P020-v4, P021-v6, P012-v2, P013-v2, P001, P002, P003, P004, P005, P006, P007, P008, P009, P010, P011-v3
- `claude/image-prompts-special.md`: P022-v2, P023a, P023b, P023c, P024a, P024b, P024c, P024d

## รุ่นที่เลิกใช้ (เก็บแค่หัวข้อ)
- P022 —  ซุ้มประตูเหรียญทอง
- P023 —  ตู้ ATM ชั้นเดียว
- P024 — พักผ่อน (แยกเป็น 4 แบบ ตามเขต · ตัวรวมเลิกใช้)
- P025 —  จุดพักรถริมทาง (ภาพเดียว 4 ช่อง)
- [หมายเหตุกลุ่ม] ชุดแนบภาพ P001 (P014–P021 รุ่นล่าสุด) — ตัวที่ใช้งาน
- ชุดปริมณฑล (P012-v2, P013-v2 ยังใช้งาน · ที่เหลือเลิกใช้)
- P014-v3 — ร้านอาหารซีฟู้ด ( — แผ่นพื้นผืนผ้า แทนด้วยรุ่นแนบภาพ P001)
- P014-v2 —  (ริมแม่น้ำ) ร้านอาหารซีฟู้ด
- P015-v3 — เรือนำเที่ยว ( — แผ่นพื้นผืนผ้า แทนด้วยรุ่นแนบภาพ P001)
- P015-v2 —  (ริมแม่น้ำ) เรือนำเที่ยว
- P016-v3 — รีสอร์ตริมทะเล ( — แผ่นพื้นผืนผ้า แทนด้วยรุ่นแนบภาพ P001)
- P016-v2 —  (ริมแม่น้ำ) รีสอร์ตริมน้ำ
- เขตชุมชน v3 (เลิกใช้ — แทนด้วยชุดแนบภาพ P001)
- P017-v3 — ร้านขายของชำ ( แทนด้วย v4)
- P018-v3 — ตลาดนัดชุมชน ( แทนด้วย v4)
- P019-v3 — ทาวน์โฮม ( แทนด้วย v4)
- P020-v3 — หอพัก ( แทนด้วย v4)
- P021-v5 — ปั๊มน้ำมัน ( — แผ่นพื้นผืนผ้า แทนด้วยรุ่นแนบภาพ P001)
- P021-v4 —  ปั๊มน้ำมัน (ร้านค้าเด่นเกิน)
- P021-v3 —  ปั๊มน้ำมัน (หัวจ่ายเล็กเกิน)
- P017-v2 —  ร้านขายของชำ
- P018-v2 —  ตลาดนัดชุมชน
- P019-v2 —  ทาวน์โฮม
- P020-v2 —  หอพัก
- P021-v2 —  ปั๊มน้ำมัน
- P011 — นิคมอุตสาหกรรม (v1 ·  แทนด้วย P011-v2)
- P011-v2 — นิคมอุตสาหกรรม ( — ได้แผ่นพื้นซ้อน 2 ชั้น)
- P012 — ร้านของฝาก (v1 ·  — ออกแนวชนบท แทนด้วย P012-v2)
- P013 — โฮมสเตย์ (v1 ·  — ออกแนวชนบท แทนด้วย P013-v2)
- P014 — ร้านอาหารซีฟู้ด (v1 ·  — ออกแนวชนบท แทนด้วย P014-v2)
- P015 — เรือนำเที่ยว (v1 ·  — ออกแนวชนบท แทนด้วย P015-v2)
- P016 — รีสอร์ตริมทะเล (v1 ·  — ออกแนวชนบท แทนด้วย P016-v2)
- P017 — ร้านขายของชำ (v1 ·  — ออกแนวชนบท แทนด้วย P017-v2)
- P018 — ตลาดนัดชุมชน (v1 ·  — ออกแนวชนบท แทนด้วย P018-v2)
- P019 — ทาวน์โฮม (v1 ·  — ออกแนวชนบท แทนด้วย P019-v2)
- P020 — หอพัก (v1 ·  — ออกแนวชนบท แทนด้วย P020-v2)
- P021 — ปั๊มน้ำมัน (v1 ·  — ออกแนวชนบท แทนด้วย P021-v2)
