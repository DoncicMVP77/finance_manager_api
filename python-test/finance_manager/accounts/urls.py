from django.urls import include, path
from rest_framework import routers
from accounts.views import AccountViewSet

router = routers.DefaultRouter()
router.register(r'', AccountViewSet)

urlpatterns = [
    path('', include(router.urls))
]
