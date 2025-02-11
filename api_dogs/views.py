from typing import Any
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.db.models import Avg, Subquery, OuterRef, Count, QuerySet

from api_dogs.models import Breed, Dog
from api_dogs.serializers import BreedSerializer, DogSerializer

# Create your views here.

class DogViewSet(ModelViewSet):
    """API-эндпоинт для управления собаками
    
    Позоляет выполнять CRUD операции с моделью Dog
    """
    queryset: QuerySet[Dog] = Dog.objects.all()
    serializer_class = DogSerializer

    def get_serializer_context(self) -> dict[str, Any]:
        """
        Передаёт в сериализатор флаги для динамического отображения полей
        
        Returns:
            Dict[str, Any]: Контекст для сериализатора.
        """
        context: dict[str, Any] = super().get_serializer_context()

        if self.action == 'list':  # GET /api/dogs/
            context['is_list_dog_view'] = True

        if self.action == 'retrieve':  # GET /api/dogs/<id>/
            context['is_detail_dog_view'] = True

        return context
    
    def get_queryset(self) -> QuerySet[Dog]:
        """
        Возвращает QuerySet для модели Dog с аннотациями.

        - Для списка собак (`list`):
            - Использует `select_related('breed')` для оптимизации запроса.
            - Добавляет аннотацию `breed_avg_age`, вычисляющую средний возраст собак той же породы.

        - Для детального просмотра (`retrieve`):
            - Добавляет аннотацию `dogs_breed_count`, вычисляющую количество собак той же породы.

        Returns:
            QuerySet: Отфильтрованный и аннотированный набор данных.
        """
        queryset: QuerySet[Dog] = Dog.objects.all()

        if self.action == 'list':
            queryset = queryset.select_related('breed').annotate(
                breed_avg_age=Subquery(
                    Dog.objects.filter(breed=OuterRef('breed'))
                    .annotate(avg_age=Avg('age'))
                    .values('avg_age')[:1]
                )
            )
        
        if self.action == 'retrieve':
            queryset = queryset.annotate(
                dogs_breed_count=Subquery(
                Dog.objects.filter(breed=OuterRef('breed'))
                .order_by()
                .values('breed')
                .annotate(count=Count('id'))
                .values('count')[:1]
                )
            )
        
        return queryset
            



class BreedViewSet(ModelViewSet):
    """API-энпоинт для работы с породами собак

    Позволяет выполнять CRUD операции с моделью Breed
    """
    queryset: QuerySet[Breed] = Breed.objects.all()
    serializer_class = BreedSerializer

    def get_serializer_context(self) -> dict[str, Any]:
        """
        Передаёт в сериализатор флаги для динамического отображения полей
            
        Returns:
            Dict[str, Any]: Контекст для сериализатора.
        """
        context: dict[str, Any] = super().get_serializer_context()

        if self.action == 'list':
            context['is_list_breed_view'] = True

        return context
    
    def get_queryset(self) -> QuerySet[Breed]:
        """
        Возвращает QuerySet для модели Breed с аннотациями.

        - Для списка пород (`list`):
            - Добавляет аннотацию `dogs_breed_count`, вычисляющую количество собак данной породы.

        Returns:
            QuerySet: Отфильтрованный и аннотированный набор данных.
        """

        queryset: QuerySet[Breed] = Breed.objects.all()
        if self.action == 'list':
            queryset = queryset.annotate(
               dogs_breed_count=Count('dogs')
            )
        
        return queryset