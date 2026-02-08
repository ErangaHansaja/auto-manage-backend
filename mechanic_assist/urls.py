from django.urls import path
from mechanic_assist.views import AssistView

urlpatterns = [
    # endpoints will be added later
    path('mechanic-assist', AssistView.as_view(), name='ai-agent'),
]
