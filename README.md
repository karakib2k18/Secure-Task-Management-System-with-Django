# Secure-Task-Management-System-with-Django
# Task Management System

## Overview
This is a task management web application built with Django. Users can create, view, and manage tasks. Each task belongs to a predefined category, which is managed by the admin.

## Features
- Task creation and management
- Categories managed by the admin
- CSRF protection and secure forms
- Custom 404 and 500 error pages
- Bootstrap-based UI

## Setup Instructions

### Prerequisites
- Python 3.7
- Django 5

### Installation
1. Clone the repository:
   git clone <repository_url>
   cd task_manager


# Install dependencies: 
pip3 install -r requirements.txt

# Apply migrations:
python3 manage.py migrate


# Create a superuser:
python3 manage.py createsuperuser


# Run the development server:
python3 manage.py runserver
