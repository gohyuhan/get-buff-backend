from rest_framework import serializers

from training.models import (
    Exercise,
    PresetTrainingSet, 
    PresetTrainingExercise,
    CustomTrainingSet,
    CustomTrainingExercise
)
from muscle.serializer import (
    MuscleSerializer,
    MuscleCategorySerializer
)
from user.serializer import UserProfileSerializer



class ExerciseSerializer(serializers.ModelSerializer):
    muscle = MuscleSerializer(many=True)
    muscle_category = MuscleCategorySerializer(many=True)

    class Meta:
        model = Exercise
        fields = (
            "id",
            "name",
            "explanation",
            "calculate_in", 
            "animation",
            "muscle",
            "muscle_category",
            "min_count"
        )
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['calculate_in'] = instance.get_calculate_in_display()
        return representation


class PresetTrainingExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=False)
    class Meta:
        model = PresetTrainingExercise
        fields = (
            "id",
            "calculate_in",
            "required_value",
            "level",
            "exercise",
            "order",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['level'] = instance.get_level_display()
        representation['calculate_in'] = instance.get_calculate_in_display()
        return representation


class PresetTrainingSetSerializer(serializers.ModelSerializer):
    exercise = PresetTrainingExerciseSerializer(source='preset_training_exercise', many=True)
    muscle_category = MuscleCategorySerializer(many=False)
    
    class Meta:
        model = PresetTrainingSet
        fields = (
            "id",
            "name",
            "level",
            "muscle_category",
            'exercise',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['level'] = instance.get_level_display()
        return representation
    

class CustomTrainingExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=False)
    class Meta:
        model = CustomTrainingExercise
        fields = (
            "id",
            "calculate_in", 
            "required_value",
            "level",
            "exercise",
            "order",
            "status"
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['calculate_in'] = instance.get_calculate_in_display()
        representation['level'] = instance.get_level_display()
        representation['status'] = instance.get_status_display()
        return representation


class CustomTrainingSetSerializer(serializers.ModelSerializer):
    exercise = CustomTrainingExerciseSerializer(source="custom_preset_training_exercise", many=True)
    muscle_category = MuscleCategorySerializer(many=False)
    user_profile = UserProfileSerializer(many=False)

    class Meta:
        model = CustomTrainingSet
        fields = (
            "id",
            "user_profile",
            "name",
            "level",
            "muscle_category",
            "status",
            "training_type",
            "exercise",
            "created"
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['level'] = instance.get_level_display()
        representation['status'] = instance.get_status_display()
        representation['training_type'] = instance.get_training_type_display()
        return representation
    
    


