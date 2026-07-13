# Health Monitoring Portal

## About
Health Monitoring Portal (HMP) is a full-stack web application built with Python and Django that digitizes paper-based medical records. It provides a centralized platform where patient history, surgeries, medicines, and treatments can be securely stored and accessed, helping doctors and hospitals deliver faster, more informed care across cities. The system reduces dependency on physical files and improves continuity of care between different healthcare providers.

## Features
- **Admin Module** – Manage users, hospitals, doctors, and overall system data
- **Patient Module** – Register, view personal health records, treatment history, and medical documents
- **Hospital Module** – Manage hospital-specific data and patient admissions
- **Doctor Module** – Access patient history, add treatment records, and manage prescriptions
- Secure storage of ID proofs and medical certificates
- Digitized medical records replacing physical paperwork
- Cross-city access to patient health history for continuity of care

## Technologies Used
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite

## Project Structure
├── certificates/     # Medical certificates storage
├── doctor/           # Doctor module app
├── hmp/              # Main Django project settings
├── hospital/         # Hospital module app
├── idproofs/         # ID proof documents storage
├── patient/          # Patient module app
├── static/           # Static files (CSS, JS, images)
├── templates/        # HTML templates
├── db.sqlite3        # SQLite database
└── manage.py         # Django management script
