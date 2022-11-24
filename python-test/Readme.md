# Тестовое задание "Менеджер учёта расходов"
REST API для учета расходов пользователя

# Версия 1 API
- Регистрация пользователя   
- Авторизация пользователя (по токену)   
- Транзакции пользователя - CRUD
- Категории пользователя - CRUD
- Категории пользователя - CRUD
- Отправка статистики пользователя на почту.

# Что будет реализовано в Версии 2 API
- Добавление валют(USD, EUR, RUB)
- Добавление трансфера между бюджетами
- Конвертер валют
- Авторизация через EMAIL, Facebook
- Учет и расчет статистики пользователя(День, Неделя, Месяц, Год)

#Как использовать этот проект?
1. Обновите переменные окружения в docker-compose.yml и .env файле
2. Создайте image и запустите контейнер docker:

    ```
    $ docker-compose up -d --build
    ```
Протестируйте проект на  [http://localhost:8000](http://localhost:8000).

# MANAGER_API ENDPOINT
| Method |  ENDPOINT | DESCRIPTION |
|--------|----------|--------------|          
|  **GET**   | api/v1/manager/categories  | Возвращает лист категорий 
|  **POST**  | api/v1/manager/categories  | Создает новую категорию
|  **GET**   | api/v1/manager/categories/{id}  | Возвращает определенную категорию
|  **PUT**   | api/v1/manager/categories/{id}  | Обновляет категорию
|  **DELETE**  | api/v1/manager/categories/{id}   | Удаляет категорию
|  **GET**   | api/v1/manager/tags | Возвращает лист тегов 
|  **POST**  | api/v1/manager/tags| Создает новый тег
|  **GET**   | api/v1/manager/tags/{id}   | Возвращает определенный тег
|  **PUT**   | api/v1/manager/tags/{id}   | Обновляет тег
|  **DELETE** | api/v1/manager/tags/{id}  | Удаляет тег
|  **GET**   | api/v1/manager/transactions | Возвращает лист транзакций 
|  **POST**   | api/v1/manager/transactions | Создает новый объект транзакции
|  **GET**   | api/v1/manager/transactions/{id} | Возвращает определенную транзакцию
|  **PUT**   | api/v1/manager/transactions/{id} | Обновляет транзакцию
|  **DELETE**   | api/v1/manager/transactions/{id} | Удаляет транзакцию

# AUTHENTICATION_API ENDPOINT
| Method |  ENDPOINT | DESCRIPTION |
|--------|----------|--------------|          
|  **POST**   | api/v1/authentication/register  | Создание нового пользователя 
|  **POST**   | api/v1/authentication/change_password/{id}/  | Смена пароля пользователя
|  **POST**  | api/v1/authentication/token | Создает и возвращает access JWT и refresh token пользователя 
|  **POST**   | api/v1/authentication/token/refresh   | Получение нового access JWT с помощью refresh token


# ACCOUNT_API ENDPOINT
| Method |  ENDPOINT | DESCRIPTION |
|--------|----------|--------------|          
|  **GET**   | api/v1/accounts  | Возвращает лист аккаунтов
|  **POST**   | api/v1/accounts  | Создает новый аккаунт
|  **GET**  | api/v1/accounts/{id} | Возвращает определенный аккаунт
|  **PUT**   | api/v1/accounts/{id}   | Обновляет аккаунт
|  **DELETE**   | api/v1/accounts/{id}   | Удаляет аккаунт
