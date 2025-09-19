📘 EROOMS - Your Room, Your Choice
EROOMS is a fully functional Django-based web application for listing and browsing rental rooms with key details like address, host info, and user reviews. The platform features dark mode, profile picture support, search functionality, and smooth navigation for a better user experience.

📌 Table of Contents
Features

Tech Stack

Screenshots

Project Structure

Getting Started

Available URLs

Models Overview

Contributing

License

Acknowledgments

🚀 Features
🔒 User Authentication: Register, Login, Logout

👤 Profile Management: Edit profile with image

🏡 Room Listings: Browse all available rooms

🔍 Search Bar: Search by title or address

🌓 Dark Mode Toggle: Smooth UI toggle with local storage

🗺️ Listing Page: Address, photos, and review details

⭐ Rating System: User reviews with star ratings

📱 Responsive Design: Looks good on mobile and desktop

🧭 Pagination: Better experience for large listing datasets

🧰 Tech Stack
Layer	Technology
Language	Python 3.9+
Framework	Django 4.x
Database	SQLite3 (default)
Frontend	HTML5, CSS3
Templating	Django Templates
Static Files	Custom CSS & SVG
Hosting	(Your deployment provider here if any)

📷 Screenshots
Add screenshots here, for example:

Home Page with Listings

Listing Details with Reviews

User Profile with Picture

Dark Mode UI

🏗️ Project Structure
bash
Copy
Edit
airbnb_proj/
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
└── .venv/                      # Virtual environment
⚙️ Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/erooms.git
cd erooms
2. Create Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Run Migrations
bash
Copy
Edit
python manage.py migrate
5. Create Superuser (Admin)
bash
Copy
Edit
python manage.py createsuperuser
6. Start the Server
bash
Copy
Edit
python manage.py runserver
Visit: http://127.0.0.1:8000/

🔗 Available URLs
Path	Purpose
/	Home page (Listings)
/login/	Login user
/register/	Register new user
/profile/<id>/	View user profile
/editprofile/	Edit profile
/logout/	Logout user
/listing/<id>/	Detailed listing page

🧬 Models Overview
User (from Django's auth.User)

Profile (authy.models.Profile):

user (OneToOne)

image

bio / details (if extended)

Listing (post.models.Listing):

title, address, photos, owner

Photo (post.models.Photo):

ForeignKey to Listing

Review (post.models.Review):

rating, comment, ForeignKey to Listing and User

🤝 Contributing
Pull requests are welcome! Please follow these steps:

Fork the repo

Create a new branch (git checkout -b feature-name)

Commit changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature-name)

Open a Pull Request

📄 License
This project is licensed under the MIT License.

🙏 Acknowledgments
Django Documentation

All contributors and testers

Bootstrap inspirations (if used)

Figma or design assets (if relevant)

