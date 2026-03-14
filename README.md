# LuxStay : Hotel Management System

A Django-based hotel management system with modern dark UI.

## Features
- User authentication (Login / Register / Logout)
- Browse cities and hotels
- Hotel detail pages with image gallery (lightbox)
- Room listing with type, capacity, price
- Room booking with date picker & price calculator
- My Bookings page with cancel option
- Filter hotels by stars and price
- Django Admin panel
- Fully responsive design

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Load Sample Data (Cities, Hotels, Rooms, Users)
```bash
python seed_data.py
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Open in Browser
- **App**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## Login Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| User | user1 | user1234 |

## Project Structure
```
hotel_project/
├── hotel_project/          # Django settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── hotel_app/              # Main app
│   ├── models.py           # City, Hotel, Room, Booking
│   ├── views.py            # All views
│   ├── urls.py             # URL patterns
│   ├── admin.py            # Admin config
│   └── templates/
│       └── hotel_app/
│           ├── base.html       # Shared layout & nav
│           ├── login.html      # Login page
│           ├── register.html   # Register page
│           ├── home.html       # Homepage with hero
│           ├── cities.html     # City grid
│           ├── hotels_list.html # Hotels per city
│           ├── hotel_detail.html # Hotel + gallery + rooms
│           ├── book_room.html   # Booking form
│           └── my_bookings.html # User bookings
├── seed_data.py            # Sample data loader
├── manage.py
└── requirements.txt
```

## Pages
| URL | Page |
|-----|------|
| `/` | Homepage |
| `/login/` | Login |
| `/register/` | Register |
| `/cities/` | All Cities |
| `/hotels/city/<id>/` | Hotels in a City |
| `/hotel/<id>/` | Hotel Detail + Gallery |
| `/book/<room_id>/` | Book a Room |
| `/my-bookings/` | User's Bookings |
| `/admin/` | Admin Panel |
