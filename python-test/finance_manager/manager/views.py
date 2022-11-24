from accounts.models import Account
from django.contrib.auth import get_user_model

from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from manager.filters import (TransactionFilters,
                             filter_categories_created_by_request_user_and_admin)
from manager.models import Budget, Category, Tag, Transaction
from manager.permissions import IsOwner, IsOwnerOrReadOnly
from manager.serializers import (BudgetSerializer, CategorySerializer,
                                 TagSerializer, TransactionSerializer)
from manager.services.change_balance_of_account_service import \
    change_account_balance_service

User = get_user_model()


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Budget.objects.all()

    def get_queryset(self):
        account = get_object_or_404(Account, user=self.request.user)
        budget_list = Budget.objects.filter(account=account)
        return budget_list


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser,]
    queryset = Category.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset
        queryset = filter_categories_created_by_request_user_and_admin(queryset=self.queryset,
                                                                       request_user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        if serializer.is_valid():
            account = get_object_or_404(Account, user=self.request.user)
            serializer.save(account=account)


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
    queryset = Tag.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset
        queryset = filter_categories_created_by_request_user_and_admin(queryset=self.queryset,
                                                                       request_user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        if serializer.is_valid():
            account = get_object_or_404(Account, user=self.request.user)
            serializer.save(account=account)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsOwner, ]
    queryset = Transaction.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionFilters

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(account__user=user).order_by('-timestamp')
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        account = get_object_or_404(Account, user=user)
        serializer.save(account=account)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        try:
            account = get_object_or_404(Account, user=self.request.user)
            change_account_balance_service(validate_data=serializer.validated_data, account=account)
        except ValueError:
            content = {'error': 'Not enough money'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
