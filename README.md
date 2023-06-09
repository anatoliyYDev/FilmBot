# Фильм Бот

Данный бот позволяет администраторам публиковать
информацию о фильмах, назначая им специальные коды с
помощью которых пользователи смогут находить различные
фильмы

### Функионал

* Проверка подписки на канал
* Редакция всей базы фильмов
* Поиск фильмов по коду

<br>

### Установка

Если вы желаете запустить данного бота у себя на
компьютере, тогда следуйте инструкциям ниже

<br>

#### Установка Python 3.11

Поскольку бот написан на [Python](https://www.python.org/), вам необходимо 
поставить его на компьютер. 
Для этого заходим на сайт Python и скачиваем нужную нам версию. 
В установщике поставьте галочку на "ADD TO PATH"

<br>

#### Получение токена бота

В Telegram заходим в [@BotFather](https://t.me/BotFather) прописываем /newbot и 
следуем инструкции. В итоге вы получите от бота так 
называемый API TOKEN. Скопируйте его и вставьте в файл .env 
после "BOT_TOKEN="

<br>

#### Получение ID Telegram

ID нужен для того чтобы назначить человека или несколько людей админом в боте. 
Это влияет на редакцию базы с вашими фильмами и получение сообщений
об ошибках.

Перейдите в специального [бота](https://t.me/getmyid_bot), напишите ему что-нибудь 
и в ответе число после "Your user ID:" - ваш ID. 
Для получения ID другого человека, просто перешлите 
этому боту сообщение который писал тот человек 
и в ответе число после "Forwarded from:" - ID того человека.

Далее зайдите в .env и после "ADMINS=" укажите все ID админов через запятую. Ну или же просто ID, если будет один админ

Теперь нам нужно получить ID канала на который будет проверяться
подписка. Для этого тому же боту перешлите пост из канала, скопируйте
отрицательное число из ответа и вставьте в .env после "CHANNEL_ID="

Так же нам необходимо скопировать ссылку на наш канал и вставить
в .env после "CHANNEL_LINK=" и добавить бота в этот канал в качестве
администратора

<br>

#### Последний рывок

Нам осталось выполнить пару команд в командной строке:

1. cd <путь папки с ботом>
2. pip install -r requirements.txt
3. python run.py
