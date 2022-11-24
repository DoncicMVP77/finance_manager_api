from celery import Celery

from manager.services.send_statistic_report_about_user_service import \
    UsersStatisticReportService

app = Celery()


@app.task
def send_yesterday_user_statistic_on_email_task():
    users_service = UsersStatisticReportService()
    users_service.execute()
