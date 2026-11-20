# คลัง Prompt — ตรงกลางกระดานเป็นสวนสาธารณะ P042 · เพิ่ม 2026-11-20

แทนเมืองกลาง P041 (Gemini ไม่ยอมเว้นถนนด้านหลัง ตึกแน่นติดช่องเดินแถวหลัง) — เจ้าของสั่ง: สวนสาธารณะเต็มพื้นที่ ต้นไม้ไม่สูง มีพุ่มไม้ตัดแต่งเป็นรูปโลโก้เกม
- ภาพร่าง `sketch-park.png` (สคริปต์ `/home/claude/p/sketchPark.py`) · แผ่นเพชร T(1024,830) R(1999,1415) L(49,1415) · ถนนวงรอบครบ 4 ด้าน · สนามหญ้า · ทางเดินวงกลม + ทางเข้า 4 ทิศ · ต้นไม้เตี้ยเรียงขอบ · แปลงดอกไม้ 4 มุม
- **พุ่มไม้รูปโลโก้:** วางรูปทรงจาก `tools/logomask.npy` จริง ลงบนพื้นที่ u,v .25–.75 (ตามกฎห้ามเปลี่ยนรูปทรงโลโก้) · หลัง Gemini เกลา ต้องเทียบรูปทรงกับ mask ถ้าเพี้ยน Claude วาดพุ่มทับเองจาก mask

### P042 — แนบ `sketch-park.png` รูปเดียว · 1:1
```
Refine the attached sketch into a finished illustration. It is the isometric centerpiece of a game board, already laid out correctly. Keep EVERYTHING in the same place: the same single diamond-shaped slab with its thin gray edge, the same size, angle and position in the frame, the gray ring street with white dashed lines running around ALL FOUR edges, the cream sidewalks, the green lawn, the round paved path and the four short paths, the pink flower beds and the rows of small trees along the edges. Turn it into a beautiful, calm, well-kept PUBLIC PARK in the middle of a modern Asian capital city.
MOST IMPORTANT: the big dark-green shape in the center is a low, neatly TRIMMED TOPIARY HEDGE that must keep EXACTLY the same outline as drawn — a rounded square frame with four round blobs inside, like a garden emblem. Do not change, simplify or redesign this shape in any way; only give it a soft clipped-hedge leaf texture, gentle shading and a thin shadow on the lawn. Inside the frame, fine light-green lawn.
Everything stays LOW: small round trees and bushes only (no tall trees, no buildings, no towers, no tall structures). Add small details at ground level: benches along the paths, a few lamp posts, low flower borders along the hedge, a small round fountain is NOT needed. Isometric, soft painted manhwa / webtoon illustration style, gentle cel shading, hand-drawn clean ink outlines, painted textures, flat painted look (not a 3D render). Bright sunny daylight, warm, bright, cheerful colors — not dull. Pure white background, nothing outside the slab. No people, no vehicles, no utility poles, no wires. No text, no letters, no numbers, no logos, no signs with writing.
```
