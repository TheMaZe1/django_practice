from typing import Any
from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField

from api_dogs.models import Breed, Dog


class BreedSerializer(ModelSerializer):

    class Meta:
        model = Breed
        fields = '__all__'
    
    def to_representation(self, instance: Breed) -> dict[str, Any]:
        """
        Преобразует объект модели в словарь для отображения в API.

        - Если передан контекст `is_list_breed_view=True`, добавляет `dogs_breed_count`.

        Args:
            instance (Breed): Экземпляр модели `Breed`.

        Returns:
            dict[str, Any]: Сериализованные данные породы.
        """
        data = super().to_representation(instance)

        if self.context.get('is_list_breed_view', False):
            data['dogs_breed_count'] = instance.dogs_breed_count

        return data



class DogSerializer(ModelSerializer):
    breed = BreedSerializer(read_only=True)
    breed_id = PrimaryKeyRelatedField(queryset=Breed.objects.all(), source='breed', write_only=True)

    class Meta:
        model = Dog
        fields = '__all__'


    def to_representation(self, instance: Dog) -> dict[str, Any]:
        """
        Преобразует объект модели в словарь для отображения в API.

        - Если передан контекст `is_detail_dog_view=True`, добавляет `dogs_breed_count`.
        - Если передан контекст `is_list_dog_view=True`, добавляет `average_age` в отображение породы.

        Args:
            instance (Dog): Экземпляр модели `Dog`.

        Returns:
            dict[str, Any]: Сериализованные данные собаки.
        """
        data = super().to_representation(instance)

        if self.context.get('is_detail_dog_view', False):
            data['dogs_breed_count'] = instance.dogs_breed_count
        
        if self.context.get('is_list_dog_view', False):
            data['breed']['average_age'] = instance.breed_avg_age

        return data