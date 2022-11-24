from django.urls import include, path
from rest_framework import routers

from manager.views import (BudgetViewSet, CategoryViewSet, TagViewSet,
                           TransactionViewSet)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'budget', BudgetViewSet)
router.register(r'tags', TagViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('categories/', CategoryViewSet.as_view({'get':'list'}), name='categories'),
    # path('categories/<str:pk>', CategoryDetailAPIView.as_view(), name="category_detail"),
]
