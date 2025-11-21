# Edunotifier - Система управления уроками

О проекте

Edunotifier - система управления уроками и уведомлений для образовательного процесса. Приложение позволяет преподавателям создавать уроки для студентов и автоматически отправлять уведомления.

Технические особенности
Сигналы (Signals)
Используется Django сигнал post_save для отслеживания создания новых уроков

При создании урока автоматически запускается задача уведомления

Celery & Redis
Redis - брокер сообщений для обработки фоновых задач

Celery - асинхронная очередь задач для отправки уведомлений

Уведомления обрабатываются в фоне, не блокируя основной интерфейс

### Полная инструкция для запуска:

git clone https://github.com/Neolog13/edunotifier.git
cd edunotifier

1. Создание виртуального окружения
   python -m venv venv

2. Активация виртуального окружения
   source venv/bin/activate

3. Установка зависимостей
   pip install -r requirements.txt

4. Настройка базы данных
   python manage.py migrate

5. Запуск серверов

Терминал 1 - Redis
redis-server

Терминал 2 - Celery Worker
celery -A edunotifier worker --loglevel=info

Терминал 3 - Django сервер
python manage.py runserver

Создание пользователей:
http://127.0.0.1:8000/api/auth/register/

Учитель:
{
  "username": "teacher_demo",
  "email": "teacher@example.com",
  "password": "teacher123",
  "first_name": "Иван",
  "last_name": "Преподавателев",
  "user_type": "teacher"
}

Студент:
{
  "username": "student_demo",
  "email": "student@example.com", 
  "password": "student123",
  "first_name": "Петр",
  "last_name": "Студентов",
  "user_type": "student"
}


### Доступ к приложению
API: http://localhost:8000/api/


GET    /lessons/           - список всех уроков пользователя
POST   /lessons/           - создание урока (только учителя)
GET    /lessons/{id}/      - детали урока
PUT    /lessons/{id}/      - обновление урока
PATCH  /lessons/{id}/      - частичное обновление
DELETE /lessons/{id}/      - удаление урока
POST   /lessons/{id}/confirm/ - подтверждение урока (только студенты)


POST /api/auth/register/ - регистрация пользователя
POST /api/auth/login/ - вход в систему
POST /api/auth/logout/ - выход из системы
GET  /api/auth/profile/ - профиль пользователя


Результаты работы
Результаты выполнения задач можно наблюдать в терминале Celery - там выводятся сообщения о отправленных уведомлениях:

Уведомление отправлено студенту [ID] по уроку '[Название]'

- Для остановки ручного запуска используйте Ctrl+C в каждом терминале

