from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command create Facilities."

    """ def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times you can help me?") """

    def handle(self, *args, **options):
        facilities = [
            "Free parking on premises",
            "Elevator",
            "Gym",
            "Hot tub",
            "Pool",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
