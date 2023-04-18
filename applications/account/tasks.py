import time

from django.core.mail import send_mail


from main.celery import app


@app.task
def celery_confirm_email(code, email):


    full_link = f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail(
        'Он-лайн кинотеатр cinemakg',
        full_link,
        'victorkim.2016@gmail.com',
        [email]
    )


@app.task
def info_email(email):

        full_link = f'Hello'
        send_mail(
            'Он-лайн кинотеатр cinemakg',
            full_link,
            'victorkim.2016@gmail.com',
            [email]
    )

@app.task
def forgot_password_email(code, email):
    send_mail(
        'Восстановление пароля',
        f'Ваш код подтверждения: {code}',
        'victorkim.2016@gmail.com',
        [email]
    )