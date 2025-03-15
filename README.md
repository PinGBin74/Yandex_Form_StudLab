# Yandex Form StudLab

**Стек:** Python 3.12, FastAPI, PostgreSQL, SQLAlchemy, JWT, Gunicorn

## Как запустить проект:

- **Клонировать репозиторий и перейти в него в командной строке:**
    ```sh
    https://github.com/PinGBin74/Yandex_Form_StudLab.git

- **Создать и активировать виртуальное окружение:**
    ```sh
    poetry init

    poetry install

- **Для работы с Docker:**
  - Создать контейнер PostgreSQL с настройками:
    - **Port:** `5432`
    - **User:** 
      ```sh
      postgres
      ```
    - **Password:**
      ```sh
      password
      ```
    - **Database Name:** 
      ```sh
      YaStudLab
      ```
  - Запустить контейнер:
    ```bash
    docker-compose up -d
    ```
