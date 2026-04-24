from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("user.urls")),
    path("api/customers/", include("customer.urls")),
    path("api/employees/", include("employee.urls")),
    path("api/vehicles/", include("vehicle.urls")),
    path("api/health/", include("health.urls")),
    path("api/ai_assistant/", include("ai_assistant.urls")),
    path("api/service/", include("service.urls")),
]
