# Внесены правки:
Создан вывод профиля пользователя 
1.![Screenshot 2025-03-07 at 20-49-54 Spam sender](https://github.com/user-attachments/assets/c98b40bc-2cc1-485c-9752-300061c1fbaa)
2. Кнопка Вход в редактор профиля расположена в области вход/выход/регистрация<br>
![Screenshot 2025-03-07 at 21-47-45 Spam sender.png](static/images/Screenshot%202025-03-07%20at%2021-47-21%20Spam%20sender.png)<br>
3. Пользователю организован доступ к редактированию своего профиля
![Screenshot 2025-03-07 at 21-47-45 Spam sender.png](static/images/Screenshot%202025-03-07%20at%2020-58-16%20Spam%20sender.png)
4. Установлен flake8 , при помощи которого проверено соответствие PEP-8 
---
# Веб-приложение для управления рассылками сообщений

![Screenshot 2025-03-06 at 06-59-41 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2006-59-41%20Spam%20sender.png)
<br> ## Страница рассылки
![Screenshot 2025-03-06 at 07-10-16 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2007-10-16%20Spam%20sender.png)
<br> ## Страница Детали рассылки: Вид для создателя рассылки
![Screenshot 2025-03-06 at 07-12-44 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2007-12-44%20Spam%20sender.png)
<br> ## Страница Детали рассылки: Вид рассылки детали не для владельца, (старт рассылок отсутсвует)
![Screenshot 2025-03-06 at 07-16-27 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2007-16-27%20Spam%20sender.png)
<br> ## Кратенько про отображение списка клиентов нетерпеливых получателей долгожданных писем
![Screenshot 2025-03-06 at 07-19-53 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2007-19-53%20Spam%20sender.png)
<br> ## Редактор рассылки
![Screenshot 2025-03-06 at 07-32-56 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2007-32-56%20Spam%20sender.png)
<br> ## Удаление рассылки
![Screenshot 2025-03-06 at 07-35-46 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2007-35-46%20Spam%20sender.png)
<br> ## Он CRUD во всём, поэтому скриншоты всего не показывают
![Screenshot 2025-03-06 at 07-37-36 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2007-37-36%20Spam%20sender.png)
<br> ## Самое главное достижение,- я заставил яндекс явно указывать что рассылка не состоялась. см. Ниже
![Screenshot 2025-03-06 at 07-48-07 Spam sender.png](static/images/Screenshot%202025-03-06%20at%2007-48-07%20Spam%20sender.png)
# Веб-приложение для управления рассылками сообщений

# Описание проекта

Веб-приложение разработано для управления рассылками сообщений клиентам. Оно позволяет создавать, редактировать, удалять и просматривать рассылки, а также отслеживать статистику отправки. Приложение реализовано на Django и включает следующие функции:

- Управление клиентами (добавление, редактирование, удаление).
    
- Управление сообщениями (создание, редактирование, удаление).
    
- Управление рассылками (создание, запуск, завершение, удаление).
    
- Отправка сообщений по требованию.
    
- Логирование попыток рассылки.
    
- Статистика и отчеты по рассылкам.
    
- Регистрация и аутентификация пользователей.
    
- Разграничение прав доступа (пользователи и менеджеры).
    
- Кеширование данных с использованием Redis.
    

---

# Функциональность

## Основные функции:

1. **Управление клиентами**:
    
    - Добавление, редактирование и удаление клиентов.
        
    - Хранение информации о клиентах (email, Ф.И.О., комментарий).
        
2. **Управление сообщениями**:
    
    - Создание, редактирование и удаление сообщений.
        
    - Хранение темы и тела письма.
        
3. **Управление рассылками**:
    
    - Создание, редактирование и удаление рассылок.
        
    - Указание времени начала и окончания рассылки.
        
    - Выбор сообщения и списка получателей.
        
    - Статусы рассылки: "Создана", "Запущена", "Завершена".
        
4. **Отправка сообщений**:
    
    - Автоматическая отправка сообщений по расписанию.
        
    - Ручной запуск рассылки через интерфейс или командную строку.
        
    - Логирование попыток отправки (успешно/не успешно).
        
5. **Статистика**:
    
    - Отображение количества всех рассылок, активных рассылок и уникальных клиентов.
        
    - Отчеты по успешным и неуспешным попыткам рассылки.
        
6. **Аутентификация и авторизация**:
    
    - Регистрация и вход пользователей.
        
    - Восстановление пароля.
        
    - Разграничение прав доступа:
        
        - Пользователи могут управлять только своими рассылками и клиентами.
            
        - Менеджеры могут просматривать все рассылки и блокировать пользователей.
            
7. **Кеширование**:
    
    - Использование Redis для кеширования данных и повышения производительности.
        

---

# Установка и запуск

## Требования:

- Python 3.10+
    
- Redis
    
- PostgreSQL (или другая СУБД, поддерживаемая Django)
    

## Шаги для установки:

1. Клонируйте репозиторий:
    
    bash
    
    Copy
    
    git clone https://github.com/Lazarus-Phoenix/mailing_management_service.git
    cd mailing_management_service
    
2. Создайте виртуальное окружение и установите зависимости:
    
    bash
    
    Copy
    
    python -m venv venv
    source venv/bin/activate  # Для Linux/MacOS
    # venv\Scripts\activate    # Для Windows
    pip install -r requirements.txt
    
3. Настройте базу данных:
    
    - Создайте базу данных в PostgreSQL.
        
    - Обновите настройки в `settings.py`:
        
        python
        
        Copy
        
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_db_name',
                'USER': 'your_db_user',
                'PASSWORD': 'your_db_password',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
        
4. Примените миграции:
    
    bash
    
    Copy
    
    python manage.py migrate
    
5. Создайте суперпользователя:
    
    bash
    
    Copy
    
    python manage.py createsuperuser
    
6. Запустите Redis:
    
    bash
    
    Copy
    
    redis-server
    
7. Запустите сервер разработки:
    
    bash
    
    Copy
    
    python manage.py runserver
    
8. Перейдите в браузере по адресу:
    
    Copy
    
    http://127.0.0.1:8000/
    

---

# Использование

## Основные страницы:

- **Главная страница**: Отображает статистику по рассылкам.
    
- **Клиенты**: Управление списком клиентов.
    
- **Сообщения**: Управление шаблонами сообщений.
    
- **Рассылки**: Управление рассылками и их статусами.
    
- **Попытки рассылок**: Просмотр истории отправки сообщений.
    
- **Отчеты**: Статистика по успешным и неуспешным попыткам.
    

## Команды:

- Запуск рассылки вручную:
    
    bash
    
    Copy
    
    python manage.py send_mailings
    

---

# Технологии

- **Backend**: Django, Django REST Framework (если используется REST).
    
- **Frontend**: HTML, CSS, Bootstrap.
    
- **База данных**: PostgreSQL.
    
- **Кеширование**: Redis.
    
- **Аутентификация**: Django Allauth.
    
- **Линтер**: Flake8.
    

---

# Структура проекта

Copy

mailing_management_service/
├── mailing/                  # Приложение для управления рассылками <br>
│   ├── models.py             # Модели (Клиент, Сообщение, Рассылка, Попытка) <br>
│   ├── views.py              # Представления (CRUD, отчеты, отправка) <br>
│   ├── templates/            # Шаблоны HTML <br>
│   └── urls.py               # URL-адреса приложения <br>
├── users/                    # Приложение для управления пользователями <br>
│   ├── models.py             # Модель пользователя <br>
│   └── views.py              # Регистрация, вход, профиль <br>
├── config/                   # Настройки проекта <br>
│   ├── settings.py           # Основные настройки <br>
│   └── urls.py               # Глобальные URL-адреса <br>
├── manage.py                 # Управление проектом <br>
└── requirements.txt          # Зависимости <br>

---

# Автор

- **Имя**: [ Гви́до Фокс ]
    
- **GitHub**: [Lazarus-Phoenix](https://github.com/Lazarus-Phoenix)
    
- **Контакт**: [Я везде!- прошепчи и я услышу.]
    

---

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности см. в файле [LICENSE](https://license/).
