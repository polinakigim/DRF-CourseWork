# DRF-CourseWork

## 📝 Описание проекта

Django REST Framework-проект с поддержкой Docker, Celery и PostgreSQL.

### 🚀 Локально (без Docker)

1. Клонируйте репозиторий:

```bash
git clone https://github.com/polinakigim/DRF-CourseWork.git
cd drf-course-work
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Примените миграции и запустите сервер:

```bash
python manage.py migrate
python manage.py runserver
```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

---

### 🐳 Запуск через Docker

1. Создайте файл `.env` в корне проекта и добавьте туда переменные окружения

2. Запустите контейнеры:

```bash
docker compose up --build -d
```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

---

## 🚀 Деплой на удалённый сервер

Настроено автоматическое развертывание через **GitHub Actions**.

### 🔧 Инструкция

1. Зарегистрируйтесь на [Docker Hub](https://hub.docker.com)

2. Создайте **Personal Access Token**:
   - Перейдите в "Account Settings" → "Security"
   - Нажмите "New Access Token", укажите описание, сохраните

3. В репозитории на **GitHub**:
   - Перейдите в `Settings → Secrets → Actions`
   - Добавьте секреты:
     - `DOCKER_HUB_USERNAME`
     - `DOCKER_HUB_ACCESS_TOKEN`

4. При каждом пуше в ветку `main`:
   - GitHub Actions соберёт Docker-образ
   - Отправит его в Docker Hub
   - Подключится к серверу и перезапустит приложение

---

## 🗂 Структура проекта

- `docker-compose.yml` — описание контейнеров
- `Dockerfile` — инструкция сборки образа Django-приложения
- `config/` — конфигурация проекта
- `habit/` — основное приложение

---

## ✅ Тестирование

```bash
python manage.py test
```

---
