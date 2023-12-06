# kedarnath
    
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
    

## About

Kedarnath is the backbone for Attendify - a web application for managing attendance. It is built using Django and Django REST Framework.

## Features

- Attendance managemnt with Daily check-in and check-out
- Attendance reports
- Leave management
- User management
- User authentication with JWT tokens and session authentication (for browsable API)
- User roles and permissions
- User profile
- User activity log

## Future Features

- [ ] Advanced Admin Panel
- [ ] Project management with Kanban boards and ticketing system
- [ ] Integrations with Google Calendar, Google Drive, Google Meet, Zoom, Slack, etc.
- [ ] Advanced reporting
- [ ] Integration with biometric devices
- [ ] Integration with paytm and stripe and support for custom payment gateways.
- [ ] Payroll management with Payslips (for businesses)
- [ ] Support for multiple organizations
- [ ] Support for automated pipelines and CI/CD

## Setup

- Clone repository

```bash
git clone https://github.com/grvsh02/kedarnath
```

- Create virtual environment

```bash
python -m venv venv
```

- Activate virtual environment

```bash
source venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Run server

```bash
python manage.py runserver
```

- Create superuser

```bash
python manage.py createsuperuser
```

- Migrate database

```bash
python manage.py makemigrations
python manage.py migrate
```

## Contributing

- Fork this repository
- Clone your forked repository
- Create a branch
- Make your changes
- Commit and push
- Create a pull request
- Star this repository
- Wait for pull request to be merged
- Celebrate 🎉
- Repeat <br><br>
