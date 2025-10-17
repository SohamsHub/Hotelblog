# 📘 EROOMS - Your Room, Your Choice

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*EROOOMS* is a fully functional Django-based web application for listing and browsing rental rooms with key details like address, host info, and user reviews. The platform features dark mode, profile picture support, search functionality, and smooth navigation for an enhanced user experience.

---

## 📌 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Screenshots & Demo](#-screenshots--demo)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Available URLs](#-available-urls)
- [Models Overview](#-models-overview)
- [Git Workflow](#-git-workflow)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🚀 Features
- 🔒 *User Authentication*: Register, Login, Logout  
- 👤 *Profile Management*: Edit profile with image upload  
- 🏡 *Room Listings*: Browse all available rooms  
- 🔍 *Search Bar*: Search listings by title or address  
- 🌓 *Dark Mode Toggle*: Smooth UI toggle with local storage  
- 🗺️ *Listing Page*: Address, photos, and review details  
- ⭐ *Rating System*: User reviews with star ratings  
- 📱 *Responsive Design*: Mobile and desktop friendly  
- 🧭 *Pagination*: Improved experience for large datasets  

---

## 🧰 Tech Stack

| Layer       | Technology |
|------------|------------|
| Language    | Python 3.12+ |
| Framework   | Django 4.x |
| Database    | SQLite3 (default) |
| Frontend    | HTML5, CSS3 |
| Templating  | Django Templates |
| Static Files| Custom CSS & SVG |
---


## 🏗️ Project Structure
```bash
erooms/
├── blogapp/
│   ├── authy/                  # Authentication app
│   ├── post/                   # Main app for listings
│   ├── media/                  # Uploaded images
│   ├── templates/
│   │   ├── authy/              # login.html, register.html, profile.html
│   │   └── post/               # home.html, listing_room.html
│   └── blog_app_1/             # Main settings & urls
├── db.sqlite3                  # Default database
├── manage.py                   # Django management CLI
├── requirements.txt            # Python dependencies
