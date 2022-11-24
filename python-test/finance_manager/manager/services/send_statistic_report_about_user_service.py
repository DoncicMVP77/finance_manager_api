import datetime
from dataclasses import dataclass
from typing import Iterable, List

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from finance_manager import settings

from manager.models import Transaction

User = get_user_model()


@dataclass
class Statistic:
    sum_income: int
    sum_expense: int
    change_balance: int
    detail_income: List[str]
    detail_expense: List[str]


@dataclass
class UserStatistic:
    email: str
    statistic: Statistic


class UsersStatisticReportService:

    @staticmethod
    def _extract_user_data() -> Iterable[User]:
        return User.objects.all()

    def _get_list_all_transactions_from_yesterday(self) -> Iterable[Transaction]:
        yesterday = datetime.datetime.now() - datetime.timedelta(hours=24)
        list_transactions = Transaction.objects.select_related('account').all()
        return list_transactions.filter(timestamp__day=yesterday.day)

    def _calculate_yesterday_user_statistic(self, transaction_list: Iterable[Transaction]):
        sum_income = 0
        sum_expense = 0
        change_balance = 0
        detail_income = []
        detail_expense = []
        for transaction in transaction_list:
            if transaction.transaction_type == 'Income':
                sum_income += transaction.amount
                detail_income.append(f"{transaction.category} - {transaction.amount}")
            elif transaction.transaction_type == 'Expense':
                sum_expense += transaction.amount
                detail_expense.append(f"{transaction.category} - {transaction.amount}")
        change_balance = sum_income - sum_expense
        return Statistic(
            sum_income=sum_income,
            sum_expense=sum_expense,
            change_balance=change_balance,
            detail_income=detail_income,
            detail_expense=detail_expense
        )

    def _get_yesterday_user_statistic(self,
                                      users: Iterable[User],
                                      transaction: Iterable[Transaction]):
        for user in users:
            list_user_yesterday_transactions = transaction.filter(
                account__user=user)
            user_statistic = self._calculate_yesterday_user_statistic(
                list_user_yesterday_transactions)
            yield UserStatistic(user, user_statistic)

    def _send_yesterday_user_statistic_on_email(self,
                                                list_users_statistic: Iterable[UserStatistic]):
        for user_statistic in list_users_statistic:
            subject = f"Вчерашняя статистика"

            string_change_balance = f"Вчера ваш ежедневный баланс изменился на" \
                                    f" {user_statistic.statistic.change_balance} \n"
            string_sum_income = f"Доходы составили: {user_statistic.statistic.sum_income} \n"
            string_sum_expense = f"Расходы составили: {user_statistic.statistic.sum_expense}  \n"
            string_list_income = "Все доходы \n" + "\n".join(
                user_statistic.statistic.detail_income) \
                + '\n'
            string_list_expense = "Все расходы" + "\n".join(
                user_statistic.statistic.detail_expense) + '\n'

            message = string_change_balance + string_sum_income + string_sum_expense + \
                      string_list_income + string_list_expense

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_statistic.email],
                fail_silently=True,
            )

    def execute(self):
        users = self._extract_user_data()
        list_transactions_from_yesterday = self._get_list_all_transactions_from_yesterday()
        user_statistic = self._get_yesterday_user_statistic(
            users=users,
            transaction=list_transactions_from_yesterday
        )
        self._send_yesterday_user_statistic_on_email(user_statistic)
