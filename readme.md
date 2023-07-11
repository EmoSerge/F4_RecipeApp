<h1>Домашнее задание модуля F4 - DRF, React, OpenAPI </h1>

<h2>Ваше задание:</h2>

1. Создайте фуллстек-приложение с рецептами блюд, которое будет использовать Django Rest Framework, автодокументацию OpenAPI+Swagger и react-router.
2. Давать пользователю возможность создавать рецепты не нужно: достаточно распределить их по категориям и отображать в клиенте и в API.
3. Где отображать документацию API — решать вам.
4. У каждого блюда и каждой категории должна быть своя страница: с главной страницы можно перейти на любую из категорий, а из категории — на любой рецепт этой категории.


<h2>Запуск проекта</h2>

Запуск проекта

Примеры команд даны для Windows-системы.

1. Перейдите в терминале в директорию проекта. 
2. Клонируйте проект.
```bash
git clone https://github.com/EmoSerge/F4_RecipeApp
```
3. Перейдите в папку backend и создайте и активируйте виртуальную среду.
```bash
cd backend
py -m venv venv
venv\scripts\activate
```
4. Установите требуемые библиотеки.
```bash
pip install -r requirements.txt
```
5. Создайте секретный ключ и вставьте его в файл backend\recipeapp\recipeapp\.env в переменную SECRET_KEY
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
6. Перейдтие в директорию recipeapp
```bash
cd recipeapp
```
7. Запустите сервер.
```bash
py manage.py runserver
```
8. Откройте второе окно терминала
9. Перейдите в директорию frontend
```bash
cd frontend
```
10. Установите требуемые зависимости
```bash
npm install
```
11. Запустите локальный web-сервер
```bash
npm start
```

<h2>Расположение API-документации</h2>
Доступ к API только по GET-запросам. Для наполнения базы данных используется Административная панель Django.

Вся документация расположена по адресам:

http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/swagger
http://127.0.0.1:8000/swagger.json

<h2>Возможности приложения</h2>
Главная страница приложения расположена по адресу:

http://localhost:3000/

В шапке приложения закреплена кнопка для возврата к главной странице.
На главной странице можно перейти на страницу категории и увидеть все рецепты в данной категории.
На странице категории можно перейти на страницу рецепта и подробно ознакомится с ним.


