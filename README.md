# 🎓 SnapClass AI - Smart Attendance Management System

An AI-powered attendance management system that automates classroom attendance using Facial Recognition technology.

SnapClass enables teachers to mark attendance instantly by capturing a classroom image, identifying students through AI, and generating attendance reports automatically.

---

## 🚀 Features

* 📷 AI-powered facial recognition attendance
* ⚡ Instant attendance marking
* 👨‍🏫 Separate Teacher Portal
* 👨‍🎓 Separate Student Portal
* 📊 Attendance analytics and reports
* 📁 Export attendance records to CSV
* 🔐 Secure authentication system
* 🧠 Face embedding-based identification
* ☁️ Cloud-ready deployment
* 📈 Real-time attendance tracking

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / Computer Vision

* OpenCV
* DeepFace / Face Recognition
* NumPy

### Data Processing

* Pandas

### Database

* SQLite / PostgreSQL

### Deployment

* Streamlit Cloud

---

## 📂 Project Structure

```
SnapClass-AI/

├── app/
│ ├── student/
│ ├── teacher/
│ ├── auth/
│ ├── ai/
│ ├── database/
│ └── utils/
│
├── datasets/
├── models/
├── reports/
├── assets/
│
├── streamlit_app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── LICENSE
```
---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/your-username/SnapClass-AI.git

cd SnapClass-AI

### 2️⃣ Create Virtual Environment

python -m venv venv

venv\Scripts\activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Configure Environment Variables

Create a .env file

DATABASE_URL=your_database_url

SECRET_KEY=your_secret_key

MODEL_PATH=models/

### 5️⃣ Run Application

streamlit run streamlit_app.py

---

## 🎯 How It Works

### Student Registration

* Upload student photos
* Generate facial embeddings
* Store student profiles

### Attendance Marking

* Teacher captures classroom image
* AI detects faces
* AI recognizes registered students
* Attendance is marked automatically

### Report Generation

* Attendance stored in database
* Generate attendance analytics
* Export reports in CSV format

---

## 📸 System Modules

### 👨‍🎓 Student Portal

* View attendance history
* Profile management
* Attendance statistics

### 👨‍🏫 Teacher Portal

* Manage students
* Mark attendance
* View reports
* Export records

### 🤖 AI Engine

* Face Detection
* Face Recognition
* Attendance Processing
* Identity Verification

---

## 🌟 Future Enhancements

* 🎙️ Voice Recognition Attendance
* 📱 Mobile Application
* ☁️ Cloud Storage Integration
* 📊 Advanced Analytics Dashboard
* 🔔 Attendance Notifications
* 📄 PDF Report Generation

---

## 👨‍💻 Author

Kris Kalariya

GitHub:
https://github.com/Kris-Kalariya

---

## ⭐ Contribution

Contributions are welcome!

Feel free to fork this repository and improve the project.

---

## 📜 License

This project is licensed under the MIT License.
