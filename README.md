# radiance
<img src="https://travis-ci.org/twilightrus/radiance.svg?branch=master">
Блог, написанный с применением Django в качестве веб-фреймворка и postgres в качестве СУБД


На данный момент имеется следующий функционал:
- Авторизация и регистрация
- Детальный и общий просмотр всех статей (статьи имеют собственную картинку, заголовок, дату публикации, текст, комментарии, количество комментариев).
- Статьи представлены в виде страниц, на каждой по 6 штук.
- Доступ к просмотру статей разрешен только авторизованным пользователям.
- Комментирование статей (AJAX).
- Лайки на статьи и комментарии к ним (AJAX);
- Редактирование и удаление своих комментариев;

<h1>Как установить?</h1>

<b>
- git clone https://github.com/twilightrus/radiance.git

- cd radiance && virtualenv venv --python=python3.6 && source venv/bin/activate && mv .env.example .env

- Edit file .env for your Postgres user-data (DB, User, Password, Host, Port.

- pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate

- python manage.py runserver

- Go to http://localhost:8000 and test your application!
</b>