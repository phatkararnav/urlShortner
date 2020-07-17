from django.core.management.base import BaseCommand, CommandError

from shortner.models import arnURL

class Command(BaseCommand):
    help = 'Refreshes all the shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int) 

    def handle(self, *args, **options):
        return arnURL.objects.refresh_shortcodes(items=options['items'])

