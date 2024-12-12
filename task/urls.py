from django.urls import path
from .views import QuestionListCreateAPIView, AnswerListCreateAPIView, QuestionDetailAPIView,questions_list,answer_question

urlpatterns = [
    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('questions/<int:question_id>/answers/', AnswerListCreateAPIView.as_view(), name='answer-list'),
    path('', questions_list, name='questions_list'),
    path('answer/<int:question_id>/', answer_question, name='answer_question'),
]
