    # test task for AeroDE

## Основные возможности

- Автоматическое создание базы данных.
- Загрузка данных из различных API в созданную базу данных.
- Оркестрация задач с использованием `cron`.

## Настройка и установка
    
### 1. Клонирование репозитория:

```bash
git clone <https://github.com/valfitkovich/test_taskAeroDE>
cd <Имя директории вашего репозитория>
```
### 2. Установка зависимостей:
```bash
pip install -r requirements.txt
```
### 3.Создание базы данных и таблиц:
```bash
python create_database.py
```
### 4.Добавьте свои креды в main.py:
```python
 def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            dbname="test_task",
            user="",
            password="",
            host="localhost",
            port="5432"
        )
```

### 5. Оркестрация задач:
```bash
chmod +x setup_cron.sh
./setup_cron.sh
```

