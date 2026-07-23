# Health Monitoring Portal (HMP)

An online healthcare system built with Django that digitizes paper medical records — giving Admins, Patients, Hospitals, and Doctors a single portal for secure, continuous access to patient history, surgeries, medicines, and treatments. It helps doctors provide faster, better-informed care across cities and reduces dependency on physical files.

## Modules

- **Admin** — manages hospitals, doctors, and platform-level oversight.
- **Patient** — maintains personal health records, ID proofs, and treatment history; accessible securely from anywhere.
- **Hospital** — manages hospital-level records, doctor assignments, and patient intake.
- **Doctor** — views patient history, prescribes treatments, and updates medical records during consultations.

## Key Features

- Centralized digital medical records — no more relying on paper files carried between hospitals.
- Secure access to patient history, past surgeries, medicines, and treatments.
- Continuity of care — a patient's records follow them across different hospitals and doctors.
- Certificate and ID proof storage for patient verification.

## Tech Stack

- **Backend:** Python / Django (`manage.py`, SQLite database)
- **Frontend:** HTML, CSS, JavaScript (Django templates)
- **Database:** SQLite (`db.sqlite3`)

## Project Structure

```
Health-Monitoring-Portal-HMP-/
├── hmp/            # Main Django project (settings, urls, wsgi/asgi)
├── doctor/         # Doctor module (app)
├── hospital/       # Hospital module (app)
├── patient/        # Patient module (app)
├── certificates/   # Stored certificates
├── idproofs/       # Stored ID proof documents
├── static/         # CSS, JS, images
├── templates/       # HTML templates
├── db.sqlite3       # SQLite database
└── manage.py         # Django management script
```

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
git clone https://github.com/yash-kathiriya/Health-Monitoring-Portal-HMP-.git
cd Health-Monitoring-Portal-HMP-
pip install -r requirements.txt   # if a requirements.txt is present
```

### Run migrations (if needed)

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start the development server

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

### Create an admin/superuser (optional)

```bash
python manage.py createsuperuser
```

## Usage

- **Patients** register and manage their own health records, ID proofs, and view treatment/surgery history.
- **Hospitals** onboard doctors and manage patient intake.
- **Doctors** access assigned patients' medical history and update treatments/prescriptions.
- **Admins** oversee hospitals, doctors, and overall platform data.

## License

No license specified yet — add one (e.g. MIT) if you plan to share or open-source this project.

## Contributing

Issues and pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.
