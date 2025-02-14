# YouTube Blog Generator

## Overview
YouTube Blog Generator is a Django-based web application that automatically generates blog posts from YouTube video transcripts. It extracts video details, processes the transcript, and formats a blog post using AI-based content structuring.

https://github.com/user-attachments/assets/ef60343e-2552-4285-bd5a-c48eaa21ed84

## Features
- Extracts video title, description, and transcript from YouTube.
- Generates structured blog posts using AI.
- Stores blogs in a PostgreSQL database.
- User authentication and dashboard for managing blog posts.
- Simple and clean UI for editing and publishing posts.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: Django Templates, HTML, CSS, JavaScript
- **APIs Used**: YouTube Data API

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Virtualenv (optional but recommended)

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/youtube-blog-generator.git
   cd youtube-blog-generator
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure PostgreSQL:
   - Create a new PostgreSQL database.
   - Update `settings.py` with your database credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
5. Run migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```sh
   python manage.py runserver
   ```
8. Open the app in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
1. Log in to the admin panel at `/admin`.
2. Add your YouTube API key in the settings.
3. Submit a YouTube video URL to generate a blog post.
4. Edit and publish the generated blog.

## Environment Variables
Create a `.env` file in the project root and add:
```
YOUTUBE_API_KEY=your_youtube_api_key
SECRET_KEY=your_django_secret_key
DEBUG=True
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, feel free to contact [your email or GitHub profile].

