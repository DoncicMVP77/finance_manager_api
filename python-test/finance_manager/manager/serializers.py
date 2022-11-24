from rest_framework import serializers

from manager.models import Budget, Category, Tag, Transaction


class BudgetSerializer(serializers.ModelSerializer):
    account = serializers.ReadOnlyField(source='account.user.email')
    date_create = serializers.ReadOnlyField()
    last_update = serializers.ReadOnlyField()

    class Meta:
        model = Budget
        fields = [
            'account',
            'name',
            'balance',
            'date_create',
            'last_update',
        ]


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    date_create = serializers.ReadOnlyField()
    last_update = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = [
            'user',
            'name',
            'description',
            'date_create',
            'last_update'
        ]


class TagSerializer(serializers.ModelSerializer):
    account = serializers.ReadOnlyField(source='account.user.email')
    date_create = serializers.ReadOnlyField()
    last_update = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = [
            'account',
            'name',
            'date_create',
            'last_update'
        ]


class TransferSerializer(serializers.ModelSerializer):
    pass


class TransactionSerializer(serializers.ModelSerializer):
    account = serializers.ReadOnlyField(source='account.user.email')
    timestamp = serializers.ReadOnlyField()
    last_update = serializers.ReadOnlyField()

    class Meta:
        model = Transaction
        fields = '__all__'
