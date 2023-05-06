from django.urls import path, include
from rest_framework.routers import DefaultRouter

from status_log import views

router = DefaultRouter()
router.register('api/status-log', views.StatusLogViewSet)

urlpatterns = router.urls
