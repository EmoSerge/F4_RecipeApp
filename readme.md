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
py -m vevn venv
venv\scripts\activate
```
4. Установите требуемые библиотеки.
```bash
pip install -r requirements.txt
```
5. Создайте секртерный ключ и вставьте его в файл ChatB\.env
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
6. Перейдтие в директорию ChatB
```bash
cd recipeapp
```
7. Запустите сервер.
```bash
py manage.py runserver
```