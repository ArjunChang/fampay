# Fampay YT
### About Project
This is a webserver built for FamPay Assignment. The server runs a task every **2min** to fetch videos related to cats 
and stores it in the database. All the basic and bonus requirements have been met.

Built with Python (Django)

### Pre Requisites
1. Python
2. Docker
3. PostgreSQL

### Installation

1. Clone the repo
   ```sh
   $ git clone git@github.com:ArjunChang/fampay.git
   $ cd fampay
   ```
2. In `docker-compose.yml` file, set 
   ```sh
   DEFAULT_YOUTUBE_API_KEY=<your_api_key>
   ```
3. Setup Postgres DB
   ```shell
   $ sudo -u postgres createuser fampay
   $ sudo -u postgres createdb fampaydb
   $ sudo -u postgres psql
   postgres=: alter user fampay with encrypted password 'fampay123' ;
   postgres=: grant all privileges on database fampaydb to fampay ;
   postgres=: \q
   ```
4. Build the Docker Containers
   ```sh
   $ docker-compose build
   ```
5. Run Migrations
   ```sh
   $ docker-compose run django python manage.py migrate
   ```
6. Create a Super User to log into django admin
   ```sh
   $ docker-compose run django python manage.py createsuperuser
   ```
7. Start the Application
   ```sh
   $ docker-compose up
   ```
8. Login to django-admin and add multiple API Keys under YouTube Admin
9. The Web App is ready to go!


### Usage
1. `youtube/list` lists out all the database entries in a paginated manner
2. You can search for title/description in the `nav-bar` or append query parameter `?search=<your-search>`, this will 
   filter out entries that contains your search words
3. You can sort the entries based on Title, Channel or Published Time by clicking on the respective headers


### Contact
Arjun Chengappa [Linkedin](https://www.linkedin.com/in/arjun-chengappa-159b811a2/)

Email: `arjunchang25@gmail.com`
