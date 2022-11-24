import django_filters
from django.contrib.auth import get_user_model
from django.db.models import Q, QuerySet
from django_filters import rest_framework as filters

from manager.models import Transaction

User = get_user_model()


def filter_categories_created_by_request_user_and_admin(queryset: QuerySet, request_user: User) \
        -> QuerySet:
    """
    Return filter queryset of personally categories created by user and general
    categories created by admin
    """

    users = User.objects.filter(Q(is_staff=True) | Q(
        email=request_user))
    category_query = queryset.filter(account__user__in=users)

    return category_query


class TransactionFilters(filters.FilterSet):
    min_amount = filters.NumberFilter(field_name="amount", lookup_expr='gte')
    max_amount = filters.NumberFilter(field_name="amount", lookup_expr='lte')
    start_date = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = [
            'transaction_type',
            'min_amount',
            'max_amount',
            'start_date',
            'end_date'
        ]
