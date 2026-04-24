from django.urls import path
from ai_assistant.views.assist_view import AssistView

urlpatterns = [
    path('', AssistView.as_view(), name='ai-assistant'),
]
