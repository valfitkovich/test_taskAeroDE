    # Название вашего проекта

Краткое описание вашего проекта и его основных целей.

## Основные возможности

- Автоматическое создание базы данных с уникальным именем.
- Загрузка данных из различных API в созданную базу данных.
- Оркестрация задач с использованием `cron`.

## Настройка и установка

### 1. Клонирование репозитория:

```bash
git clone <URL вашего репозитория на GitHub>
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
### 4.1 Оркестрация задач:
```bash
chmod +x setup_cron.sh
./setup_cron.sh
```
