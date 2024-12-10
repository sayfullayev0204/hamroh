from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'image', 'created_at', 'status', 'image_url', 'user']

    def create(self, validated_data):
        # Foydalanuvchini kontekstdan olib, savolga biriktiramiz
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title', 'image', 'created_at', 'question']

class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)  # Related `answers` field

    class Meta:
        model = Question
        fields = ['id', 'title', 'image', 'status', 'created_at', 'answers']
