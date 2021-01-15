from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command create Amenities."

    """ def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times you can help me?") """

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Dedicated workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check_in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
            "Piano",
            "Beachfront",
            "Waterfront",
        ]
        for item in amenities:
            Amenity.objects.create(name=item)
        self.stdout.write(self.style.SUCCESS("Amenities created."))
