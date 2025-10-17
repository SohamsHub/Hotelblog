### Erooms
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

EROOMS is a fully functional Django-based web application for listing and browsing rental rooms with key details like address, host info, and user reviews. The platform features dark mode, profile picture support, search functionality, and smooth navigation for a better user experience.

## Key features

- Listings: title, description, price/night, address, location, amenities, photos
- Listing details page: photo gallery, basic info, reviews
- Search: by title or address (case-insensitive)
- Reviews (1–5 rating), reservations model scaffold
- Authentication: register, login, logout
- Profiles: view and edit profile, upload profile image
- Pagination on the home page
- Dark mode toggle
- Media file serving in development (/media/)

## Tech stack

- Python 3.11+ (recommended)
- Django 5.x
- django-extensions
- django-browser-reload (optional, improves dev UX)
- SQLite (development default)

The main apps live in:
- post/ — listings, photos, reservations, reviews, home and detail views
- authy/ — user profiles, auth views (login/register/logout, edit profile)
- theme/ — Tailwind integration and static build tooling

## Project structure (abridged)

- blog_app_1/settings.py — settings (MEDIA and Tailwind configured)
- blog_app_1/urls.py — routes include post and authy, media served in dev
- post/models.py — Amenity, Listing, ListingPhoto (UUID), Reservation, Review
- post/views.py — home (search + pagination), listing detail
- authy/models.py — Profile (OneToOne with User), image upload path
- authy/views.py — login, register, logout, profile view/edit
- templates/ — HTML templates for post/authy pages
- media/ — user/media uploads (sample data included)
- theme/static_src/ — Tailwind CLI build config (package.json, postcss, tailwind.config)

## Prerequisites

- Python 3.11+ (3.12 works fine)
- pip
- Node.js 18+ (only if you want Tailwind live build)

## Quick start (development)

## 1) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## 2) Install Python dependencies

```bash
pip install -r requirements.txt
```


## 3) Apply database migrations

```bash
python manage.py migrate
```

## 4) (Optional) Create a superuser to access Django admin

```bash
python manage.py createsuperuser
```

## 5) Run the development server

```bash
python manage.py runserver
```

The app will be available at http://127.0.0.1:8000/

- Home: / (listings with pagination, search by title/address)
- Listing details: /rooms/<id>
- Auth: /login, /register, /logout
- Profiles: /profiles/<id>, /edit-profile/
- Admin: /admin/ (if you created a superuser)

Media files are served from /media/ in development.

Note: The main templates under templates/post/ mostly use custom CSS. Tailwind is available if you choose to build styles or extend the theme/templates/base.html.

## Database and media

- Default DB: SQLite (db.sqlite3). Suitable for local development.
- Media uploads are stored under media/ with structured paths for listings and profiles.
- In production, configure a proper database and media/static hosting. Do not use the committed SECRET_KEY in production.

## Running tests

```bash
python manage.py test
```

## Git: clone and fork workflows

You can either clone the original repository or fork it and work on your copy.

### Clone (read-only contribution path)

HTTPS:

```bash
git clone https://github.com/SohamsHub/Hotelblog.git
cd Hotelblog
```

SSH:

```bash
git clone git@github.com:SohamsHub/Hotelblog.git
cd Hotelblog
```

### Fork (recommended for contributing)

1) On GitHub, click “Fork” on https://github.com/SohamsHub/Hotelblog to create your fork under your account.
2) Clone your fork locally.

HTTPS:

```bash
git clone https://github.com/SohamsHub/Hotelblog.git
cd Hotelblog
```

SSH:

```bash
git clone git@github.com:SohamsHub/Hotelblog.git
cd Hotelblog
```
