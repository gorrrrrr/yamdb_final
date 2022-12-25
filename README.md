# api_yamdb - infrastructure

## Проект
Это заготовка для сайта, который собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
Произведению может быть присвоен Genre из списка предустановленных. Пользователи оставляют к произведениям Review и ставят произведению оценки (от 1 до 10), из которых формируется рейтинг.
Проект обладает своей документированной API.


## API
\api_yamdb\static\redoc.yaml - здесь документирована API. Удобно просматривать в браузере [тут](http://127.0.0.1:8000/redoc/) (работает, если проект равернут локально).


## Как запустить проект:

Для запуска контейнера вам требуется установленный и запущенный Docker.

* Клонировать репозиторий

В репозитории уже сформирована инфраструктура для запуска контейнера с проектом.

Если вы работает на UNIX подобной сиситеме, просто запустите в корневой папке проекта файл Makefile.

```bash
make
```

В ином случае, сделайте то же руками:

* Из папки INFRA_SP2/infra запустите bash команду:
```bash
docker-compose up -d
```

Сборка может занять некоторое время. По окончании работы docker-compose сообщит, что контейнеры собраны и запущены. Используйте эту команду каждый раз для запуска приложения в контейнере.

* Выполните поочерёдно:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

В контейнере web выполнятся миграции, будет создан superuser (придумайте ему логин почту и пароль) и собрана статика.

Теперь проект доступен по адресу http://localhost/
---

Для корректной работы добавьте в папку файл .env с ключами:

DB_ENGINE
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
DB_PORT
SECRET_KEY

Для остановки контейнера:
```bash
docker-compose down
```

Чтобы внести или удалить какие-либо данные, зайдите в аккаунт вашего superuser по адресу http://localhost/admin

### Авторы
Тимофей Городилов - управление пользователями (Auth и Users): систему регистрации и аутентификации, права доступа, работу с токеном, систему подтверждения через e-mail.
Iлья Хахалкин - категории (Categories), жанры (Genres) и произведения (Title): модели, представления и эндпойнты для них.
Анна Петрова - отзывы (Review) и комментариями (Comments): описывает модели, представления, настраивает эндпойнты, определяет права доступа для запросов. Рейтинги произведений, а также реализация механизма импорта данных из csv файлов.
