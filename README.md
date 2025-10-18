# TCAS System (ระบบการสมัครสอบ TCAS)

โปรแกรมจัดการการสมัครสอบ TCAS สำหรับนักเรียน — เมนูหลักประกอบด้วย:
1. Student Menu (เมนูนักเรียน)
2. Course information (ข้อมูลหลักสูตร)
3. TCAS Applicant and Fee Statistics Report (รายงานสถิติผู้สมัครและค่าธรรมเนียม)
4. Exit Program

การติดตั้ง
- ติดตั้ง Python 3.10+ (หรือเวอร์ชันที่ติดตั้งแล้วในระบบ)
- ติดตั้งไลบรารีที่จำเป็น:
```bash
pip install wcwidth
```

วิธีการรัน
```bash
python main.py
```
จากนั้นเลือกเมนูตามที่โปรแกรมแสดง

คำอธิบายฟีเจอร์หลัก 
- Student Menu 
  - ลงทะเบียนและจัดการข้อมูลผู้สมัคร 
- Course information 
  - ค้นหาและแสดงข้อมูลมหาวิทยาลัย คณะ และหลักสูตร
- Report 
  - สร้างรายงานสถิติเกี่ยวกับผู้สมัครและค่าธรรมเนียม

โครงสร้างโปรเจค (โดยย่อ)
```
Tcas/
├── main.py
├── README.md
├── data_information/
│   ├── __init__.py
│   ├── course_info.py
│   ├── student_tcas.py
│   ├── report_register.py
│   └── datas/          
```