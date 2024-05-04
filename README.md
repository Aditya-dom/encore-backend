# Full fledged college fest website backend on django framework.
* Registration portal
* Login portal
* Campus ambassador portal
* Admin portal to manage data

## Setup Instructions
1 - Clone the Repository:
```
git clone https://github.com/Aditya-dom/encore-backend.git
```

2 - Install Dependencies:
```
cd encore-backend
pip install -r requirements.txt
```

3 - Database Setup:
 - Configure your database settings in settings.py.
 - Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```

4 - Create Superuser (for admin access):
```
python manage.py createsuperuser
```

5 - Run Development Server:
```
python manage.py runserver
```

Access the Website:
Visit `http://localhost:8000` in your web browser.

### Portals
1. Registration Portal
- Description: Allows students to register for various events and activities in the college fest.
- URL: /register

2. Login Portal
- Description: Registered users can log in to access their profiles, event registrations, and other personalized features.
- URL: /login

3. Campus Ambassador Portal
- Description: For campus ambassadors who promote the college fest within their campuses and manage registrations of participants.
- URL: /ambassador

4. Admin Portal
- Description: Administrators can manage all data related to the college fest, including events, registrations, and users.
- URL: /admin
- Access: Requires superuser credentials created during setup.

### Contributing
We welcome contributions from the community. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

License
This project is licensed under the [MIT License](/LICENSE).

#### feel free to Clone it and customize it with your templates and codes.
~~thank you!!~~
