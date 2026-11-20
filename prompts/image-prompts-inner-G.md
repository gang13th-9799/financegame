# คลัง Prompt — วงใน ชุด G ย่านธุรกิจ (i16–i23) + ส่วนหน้า v8 · อัปเดต 2026-11-20

ต่อจาก `claude/image-prompts-inner.md` · ด้าน 2 (แถว 11) เกมไม่กลับภาพ · i20 สถานีรถไฟมีแล้ว

## บทเรียน 2026-11-20 (เจ้าของ)
- ตึกที่ชั้นล่างไม่ถึงขอบแผ่น = ดูเล็ก ไม่สวย (i8 i9 i11 i14 i15 i19 i21) · ภาพแบบเป็นกล่องเต็ม → Gemini ทำตึกกล่อง ไม่สวย (เลิกใช้ `guide-full-tall/mid`)
- ✅ ใช้ได้: ภาพแบบ `guide-podium.png` (Downloads/outputs · แผ่นตามแม่แบบ + ฐานเตี้ยเต็มแผ่น) + ส่วนหน้า v7/v8 → i14 i15 ออกมาดี
- ชั้นล่างต้องมี **ต้นไม้ พุ่มไม้ กระบะต้นไม้ เรียงชิดผนังรอบตึก** บนขอบแผ่น (เจ้าของ)
- ป้ายข้อความ: ห้ามทั่วไป · **ยกเว้น i15 ศูนย์การค้า ("Shopping Mall") เจ้าของอนุญาต** · ภาพมีตัวหนังสือในด้าน 1/3 ต้องกลับซ้ายขวาก่อนใส่เกม
- ภาพที่แผ่นใหญ่กว่าแม่แบบ: ตัดตามมุมแผ่นของภาพเองแล้วย่อ (เจ้าของโอเค)

## ส่วนหน้า v8 (แนบ `guide-podium.png` · ต่อท้ายด้วยฉาก)
```
Refine the attached sketch into a finished illustration. It is an isometric game board tile that is already laid out correctly. Keep the same thin gray concrete slab, the same size, angle and position in the frame, with SHARP POINTED left and right corners and the white margin around it. The low beige block on the slab is ONLY a guide for the building's ground floors: the bottom three or four floors of the building must cover almost the whole slab like that block — walls rising close to the edges of the slab on all four sides, no plaza, no empty ground. Along the foot of the walls, all around the building, put a narrow strip of lush greenery right at the slab edge: planter boxes, trimmed hedges, flowering bushes and small trees hugging the walls. Do NOT copy the block as a plain box: turn it into a richly detailed podium with glass, stone, entrances and terraces. ABOVE the podium the building is completely free in shape — a tower, curves, setbacks, stepped terraces, domes or spires as the design needs — big, bold and impressive, never a plain box. Isometric game board tile, soft painted manhwa / webtoon illustration style, gentle cel shading, hand-drawn clean ink outlines, painted textures, flat painted look (not a 3D render). Bright sunny daylight, warm, bright, cheerful colors — not dull. Setting: the dense downtown of a modern, prosperous Asian capital city like central Bangkok — luxurious and clean. The building is empty: no people anywhere, not even tiny figures inside the windows. Do NOT add any vehicles, no utility poles, no wires. No text, no letters, no numbers, no logos, no signs with writing, no shop signs. Pure white background, nothing outside the tile. The building is:
```

## เจนใหม่ชุด F (ใช้ v8)
- **i8 ตลาดหลักทรัพย์:** `the national STOCK EXCHANGE: a grand trading-hall podium of white stone and dark blue glass with giant wall screens showing colorful chart lines and candlestick graphs (graphics only), a golden bull sculpture on the podium roof terrace, and a tall dark-blue glass skyscraper rising from it with a sharp crown at the top.`
- **i9 ร้านอาหาร:** `a stylish dining building: several floors of glass-fronted restaurants with warm lights, colorful awnings and hanging plants on the terraces, a rooftop dining terrace with string lights, umbrellas and tables.`
- **i11 คอมมูนิตี้มอลล์:** `a trendy community mall: stacked boxes of boutique shops and cafés with warm wood and glass facades, terraces with plants and café umbrellas, a rooftop garden with a small playground.`

## ชุด G — ตาราง
| เลข | ช่อง | ชนิด · ชื่อ | ไฟล์ |
|---|---|---|---|
| P039a | i16 | เงินเดือน · ตึกแฝดสำนักงานใหญ่บริษัท | `sq-pay-i16` |
| P039b | i17 | ที่ดิน · โคเวิร์กกิ้งสเปซ | `prop-i17` |
| P039c | i18 | ศูนย์ธุรกิจ · ศูนย์นวัตกรรม | `sq-bizc-i18` |
| P039d | i19 | ที่ดิน · อาคารสำนักงาน (v1 ไม่เต็มแผ่น → เจนใหม่ v8) | `prop-i19` |
| P039e | i21 | ที่ดิน · โรงแรมธุรกิจ (v1 ไม่เต็มแผ่น → เจนใหม่ v8) | `prop-i21` |
| P039f | i22 | ศูนย์เรียนรู้ · วิทยาเขตมหาวิทยาลัย | `sq-study-i22` |
| P039g | i23 | ที่ดิน · ศูนย์ประชุม | `prop-i23` |

### ฉากชุด G (ต่อท้าย v8)
- **P039a · i16:** `the GRAND CORPORATE HEADQUARTERS of a giant conglomerate: elegant twin glass skyscrapers in silver and champagne gold rising from one massive podium, joined high up by a glass sky bridge, gold crowns on both tops, a rooftop garden terrace on the podium with trees and a reflecting pool.`
- **P039b · i17:** `a trendy creative coworking building: four to five floors of big warm-lit glass windows showing open shared desks, bright lounges and meeting pods, warm wood and white panels, terraces full of plants and bean bags, a rooftop garden with a wooden deck and string lights.`
- **P039c · i18:** `a futuristic INNOVATION AND STARTUP HUB: stacked white and glass boxes at playful angles with colorful accent panels in teal, coral and yellow, a large glowing glass atrium, green terraces, a rooftop with solar panels, a small wind turbine and a garden.`
- **P039d · i19:** `a prime-grade office tower: a tall, sleek tower of blue-green reflective glass with crisp white vertical fins, stepped sky terraces with trees, a helipad on the roof.`
- **P039e · i21:** `a luxury business hotel: a tall elegant tower of cream stone and warm bronze glass, rows of balconies with plants, a grand glass lobby podium with golden lights, a rooftop infinity pool with sun loungers and palm trees, and a sky bar terrace.`
- **P039f · i22:** `a modern UNIVERSITY CAMPUS building: a grand red-brick and glass academic hall with tall arched windows, a white planetarium dome and a small observatory telescope dome on the roof, lecture halls visible through the glass, rooftop garden courtyards with trees.`
- **P039g · i23:** `a huge modern CONVENTION AND EXHIBITION CENTER: a wide building with a dramatic sweeping white wave-shaped roof, tall glass walls showing a vast exhibition hall with colorful booths, flag poles with plain colored flags along the roof edge, rooftop green patches.`
