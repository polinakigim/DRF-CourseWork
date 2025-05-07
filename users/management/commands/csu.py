from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Создание суперпользователя по умолчанию"

    def handle(self, *args, **kwargs):
        if not User.objects.filter(email="admin@mail.ru").exists():
            user = User.objects.create(
                email="admin@mail.ru",
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            user.set_password("123")
            user.save()
            self.stdout.write(self.style.SUCCESS("Суперпользователь успешно создан"))
        else:
            self.stdout.write(self.style.WARNING("Суперпользователь уже существует"))
