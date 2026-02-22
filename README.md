# Vehicle Rental System - Django REST Framework Project

## Project Description
A simple vehicle rental system built with Django REST Framework (DRF) that allows users to view vehicles, book them, and manage bookings.

---
# folder structure 
vehiclesystem/        ← local repo root (outer folder)
├── venv/             ← virtual environment folder
└── vehicle_system/   ← Django project folder (contains manage.py, apps, settings, etc.)
    ├── settings.py
    ├── urls.py
    └── ...
Repo root (GitHub): vehicle_system/  ← contains manage.py, apps, settings, etc.
Local venv (optional) created at outer folder: vehiclesystem/venv/

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/vehicle_system.git

cd vehiclesystem/

python -m venv env

venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

create .env file
copy .env.example to .env

cd vehicle_system

migrations
python manage.py makemigrations
python manage.py migrate

to run project
python manage.py runserver

Testing API use Postman
For endpoints requiring authentication, create a user via /admin or signup endpoint.

API endpoints
vehicle
 GET    api/vehicles/
 POST   api/vehicles/createvehicle/
 GET    api/vehicles/vehicledetail/
 PUT    api/vehicles/updatevehicle/<id>/
 DELETE api/vehicles/deletevehicle/<id>/

booking
GET api/bookings/
POST api/bookings/createbooking/
GET api/bookings/<id>/

user
POST  api/usersignup/
POST  api/userlogin/

filtering
api/vehicles/?brand =
api/vehicles/?fuel_type =
api/vehicles/?is_available =

Sample JSON for Booking
{
   "id": 1,
   "customer_name": "Tony",
   "customer_phone": "1234567892",
   "start_date": "2026-02-28",
   "end_date": "2026-03-04",
}

API Testing video link
https://drive.google.com/file/d/1Ha62S_Gl0V01UOMHsPisp1oc5Tq00-K3/view?usp=drive_link


Live API
https://vehicle-system-sclu.onrender.com

GET https://vehicle-system-sclu.onrender.com/api/vehicles/








