# 🧠 Smart Attendance & Absence Detection System

📊 **"Smart Absence Tracker + Employee Truancy Detection (Simulation)"**

A modern and interactive web-based dashboard built using Python & Flask to monitor employee attendance and detect suspicious absence patterns (alfa) using simple data analytics.

---

## 🚀 Key Features

- ✅ **Automated Attendance Summary**
  - Statistics of total present, absent (alfa), and sick.
  - Summary table per employee with filtering capability.

- 📈 **Pie Chart Visualization**
  - Displays attendance status distribution (Present, Absent, Sick).
  - Modern, responsive, and animated chart.

- 🔍 **Truancy Pattern Detection**
  - Detects employees frequently absent on specific days.
  - Highlights potential truants based on behavioral patterns.

- 📥 **Export to PDF/Excel**
  - Export attendance summary reports for HR documentation.

- 👤 **Employee Filtering**
  - Analyze attendance data per individual.

---

## 🛠️ Tech Stack

| Layer       | Technologies                   |
|-------------|--------------------------------|
| Backend     | Python, Flask                  |
| Frontend    | HTML5, CSS3, Bootstrap         |
| Visualization| Chart.js                      |
| Data        | Pandas, CSV                    |
| Export      | Pandas ExcelWriter, pdfkit     |

---

## 🗂️ Project Structure

```
Smart-Attendance-Flask/
├── app.py
├── requirements.txt
├── data/
│   └── attendance_data.csv
├── src/
│   ├── bolos_detection.py
│   └── data_processing.py
├── templates/
│   ├── index.html
│   └── layout.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
```

---

## ⚙️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/ZaanmaVerse/Smart-Attendance-Dashboard.git
cd Smart-Attendance-Dashboard
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Start the Flask App
```bash
python app.py
```

Access the app at: [http://localhost:5000](http://localhost:5000)

---

## 📌 Sample Data (CSV Format)

File: `data/attendance_data.csv`

```csv
ID,Name,Date,Status
1,Andi,2025-07-01,Present
2,Budi,2025-07-01,Absent
3,Citra,2025-07-01,Sick
...
```

---

## 🧠 Potential Future Improvements

- Integration with biometric attendance (Face/Fingerprint)
- Absenteeism prediction using Machine Learning
- Automated HR notifications via email/WhatsApp

---

## 👨‍💻 Developer

**Zaidan Mahfudz Azzam Saidi**  
IT Student & AI/Cybersecurity Enthusiast  
[LinkedIn](www.linkedin.com/in/zaidanmahfudz)

---

## 📄 License

This project is open-source and intended for educational/simulation purposes only. Use responsibly.
