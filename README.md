# Library Management API

REST API для управления библиотекой на Django Rest Framework.

## Стек технологий
- Django 4.2, DRF, Simple JWT
- PostgreSQL
- Docker, Docker Compose
- OpenAPI 3.0 (drf-spectacular)

## Роли пользователей
- **Библиотекарь** – полный доступ к управлению книгами, авторами, пользователями, выдачей.
- **Читатель** – просмотр книг, создание запроса на выдачу, возврат своих книг.

## Установка и запуск

### 1. Копируйте репозиторий
```bash
git clone <url>
cd library_api