# Fampay YT
### About Project
This is a webserver built for FamPay Assignment. The server runs a task every **2min** to fetch videos related to cats and
stores it in the database. All the basic and bonus requirements have been met.

Built with Python (Django)

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:ArjunChang/fampay.git
   cd fampay
   ```
2. Create a Virtual Environment
   ```sh
   python3 -m venv fampay-venv
   ```
3. Install all packages
   ```sh
   pip install -r requirements.txt
   ```
4. Create superuser
   ```sh
   pyhton manage.py createsuperuser
   ```
5. Run the server
   ```sh
   python manage.py runserver
   ```
6. Login to Django Admin and add API Keys in `admin/youtube/youtubeapikey/`
7. Install and Start Redis: [Redis Installation and Setup Guide](https://redis.io/docs/getting-started/installation/)
8. Run Celery
   ```sh
   python -m celery -A fampay worker -l info
   ```
9. Visit `http://localhost:8000/youtube/list` and browse!

### Usage
1. `youtube/list` lists out all the database entries in a paginated manner
2. You can search for title in the `nav-bar` or append query parameter `?search=<your-search>`, this will filter out entries that contains your search words
3. You can sort the entries based on Title, Channel or Published Time by clicking on the respective headers


### Contact
Arjun Chengappa [Linkedin](https://www.linkedin.com/in/arjun-chengappa-159b811a2/)

Email: `arjunchang25@gmail.com`
