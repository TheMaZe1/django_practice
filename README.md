# django-practice

Это REST API сервис для управления собаками и их породами. Позволяет выполнять CRUD операции с моделями в базе данных.

## Установка и запус

### 1. Колинрование репозитория
```sh
https://github.com/TheMaZe1/django_practice.git
```

### 2. Настройка окружения

Создайте файл .env на основе .env.example

### 3. Запуск через Docker

Запустите контейнеры командой
```sh
docker-compose up -d --build
```

Готово. API доступно по адресу:
http://localhost:8000/api/

## Пример использование API

### Получить список собак
```http
GET /api/dog/
```

```json
[
	{
		"id": 1,
		"breed": {
			"id": 1,
			"name": "Labrador",
			"size": "MD",
			"friendlines": 2,
			"trainability": 3,
			"shedding_amount": 2,
			"exercise_needs": 1,
			"average_age": 3.0
		},
		"name": "Bertaa",
		"age": 3,
		"gender": "M",
		"color": "Orange",
		"favorite_food": "Viskas",
		"favorite_toy": "ball"
	},
	{
		"id": 2,
		"breed": {
			"id": 1,
			"name": "Labrador",
			"size": "MD",
			"friendlines": 2,
			"trainability": 3,
			"shedding_amount": 2,
			"exercise_needs": 1,
			"average_age": 3.0
		},
		"name": "Bobik",
		"age": 10,
		"gender": "M",
		"color": "Orange",
		"favorite_food": "Viskas",
		"favorite_toy": "ball"
	}
]
```

### Получить информацию о конкретной собаке
```http
GET /api/dog/1/
```

```json
{
	"id": 1,
	"breed": {
		"id": 1,
		"name": "Labrador",
		"size": "MD",
		"friendlines": 2,
		"trainability": 3,
		"shedding_amount": 2,
		"exercise_needs": 1
	},
	"name": "Bertaa",
	"age": 3,
	"gender": "M",
	"color": "Orange",
	"favorite_food": "Viskas",
	"favorite_toy": "ball",
	"dogs_breed_count": 2
}
```

### Получить список пород
```http
GET /api/breed/
```

```json
[
	{
		"id": 1,
		"name": "Labrador",
		"size": "MD",
		"friendlines": 2,
		"trainability": 3,
		"shedding_amount": 2,
		"exercise_needs": 1,
		"dogs_breed_count": 2
	}
]
```

### Получить конкретную породу
```http
GET /api/breed/1/
```

```json
{
	"id": 1,
	"name": "Labrador",
	"size": "MD",
	"friendlines": 2,
	"trainability": 3,
	"shedding_amount": 2,
	"exercise_needs": 1
}
```

### Добавить новую собаку
```http
POST /api/dog/
```

Тело запроса
```json
{	
    "name": "Bobik",
	"age": 10,
	"breed_id": 1,
	"gender": "M",
	"color": "Orange",
	"favorite_food": "Viskas",
	"favorite_toy": "ball"
}
```

### Удалить собаку
```http
DELETE /api/dogs/1/
```