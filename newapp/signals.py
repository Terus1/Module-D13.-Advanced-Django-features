from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_save
from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives

from .models import *



def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'flatpages/post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject='title',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [i.email for i in subscribers]

        send_notifications(instance.preview(), instance.id, instance.title, subscribers)

















# def send_notifications(preview, pk, title, subscribers_emails):
#     html_content = render_to_string(
#         'flatpages/post_created_email.html',
#         {
#             'text': preview,
#             'link': f'http://127.0.0.1:8000/news/{pk}',
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers_emails,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers_emails = []
#
#         for cat in categories:
#             subscribers = Subscriber.objects.filter(category=cat)
#             subscribers_emails += [subs.user.email for subs in subscribers]
#             print(subscribers_emails)
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)


# @receiver(post_save, sender=Post)
# def product_created(instance, **kwargs):
#     print('Создан пост: ', instance)



