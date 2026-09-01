# 📰 New Portal – News Management System

A web-based **News Portal Management System** developed using **Python and Django**. The application provides a structured platform for managing news content, user accounts, media files, reports, and APIs through a centralized web application.

## 📌 Project Overview

**New Portal** is a Django-based web application designed to simplify the process of creating, managing, and displaying news content.

The project follows a modular structure with dedicated Django applications for user/account management, news management, API functionality, and reporting. It also includes an administrative interface for managing application data efficiently.

## ✨ Features

* 📰 **News Management**

  * Create and manage news articles
  * Organize and display news content
  * Support for media/images associated with news

* 👤 **User & Account Management**

  * User account functionality
  * Authentication-related components
  * Structured account management

* 🔌 **REST API**

  * API endpoints for application data
  * Built using Django REST Framework
  * Supports integration with external clients or services

* 📝 **Rich Text Editor**

  * Integrated Django Summernote
  * Rich-text editing for news and other content

* 🛠️ **Admin Dashboard**

  * Enhanced Django administration interface
  * Integrated Jazzmin for a modern admin experience
  * Simplified management of application data

* 🖼️ **Media Management**

  * Image and media file handling
  * Pillow integration for image processing

* 📊 **Reporting**

  * Dedicated reporting module
  * Structured application reporting functionality

## 🧰 Technologies Used

| Technology                       | Purpose                         |
| -------------------------------- | ------------------------------- |
| **Python**                       | Core programming language       |
| **Django 5.2.3**                 | Web application framework       |
| **Django REST Framework 3.16.1** | REST API development            |
| **SQLite**                       | Database                        |
| **HTML/CSS**                     | Frontend structure and styling  |
| **JavaScript**                   | Client-side functionality       |
| **Pillow 11.2.1**                | Image processing                |
| **Django Summernote**            | Rich-text content editing       |
| **Jazzmin 3.0.1**                | Enhanced Django admin interface |

## 📂 Project Structure

```text
New-portal/
│
├── accounts/              # User and account management
│
├── api/                   # REST API functionality
│
├── media/                 # Uploaded media and images
│
├── newspaper/             # Main newspaper/news application
│
├── report/                # Reporting functionality
│
├── static/                # Static files
│
├── templates/             # HTML templates
│
├── NEWS/                  # Project configuration
│
├── db.sqlite3             # SQLite database
│
├── manage.py              # Django project management script
│
├── requiremnet.txt        # Python dependencies
│
└── README.md              # Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rahulrajyada/New-portal.git
```

Navigate to the project directory:

```bash
cd New-portal
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requiremnet.txt
```

The project currently specifies Django, Jazzmin, Pillow, Django Summernote, and Django REST Framework in its dependency file.

### 4. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin User

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your administrator account.

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application should then be available at:

```text
http://127.0.0.1:8000/
```

## 🔐 Admin Panel

After starting the server, access the Django administration panel through:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials created during setup.

The project uses **Jazzmin** to provide an enhanced administration interface.

## 🔌 API

The project includes an API application built using **Django REST Framework**.

API functionality can be accessed through the routes configured within the `api` application.

For developers extending the project, the API can be used to provide structured access to application data and integrate the portal with other applications or frontend clients.

## 🖼️ Media & Rich Content

The application includes support for uploaded media using Django's media configuration and **Pillow** for image processing.

**Django Summernote** is also integrated to provide rich-text editing capabilities for content creation.

## 🎯 Learning Outcomes

Through this project, the following skills were developed:

* Python programming
* Django web development
* Django project and application architecture
* Database integration using SQLite
* REST API development
* User/account management
* HTML/CSS-based web development
* Media and image handling
* Django administration
* Rich-text content management
* Working with third-party Django packages

## 🚀 Future Improvements

Possible future improvements include:

* [ ] Add advanced news search and filtering
* [ ] Add news categories and tags
* [ ] Implement user roles and permissions
* [ ] Add pagination for news articles
* [ ] Improve frontend responsiveness
* [ ] Add email notifications
* [ ] Add API authentication
* [ ] Deploy the application to a cloud platform
* [ ] Add automated testing
* [ ] Improve security and production configuration

## 👨‍💻 Developer

**Rahul Raj Yadav**

GitHub:
https://github.com/rahulrajyada

## 📄 License

This project is intended for educational and development purposes.

---

⭐ If you find this project useful, consider giving the repository a star!
