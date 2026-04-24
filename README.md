💰 Expense Tracker App
📌 Overview

This project is a web-based application that helps users track daily expenses, monitor budgets, and visualize spending patterns with interactive charts and insights. It is designed for real-time usage and can be accessed on both desktop and mobile devices.

🚀 Features
➕ Add, edit, and delete expenses
📊 Monthly expense trends (graph visualization)
🥧 Category-wise distribution (pie chart)
📅 Daily, weekly, and monthly tracking
🔍 Search and filter (date range + notes)
💰 Budget tracking with alerts
⚠️ Smart warnings when nearing/exceeding budget
📈 Insights (top category, weekly comparison)
📥 Export data as CSV
🌙 Dark mode support
📱 Mobile-friendly UI (can be added to home screen)

🛠️ Technologies Used
Python
Flask
SQLite (local development)
PostgreSQL (production database)
HTML, CSS, JavaScript
Chart.js

▶️ How to Run (Local)
Install dependencies:
pip install flask psycopg2-binary
Run the app:
python app.py
Open in browser:
http://127.0.0.1:5000

🌐 Deployment (Render)
Push project to GitHub
Create PostgreSQL database on Render
Create Web Service
Add environment variable:
DATABASE_URL = your_database_url
Use:
Build: pip install -r requirements.txt
Start: gunicorn app:app

📱 Mobile Usage
Open deployed link in browser
Add to Home Screen
Use like a mobile app

📂 Project Structure
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
│   └── (icons, assets)

💡 Future Improvements
🔐 User authentication (login/signup)
📊 Advanced analytics & AI insights
🔔 Expense reminders & notifications
☁️ Cloud backup & sync
📱 Native mobile app version

