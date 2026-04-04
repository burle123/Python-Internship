# PRODUCT REQUIREMENT DOCUMENT (PRD) – MVP VERSION

## 1. Project Overview

### Project Title:
Django MVP Boilerplate with Authentication and Responsive Dashboard

### Tech Stack (MVP Scope Only)

Backend:
- Django (Python framework)
- Django Built-in Authentication System
- Django ORM

Frontend:
- Django Template Engine
- HTML5
- TailwindCSS (CDN for simplicity)
- Vanilla JavaScript

Database:
- SQLite (Development Only)

⚠️ Note: This is strictly an MVP for development purposes. No production configuration, no deployment planning, and no advanced infrastructure setup is included.

---

## 2. Problem Statement

Create a reusable Django MVP boilerplate that includes:

- Sign Up
- Sign In
- Forgot Password
- Reset Password
- Mandatory Terms & Conditions acceptance

Authentication must be required to access the dashboard.

The dashboard must:
- Avoid excessive whitespace
- Display useful information (stats, activity, alerts)
- Include a notification icon in header
- Include collapsible sidebar
- Be mobile-friendly
- Support Dark and Light mode
- Default to System theme preference

This MVP will act as a starting template for future development projects.

---

## 3. MVP Goals

1. Implement complete authentication flow using Django built-ins.
2. Protect dashboard using login_required.
3. Build a responsive dashboard layout.
4. Implement theme toggle (Dark/Light/System).
5. Use SQLite as the only database.
6. Keep structure clean and simple.

---

## 4. Functional Requirements (MVP Scope)

### 4.1 Authentication Module

#### A. Sign Up
Fields:
- Full Name
- Email (Unique)
- Password
- Confirm Password
- Terms & Conditions Checkbox (Required)

Validation Rules:
- Email must be unique
- Passwords must match
- Terms must be accepted

System Behavior:
- Store terms_accepted (Boolean)
- Store terms_accepted_at (DateTime)
- Automatically login after successful registration

---

#### B. Sign In
Fields:
- Email
- Password

Behavior:
- Authenticate using Django auth
- Redirect to dashboard
- Show error messages if invalid

---

#### C. Forgot Password
- User enters email
- Use Django’s built-in password reset views
- Send reset link (console email backend for development)

---

#### D. Reset Password
- Token-based reset link
- Allow new password entry

---

#### E. Terms & Conditions
- Public page
- Checkbox mandatory during registration
- If unchecked → prevent submission

---

### 4.2 Access Control

- Use @login_required decorator for dashboard
- Redirect unauthenticated users to login page
- Prevent manual URL access

---

### 4.3 Dashboard Requirements (UI MVP)

### Layout Structure

Header:
- Logo / Project Name
- Notification icon (static count for MVP)
- Profile dropdown
- Theme toggle button

Sidebar:
- Collapsible
- Icons + labels
- Active page highlight
- Collapses automatically on mobile

Main Content:
- 4 Stats Cards (e.g., Users, Activity, Alerts, Messages)
- Recent Activity section
- Notifications preview section
- Quick Links panel

Whitespace Handling:
- Use Tailwind grid (grid-cols-1 md:grid-cols-2 lg:grid-cols-4)
- Maintain balanced spacing
- Avoid large empty containers

---

### 4.4 Theme Mode (Dark / Light / System)

Requirements:
- Detect system preference using prefers-color-scheme
- Default to system preference
- Allow manual toggle
- Store preference in localStorage
- Use Tailwind dark mode via class strategy

---

### 4.5 Mobile Responsiveness

- Mobile-first layout
- Sidebar hidden by default on small screens
- Toggle button to open sidebar
- Responsive grid for dashboard cards

---

## 5. Non-Functional Requirements (MVP Limited)

Security (Basic Dev-Level):
- CSRF protection enabled (default Django)
- Password hashing (default Django)

Performance:
- Minimal JS
- Tailwind via CDN (for development simplicity)

No production hardening included.

---

## 6. Simplified Project Structure (MVP)

project_root/
│
├── config/
├── accounts/
├── dashboard/
├── templates/
│   ├── base.html
│   ├── auth/
│   ├── dashboard/
├── static/
│   ├── js/
└── manage.py

---

# STANDARD OPERATING PROCEDURE (SOP) – MVP

---

## Phase 1: Setup

Step 1: Create Virtual Environment
- python -m venv venv
- Activate environment

Step 2: Install Django
- pip install django

Step 3: Create Project and Apps
- django-admin startproject config .
- python manage.py startapp accounts
- python manage.py startapp dashboard

---

## Phase 2: Database Setup

- Use default SQLite database
- Run:
  python manage.py makemigrations
  python manage.py migrate

No PostgreSQL. No production DB.

---

## Phase 3: Authentication Implementation

Step 1: Create Custom User Model (Optional but Recommended)
- Extend AbstractUser
- Add:
  - terms_accepted
  - terms_accepted_at

Step 2: Create Forms
- RegistrationForm
- LoginForm

Step 3: Use Django Built-in Password Reset Views
- Configure console email backend:

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

Step 4: Protect Dashboard
- Add @login_required decorator

---

## Phase 4: Frontend Implementation

Step 1: Integrate Tailwind via CDN
- Add CDN link in base.html

Step 2: Create Base Layout
- Header
- Sidebar
- Main content block

Step 3: Implement Sidebar Toggle (JavaScript)
- Toggle CSS classes
- Hide/show sidebar

Step 4: Implement Theme Toggle
- Detect system theme
- Add/remove 'dark' class
- Save selection in localStorage

---

## Phase 5: Dashboard UI Completion

- Add 4–6 stat cards
- Add activity section
- Add notification preview
- Ensure minimal whitespace
- Verify responsiveness on mobile view

---

## MVP Checklist

✔ Sign Up works
✔ Terms checkbox mandatory
✔ Login works
✔ Forgot/Reset password works (console email)
✔ Dashboard protected
✔ Sidebar collapsible
✔ Dark/Light/System theme works
✔ Mobile responsive layout
✔ No excessive whitespace
✔ SQLite database functioning

---

# Final MVP Outcome

You will have a development-ready Django boilerplate that includes:

- Complete authentication flow
- Terms & Conditions enforcement
- Protected dashboard
- Responsive UI
- Collapsible sidebar
- Notification header icon
- Dark / Light / System theme
- SQLite database
- No deployment or production configuration

This MVP serves as a clean foundation for further feature expansion.

