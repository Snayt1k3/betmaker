# Используем официальный образ Python 3.10 как базовый
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей (requirements.txt) в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Открываем порт для приложения FastAPI
EXPOSE 5000

# Команда для запуска приложения с использованием Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
