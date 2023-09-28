<h1 align="center">CogniVerse by EvoQ</h1>

<h4 align="center">Simple and Powerful Email Marketing Platform.</h4>

<p align="center">
  <a href="https://github.com/tigran-saatchyan/CogniVerse_by_EvoQ/blob/master/LICENSE"><img src="https://img.shields.io/github/license/tigran-saatchyan/mailcraft-by-evoq" alt="License"></a>
  <a href="https://t.me/PythonistiC"><img src="https://img.shields.io/badge/telegram-@PythonistiC-blue.svg?logo=telegram" alt="Telegram"></a>
  <a href="https://www.paypal.me/TigranSaatchyan"><img src="https://img.shields.io/badge/support-paypal-blue.svg?logo=paypal" alt="Support me on Paypal"></a>
</p>



<p align="center">
  <img src="static/readme/img.png" alt="screenshot">
</p>



## Table of Contents

* [Background / Overview](#background--overview)
* [Features](#features)
* [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Setting up](#setting-up)
  * [Structure / Scaffolding](#structure--scaffolding)
* [Documentation](#documentation)
* [Browser Support](#browser-support)
* [Dependencies](#dependencies)
* [Todo](#todo)
* [Release History](#release-history)
* [Changelog](#changelog)
* [Issues](#issues)
* [Bugs](#bugs)
* [Translations](#translations)
* [Authors](#authors)
* [Acknowledgments](#acknowledgments)
* [Support](#support)
* [License](#license)

## Background / Overview

CogniVerse by EvoQ is an innovative online learning platform that 
provides access to a wide range of courses across various subjects. 
Our educational materials are created by experts in their fields, 
and interactive features and carefully crafted assignments 
will help you learn most effectively.

## Features

Here are some API features of CogniVerse LMS:

1. **User Management API:**
   - Create, update, and delete user profiles.
   - Authenticate users securely.
   - Retrieve user details and enrollment information.

2. **Course Management API:**
   - List available courses and their details.
   - Enroll and unenroll users in courses.
   - Retrieve course progress and completion status.

3. **Content Access API:**
   - Access course materials, such as videos, documents, and quizzes.
   - Track content consumption and completion.

4. **Progress Tracking API:**
   - Monitor user progress within courses.
   - Retrieve quiz scores and assignment submissions.

5. **Notifications API:**
   - Send notifications and updates to users.
   - Allow users to customize notification preferences.

6. **Payment Integration API:**
   - Enable payment processing for course enrollment.
   - Manage billing information and subscription status.

7. **Analytics and Reporting API:**
   - Gather data on user engagement and course performance.
   - Generate reports on user activity and course effectiveness.

8. **Integration with External Tools/APIs:**
   - Allow integration with third-party tools like video conferencing platforms, chat systems, or analytics services.

9. **Security and Authentication API:**
   - Implement robust security measures, including role-based access control.
   - Authenticate and authorize API requests securely.

10. **Feedback and Review API:**
    - Collect and display user reviews and ratings for courses.
    - Enable feedback submission and analysis.

These API features would enhance the functionality of CogniVerse LMS, making it a comprehensive and versatile e-learning platform.

## Prerequisites

You will need the following installed on your computer.

* [Git](https://git-scm.com/)
* [Python Poetry](https://python-poetry.org/)

### Installation

Open your terminal and type in

```sh
$ git clone https://github.com/tigran-saatchyan/CogniVerse_by_EvoQ.git
$ cd CogniVerse_by_EvoQ
```

Install all the packages

```sh
$ poetry install
```

### Setting up

Run all migrations
```sh
$ python manage.py migrate
```

Load country list for users
```sh
$ python manage.py load_countries
```



### Structure / Scaffolding

<details>

<summary>Project Structure</summary>

```text
mailcraft-by-evoq
├── blog
│  ├── __init__.py
│  ├── admin.py
│  ├── apps.py
│  ├── forms.py
│  ├── migrations
│  │  ├── 0001_initial.py
│  │  ├── 0002_initial.py
│  │  └── __init__.py
│  ├── models.py
│  ├── templates
│  │  └── blog
│  │     ├── includes
│  │     │  ├── inc_full_post_card.html
│  │     │  ├── inc_paginator_old_new.html
│  │     │  ├── inc_paginator_pages.html
│  │     │  ├── inc_post_card.html
│  │     │  └── inc_post_head_section.html
│  │     ├── posts_confirm_delete.html
│  │     ├── posts_detail.html
│  │     ├── posts_form.html
│  │     └── posts_list.html
│  ├── tests.py
│  ├── urls.py
│  └── views.py
├── config
│  ├── __init__.py
│  ├── asgi.py
│  ├── settings.py
│  ├── urls.py
│  └── wsgi.py
├── contacts
│  ├── __init__.py
│  ├── admin.py
│  ├── apps.py
│  ├── forms.py
│  ├── migrations
│  │  ├── 0001_initial.py
│  │  ├── 0002_initial.py
│  │  └── __init__.py
│  ├── models.py
│  ├── templates
│  │  └── contacts
│  │     ├── contact
│  │     │  ├── contact_confirm_delete.html
│  │     │  ├── contact_detail.html
│  │     │  ├── contact_form.html
│  │     │  ├── contact_list.html
│  │     │  └── includes
│  │     │     ├── inc_contact_card.html
│  │     │     ├── inc_contact_card_test_modal.html
│  │     │     └── inc_contact_head_section.html
│  │     └── list
│  │        ├── includes
│  │        │  ├── inc_lists_card.html
│  │        │  ├── inc_lists_card_test_modal.html
│  │        │  └── inc_lists_head_section.html
│  │        ├── lists_confirm_delete.html
│  │        ├── lists_detail.html
│  │        ├── lists_form.html
│  │        └── lists_list.html
│  ├── tests.py
│  ├── urls.py
│  └── views.py
├── frontend
│  ├── __init__.py
│  ├── admin.py
│  ├── apps.py
│  ├── forms.py
│  ├── migrations
│  │  └── __init__.py
│  ├── models.py
│  ├── templates
│  │  └── frontend
│  │     ├── base.html
│  │     ├── includes
│  │     │  ├── inc_footer.html
│  │     │  ├── inc_header.html
│  │     │  ├── inc_index_head_section.html
│  │     │  └── inc_menu.html
│  │     └── index.html
│  ├── templatetags
│  │  ├── __init__.py
│  │  └── my_tags.py
│  ├── tests.py
│  ├── urls.py
│  └── views.py
├── LICENSE
├── logs
│  ├── __init__.py
│  ├── admin.py
│  ├── apps.py
│  ├── migrations
│  │  ├── 0001_initial.py
│  │  ├── 0002_initial.py
│  │  └── __init__.py
│  ├── models.py
│  ├── templates
│  │  └── logs
│  │     ├── includes
│  │     │  └── inc_mailings_head_section.html
│  │     ├── logs_confirm_delete.html
│  │     └── logs_detail.html
│  ├── tests.py
│  ├── urls.py
│  └── views.py
├── mailing
│  ├── __init__.py
│  ├── admin.py
│  ├── apps.py
│  ├── cron.py
│  ├── forms.py
│  ├── management
│  │  ├── __init__.py
│  │  └── commands
│  │     ├── __init__.py
│  │     └── send_mail.py
│  ├── migrations
│  │  ├── 0001_initial.py
│  │  ├── 0002_initial.py
│  │  └── __init__.py
│  ├── models.py
│  ├── service.py
│  ├── templates
│  │  └── mailing
│  │     ├── includes
│  │     │  ├── inc_mailing_card.html
│  │     │  ├── inc_mailing_card_test_modal.html
│  │     │  └── inc_mailings_head_section.html
│  │     ├── mailing_confirm_delete.html
│  │     ├── mailing_detail.html
│  │     ├── mailing_form.html
│  │     └── mailing_list.html
│  ├── tests.py
│  ├── urls.py
│  └── views.py
├── manage.py
├── media
│  └── blog
│     └── posts
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
├── service
│  ├── __init__.py
│  └── utils.py
├── static
│  ├── blog
│  ├── mailing
│  ├── readme
│  └── users
│     └── data
│        └── countries.json
└── users
   ├── __init__.py
   ├── admin.py
   ├── apps.py
   ├── forms.py
   ├── management
   │  ├── __init__.py
   │  └── commands
   │     ├── __init__.py
   │     ├── create_su.py
   │     └── load_countries.py
   ├── migrations
   │  ├── 0001_initial.py
   │  └── __init__.py
   ├── models.py
   ├── templates
   │  └── users
   │     ├── includes
   │     │  ├── inc_user_card.html
   │     │  └── inv_login_style.html
   │     ├── registration
   │     │  ├── email_verified.html
   │     │  ├── login.html
   │     │  ├── logout.html
   │     │  ├── password_change_done.html
   │     │  ├── password_change_form.html
   │     │  ├── password_reset_complete.html
   │     │  ├── password_reset_confirm.html
   │     │  ├── password_reset_done.html
   │     │  ├── password_reset_email.html
   │     │  ├── password_reset_form.html
   │     │  ├── register.html
   │     │  └── verification_email.html
   │     ├── user_form.html
   │     └── user_list.html
   ├── tests.py
   ├── urls.py
   └── views.py
   
    Lines of code: 5237
    Size: 164.73 KiB (117 files)
```

</details>


<strong>Note:</strong> The scaffolding was generated with tree.

## Documentation

  * Create SuperUser
```sh
$ python manage.py create_su
```



The rest will be available Soon...

## Browser Support

|  Chrome  |  IE  |   Edge   |  Safari  | Firefox  |
| :------: | :--: | :------: | :------: | :------: |
| Latest 2 |  9+  | Latest 2 | Latest 2 | Latest 2 |

## Dependencies

List of dependencies used in the project

* ![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2Fmailcraft-by-evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.python&style=flat&label=Python)
* ![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2Fmailcraft-by-evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.Django&style=flat&label=Django)
* ![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2Fmailcraft-by-evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.Pillow&style=flat&label=Pillow)
* ![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2Fmailcraft-by-evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.pytils&style=flat&label=pytils)
* ![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2Fmailcraft-by-evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.psycopg&style=flat&label=psycopg)
* ![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2Fmailcraft-by-evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.dependencies.redis&style=flat&label=Redis)


## Todo

List of things to fix or add

- [x] Improve README.md

## Release History
Actual version: ![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftigran-saatchyan%2Fmailcraft-by-evoq%2Fdevelop%2Fpyproject.toml&query=%24.tool.poetry.version&style=flat&label=Version)

[//]: # (* 0.1.0 - Initial release)

[//]: # (  * Added dependencies compilation)

[//]: # (  * Added readme)
  

## Changelog

Detailed changes for each release will be documented in the 
[release notes](https://github.com/users/tigran-saatchyan/projects/10/views/2).

## Issues 

![GitHub issues](https://img.shields.io/github/issues/tigran-saatchyan/CogniVerse_by_EvoQ)
![GitHub closed issues](https://img.shields.io/github/issues-closed/tigran-saatchyan/CogniVerse_by_EvoQ)

Please make sure to read the [Issue Reporting Checklist](https://github.com/tigran-saatchyan/CogniVerse_by_EvoQ/issues?q=is%3Aopen) before opening an issue. Issues not conforming to the guidelines may be closed immediately.

## Bugs

If you have questions, feature requests or a bug you want to report, please click [here](https://github.com/tigran-saatchyan/mailcraft-by-evoq/issues) to file an issue.

[//]: # (## Deployment)

[//]: # ()
[//]: # (Add additional notes about how to deploy this on a live system)

## Translations

* :ru: Russian/Русский

## Authors

* [**Tigran Saatchyan**](https://github.com/tigran-saatchyan) - CogniVerse

See also the list of [contributors](#acknowledgments) who participated in this project.

## Acknowledgments
This project would now have been possible without the help and advice from many contributors.

## Contact Us:

  * Discord: ![Discord](https://img.shields.io/discord/1152575327810363482) 
  * Telegram: 

## Support

Like what you see? Keep me awake at night by buying me a coffee or two.

<a href="https://www.buymeacoffee.com/saatchyan" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Book" style="height: 60px !important;width: 217px !important;" ></a>

## License
Copyright (c) 2023 Tigran Saatchyan.

Usage is provided under the MIT License. See [LICENSE](https://github.com/tigran-saatchyan/CogniVerse_by_EvoQ/blob/master/LICENSE) for the full details.
