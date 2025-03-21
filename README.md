# Yandex Form StudLab

**Стек:** Python 3.12, FastAPI, PostgreSQL, SQLAlchemy, JWT, Gunicorn/Uvicorn

## Как запустить проект:

- **Клонировать репозиторий и перейти в него в командной строке:**
    ```sh
    https://github.com/PinGBin74/Yandex_Form_StudLab.git


- **Установить poetry:**
  ```sh
  pip install poetry
  ```

- **Создать и активировать виртуальное окружение:**
    ```sh
    poetry install
    ```
- **Для работы с Docker:**
  - Запустить контейнер:
      ```bash
      docker-compose up -d
      ```
  - Создать PostgreSQL с настройками:

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
      YaStudLab@127.0.0.1
      ```
- **Применить миграции:**
  ```sh
  alembic upgrade head
  
- **Запустить проект:**
  ```sh
  uvicorn app.main:app --host 127.0.0.1 --port 8080 --reload


## Загрузка коллекции в Postman:

1. Запустите Postman;
2. В левом верхнем углу нажмите `File` -> `Import`;
3. Во всплывающем окне будет предложено перетащить в него файл с коллекцией либо выбрать файл через окно файлового менеджера.
Загрузите файл `StudLabYaForm.postman_collection.json` в Postman.

## Запуск коллекции:

1. После выполнения предыдущих шагов, в левой части окна Postman во вкладке `Collections` появилась импортированная коллекция.
Наведите на нее, нажмите на три точки напротив названия коллекции и в выпадающем списке выберите `Run collection`. В центре экрана появится список запросов коллекции,
а в правой части экрана - меню для настройки параметров запуска;
2. В правом меню включите фунцию `Persist responses for a session` - это даст возможность посмотреть ответы API после запуска коллекции;
3. Нажмите кнопку `Run <название коллекции>`;

