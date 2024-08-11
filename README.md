# Library Project

## Описание

Library Project — это веб-приложение для управления библиотечными ресурсами. Приложение предоставляет функциональность для управления книгами, пользователями и процессами выдачи книг. Оно предназначено для упрощения администрирования библиотек, предоставляя удобный интерфейс для добавления, редактирования и удаления книг, а также для управления пользовательскими записями и записями о выдаче книг.

## Основные функции

- **Управление книгами**: Добавляйте новые книги в библиотеку, редактируйте информацию о книгах и удаляйте их из системы.
- **Управление пользователями**: Регистрация новых пользователей, редактирование их данных и удаление учетных записей.
- **Процессы выдачи книг**: Отслеживание текущих выданных книг, управление сроками возврата и проверка наличия книг.
- **Административная панель**: Управление всеми аспектами приложения через встроенную панель администратора Django.

## Технологии

- **Django**: Высокоуровневый фреймворк для веб-разработки на Python, который упрощает создание сложных веб-приложений.
- **PostgreSQL**: Мощная реляционная база данных, используемая для хранения информации о книгах, пользователях и процессах выдачи книг.
- **Docker**: Платформа для контейнеризации приложений, обеспечивающая изоляцию и упрощение развертывания приложений.
- **Docker Compose**: Инструмент для управления многоконтейнерными Docker приложениями, позволяющий легко настраивать и запускать приложения, состоящие из нескольких сервисов.

## Цели проекта

Library Project предназначен для автоматизации процессов управления библиотечными ресурсами. Он позволяет библиотекарям и администраторам:

- Упростить администрирование библиотеки, используя графический интерфейс.
- Эффективно управлять большими объемами данных о книгах и пользователях.
- Обеспечить удобный доступ к функциональности через веб-интерфейс.
- Использовать современные технологии для надежности и масштабируемости приложения.

## Системные требования

- **Операционная система**: Linux, macOS или Windows
- **Docker**: Версия 20.10 или новее
- **Docker Compose**: Версия 1.29 или новее
## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone <URL вашего репозитория>
   cd <Имя вашего репозитория>
   
## Запуск проекта

1. Постройте и запустите контейнеры Docker:

   ```bash
   docker-compose up -d --build

2. Выполните миграции базы данных:

   ```bash
   docker-compose exec habit python manage.py migrate

3. Создайте суперпользователя (если необходимо):

   ```bash
   docker-compose exec habit python manage.py createsuperuser

4. Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к приложению.

## Команды Docker

Запуск контейнеров в фоновом режиме:

    ```bash
    docker-compose up -d

Остановка контейнеров:

    ```bash
    docker-compose down

Перестройка контейнеров и перезапуск:

    ```bash
    docker-compose up -d --build

Просмотр логов контейнеров:

    ```bash
    docker-compose logs

Запуск оболочки в контейнере habit:

    ```bash
    docker-compose exec habit bash

Остановка всех контейнеров:

    ```bash
    docker-compose stop

## Завершение работы

**Для остановки и удаления всех контейнеров, сетей и томов:**

    ```bash
    docker-compose down -v
