from allauth.account.forms import SignupForm
from django.core.mail import EmailMultiAlternatives, mail_admins


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        mail_admins(
            subject='Новый пользователь',
            message=f'Пользователь {user.username} зарегистрировался на сайте!'
        )

        subject = 'Добро пожаловать в наш интернет-магазин!'
        text = f'{user.username} вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/news/search/">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, 'text/html')
        msg.send()
        return user
