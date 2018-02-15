# hooli
Блог, написанный с применением Django в качестве веб-фреймворка и postgres в качестве СУБД

На данный момент имеется следующий функционал:
- Авторизация и регистрация
- Детальный и общий просмотр всех статей (статьи имеют собственную картинку, заголовок, дату публикации, текст).
- Доступ к просмотру статей разрешен только авторизованным пользователям.


<h1>Как установить?</h1>
- <p>git clone https://github.com/twilightrus/hooli.git</p>
- <p>cd hooli</p>
- <p>pip install -r requirements.txt</p>
- <p>mv hooli/settings.py.example hooli/settings.py</p>
- <p>Отредактируйте файл hooli/settings.py, смените в нем значения NAME, HOST, USER, PASSWORD, PORT для базы данных и заполните список ALLOWED_HOSTS</p>
- <p>python manage.py runserver</p>
- <p>Переходим по http://hostname:8000 и наслаждаемся!</p>
