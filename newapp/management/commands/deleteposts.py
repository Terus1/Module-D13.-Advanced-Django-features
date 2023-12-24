from django.core.management.base import BaseCommand, CommandError
from newapp.models import Post

class Command(BaseCommand):
    help = 'Удаляет все посты'
    #missing_args_message = 'Недостаточно аргументов'
    #requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Вы действительно хотите удалить все посты? да/нет')
        answer = input()
        if answer == 'да':
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Успешно удалены все посты'))
            return
        self.stdout.write(self.style.ERROR('Произошла ошибка'))
