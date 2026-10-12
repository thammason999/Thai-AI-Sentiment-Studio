# Thai AI Sentiment Studio

เว็บแอป Python + Flask สำหรับรับข้อความภาษาไทยและเรียก AIForThai EmoNews เพื่อวิเคราะห์ความรู้สึก

> หมายเหตุ: ต้องมี API Key และสิทธิ์ใช้งานบริการจาก AIForThai ก่อน การมีโค้ดเพียงอย่างเดียวไม่ได้รับประกันว่า API จะเรียกได้ทุกบัญชี ตรวจสอบชื่อบริการ วิธีติดตั้ง และรูปแบบผลลัพธ์จากเอกสารล่าสุดของ AIForThai เสมอ

## ความสามารถ

- หน้าเว็บภาษาไทยสำหรับกรอกข้อความ
- เรียกบริการ AIForThai ผ่านแพ็กเกจ `aift`
- แสดงผลตอบกลับจากบริการ
- แยก API Key ไว้ใน `.env` และกันไฟล์นี้ออกจาก Git

## สิ่งที่ต้องติดตั้ง

- Python 3.10 ขึ้นไป (แนะนำเวอร์ชันที่แพ็กเกจ AIForThai รองรับ)
- VS Code หรือ editor อื่น
- AIForThai API Key ที่มีสิทธิ์ใช้บริการ sentiment / EmoNews

## วิธีติดตั้งบน Windows

1. แตกไฟล์ ZIP และเปิดโฟลเดอร์ `ThaiAIProject` ใน VS Code
2. เปิด Terminal ใน VS Code
3. สร้าง virtual environment:

   ```bash
   python -m venv venv
   ```

4. เปิดใช้งาน environment:

   ```bash
   venv\\Scripts\\activate
   ```

5. ติดตั้ง dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. คัดลอก `.env.example` แล้วเปลี่ยนชื่อสำเนาเป็น `.env`
7. เปิด `.env` แล้วใส่ API Key จริง:

   ```env
   AIFORTHAI_API_KEY=your_real_api_key
   ```

8. รันแอป:

   ```bash
   python app.py
   ```

9. เปิดเบราว์เซอร์ไปที่ http://127.0.0.1:5000

## วิธีใช้งาน

พิมพ์ข้อความภาษาไทย เช่น “ร้านนี้อาหารอร่อยและบริการดีมาก” แล้วกด “วิเคราะห์ข้อความ” ผลลัพธ์จะมาจาก API หากบัญชีมีสิทธิ์ใช้งานและตั้งค่า API ถูกต้อง

## หากเรียก API ไม่สำเร็จ

- ตรวจสอบ API Key และสิทธิ์การใช้งาน
- ตรวจสอบเอกสาร AIForThai ปัจจุบันว่าใช้ `from aift import setting`, `from aift.nlp import sentiment`, `setting.set_api_key(...)` และ `sentiment.analyze(..., engine="emonews")` ได้กับเวอร์ชันที่ติดตั้งหรือไม่
- หาก API เปลี่ยนชื่อ endpoint หรือรูปแบบ ให้ปรับฟังก์ชัน `analyze_with_aiforthai()` ใน `app.py`
- อย่าโพสต์ API Key ในภาพหน้าจอหรือ GitHub

## อัปโหลดไป GitHub

สร้าง repository เปล่าบน GitHub แล้วรันจากโฟลเดอร์โปรเจกต์:

```bash
git init
git add .
git commit -m "Create Thai AI sentiment web app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ThaiAIProject.git
git push -u origin main
```

แทน `YOUR-USERNAME` ด้วยชื่อบัญชีจริงของคุณ ถ้า `origin` มีอยู่แล้ว ให้ตรวจด้วย `git remote -v` ก่อน ไม่ต้องเพิ่มซ้ำ

## ข้อควรระวัง

- `.env` ถูกระบุใน `.gitignore` อย่าใช้ `git add -f .env`
- แอปนี้เป็นตัวอย่างสำหรับรันในเครื่อง (`debug=True`) ไม่ควรนำขึ้นใช้งานจริงโดยไม่ปรับการตั้งค่าความปลอดภัย
- ยังไม่ได้รวม VAJAX/บริการที่สอง เพราะต้องยืนยันชื่อบริการและ API endpoint จากโจทย์หรือเอกสารอาจารย์ก่อน
