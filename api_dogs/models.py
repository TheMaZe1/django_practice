from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Dog(models.Model):
    """Модель для хранения информации о собаке

    Атрибуты:
        name (str): Имя собаки
        age (int): Возраст собаки
        breed (Breed): Порода собаки
        gender (str): Пол собаки
        color (str): Цвет собаки
        favorite_food (str): Любимая еда собаки
        favorite_toy (str): Любимая игрушка собаки
    """
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(1)])
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE, related_name='dogs')
    gender = models.CharField(max_length=255, choices=Gender)
    color = models.CharField(max_length=255)
    favorite_food = models.CharField(max_length=255)
    favorite_toy = models.CharField(max_length=255)


class Breed(models.Model):
    """Модель для хранения информации о породе собаке

    Атрибуты:
        name (str): Название породы
        size (int): Размер породы
        friedlines (int): Дружилюбие(от 1 до 5)
        trainability (int): Обучаемость(от 1 до 5)
        shedding_amount (int): Линька(от 1 до 5)
        excercise_needs (int): Нужда в физических упражнениях(от 1 до 5)
    """
    class Size(models.TextChoices):
        TINY = 'TN', 'Tiny'
        SMALL = 'SM', 'Small'
        MEDIUM = 'MD', 'Medium'
        LARGE = 'LG', 'Large'

    name = models.CharField(max_length=255)
    size = models.CharField(max_length=2, choices=Size)
    friendlines = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    trainability = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    shedding_amount = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    exercise_needs = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
