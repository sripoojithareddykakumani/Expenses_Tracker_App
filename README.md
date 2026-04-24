# 💰 Expense Tracker App

## 📌 Overview

This project is a web-based application that helps users track daily expenses, monitor budgets, and visualize spending patterns with interactive charts and insights. It is designed for real-time usage and can be accessed on both desktop and mobile devices.

## 🚀 Features

* ➕ Add, edit, and delete expenses
* 📊 Monthly expense trends (graph visualization)
* 🥧 Category-wise distribution (pie chart)
* 📅 Daily, weekly, and monthly tracking
* 🔍 Search and filter (date range + notes)
* 💰 Budget tracking with alerts
* ⚠️ Smart warnings when nearing/exceeding budget
* 📈 Insights (top category, weekly comparison)
* 📥 Export data as CSV
* 🌙 Dark mode support
* 📱 Mobile-friendly UI (can be added to home screen)

## 🛠️ Technologies Used

* Python
* Flask
* SQLite (local development)
* PostgreSQL (production database)
* HTML
* CSS
* JavaScript
* Chart.js

## ▶️ How to Run (Local)

1. Install dependencies:
   pip install flask psycopg2-binary

2. Run the app:
   python app.py

3. Open in browser:
   http://127.0.0.1:5000

## 🌐 Deployment (Render)

1. Push project to GitHub

2. Create PostgreSQL database on Render

3. Create Web Service

4. Add environment variable:
   DATABASE_URL = your_database_url

5. Use:
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app

## 📱 Mobile Usage

1. Open deployed link in browser
2. Add to Home Screen
3. Use like a mobile app

## 📂 Project Structure

Expense_Tracker/
│
├── app.py
├── database.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│
├── static/
│   ├── style.css
│   └── assets/

## 💡 Future Improvements

* 🔐 User authentication (login/signup)
* 📊 Advanced analytics & AI insights
* 🔔 Expense reminders & notifications
* ☁️ Cloud backup & sync
* 📱 Native mobile app version

## 🏆 Highlights

* Real-world full-stack project
* Dual database support (SQLite + PostgreSQL)
* Production-ready deployment
* Clean and responsive UI

## 👩‍💻 Author
Kakumani Sri Poojitha
