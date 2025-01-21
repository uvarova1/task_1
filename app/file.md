1. venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. файл .env в корне проекта
DB_PORT=5432
DB_NAME=main_db
DB_HOST=db
DB_ALEMBIC_HOST=localhost
DB_USER=postgres
DB_PASSWORD=postgres

3. docker и docker compose
sudo apt update

sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

перезапустить Docker:
sudo systemctl restart docker

docker --version
docker-compose --version

docker-compose down

docker-compose up --build

Просмотр состояния Docker
systemctl status docker.service

Проверка конфигурации Docker
sudo nano /etc/docker/daemon.json

{
  "host": ["fd://"],
  "dns": ["8.8.8.8", "8.8.4.4"]
}

Проверка статуса контейнера docker.socket
systemctl status docker.socket

Если он не работает - запустить:
sudo systemctl start docker.socket

Удалить Docker:
sudo apt-get remove --purge docker-ce docker-ce-cli containerd.io

sudo apt-get autoremove
sudo apt-get clean

Заново установить
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

4. порт 80
sudo lsof -i :80
sudo kill -9 <PID>

sudo docker ps
sudo docker stop d0fdfc34904d

5. app/model
файл с именем модели (например, `book.py`)

6. app/schema
папка book
в ней файл book.py

7. app/db
файл postgres.py

8. app/api/папка crud_book

файл __init__.py
from . import crud

файл router.py
from fastapi import APIRouter
router = APIRouter()

файл
crud.py с основной логикой

9. app/api/ папка games - работа прометеуса, счётчика counter
файл __init__.py
from . import coin

файл router.py
from fastapi import APIRouter
router = APIRouter()

файл coin.py

10. app/api/ папка tech
файл __init__.py
from . import health, metrics

файл router.py
from fastapi import APIRouter
router = APIRouter()

файл health.py

файл metrics.py

11. app/
файл main.py

12. бд
sudo apt-get install postgresql-client
pip install asyncpg

psql -h localhost -U postgres -d main_db -p 5432
psql -h localhost -p 5432 -U postgres -d main_db

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE Post (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO Post (id, title, description)
VALUES
    (gen_random_uuid(), 'Post 1', 'Description for post 1'),
    (gen_random_uuid(), 'Post 2', 'Description for post 2'),
    (gen_random_uuid(), 'Post 3', 'Description for post 3'),
    (gen_random_uuid(), 'Post 4', 'Description for post 4'),
    (gen_random_uuid(), 'Post 5', 'Description for post 5');

SELECT * FROM Post;
DROP TABLE Book;

CREATE TABLE Book (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    date DATE NOT NULL
);

INSERT INTO Book (id, title, description, date)
VALUES
    (gen_random_uuid(), 'Book Title 1', 'Description 1', '2023-03-01'),
    (gen_random_uuid(), 'Book Title 2', 'Description 2', '2023-03-01');

13. alembic 
pip install alembic
alembic init -t async alembic

зайти в env.py в папке alembic и прописать ссылку к базе данных, а также импортировать все модели базы данных.

после строки from alembic import context

from app.model.meta import Base
from app.model.book import Book
from config.settings import settings

target_metadata = Base.metadata
config.set_main_option('sqlalchemy.url', settings.db_alembic_url)

alembic upgrade head
alembic revision --autogenerate -m "create_post_table"

файл alembic.ini
[post_write_hooks] посмотреть

14. ruff
pip install ruff
ruff check .
файл pyproject.toml в корне проекта



middleware для подсчета запросов

декоратор `@measure_latency` для измерения времени выполнения запроса

Создания собственного контейнера
`docker run -d --name your_name -p your_port:5432 -e POSTGRES_PASSWORD=your_password -e POSTGRES_USER=your_user -e POSTGRES_DB=your_db  postgres
`


http://localhost/docs
http://localhost/tech/metrics
http://localhost:9091/query

