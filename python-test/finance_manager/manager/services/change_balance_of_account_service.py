from collections import OrderedDict
from decimal import Decimal

from accounts.models import Account
from django.contrib.auth import get_user_model

User = get_user_model()


def change_account_balance_service(validate_data: OrderedDict, account: Account) -> None:
    """
    Change account balance depending from transaction type
    """
    if validate_data['transaction_type'] == 'Income':
        account.balance += Decimal(validate_data['amount'])
        account.save()
    elif validate_data['transaction_type'] == 'Expense':
        account.balance -= Decimal(validate_data['amount'])
        account.save()
