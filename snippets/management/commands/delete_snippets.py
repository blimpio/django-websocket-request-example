from django.core.management.base import BaseCommand

from snippets.models import Snippet


class Command(BaseCommand):
    def handle(self, *args, **options):
        Snippet.objects.all().delete()
