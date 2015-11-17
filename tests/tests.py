from django.test import TestCase
from .models import SBox


class SboxTestCase(TestCase):
    def setUp(self):
        SBox.objects.create(area=((0, 0), (5, 5)))
        SBox.objects.create(area=((340, -80), (360, -70)))

    def test_sbox_contains(self):
        self.assertTrue(
            SBox.objects.filter(area__contains=(1, 1)).exists()
        )
        self.assertTrue(
            SBox.objects.filter(area__contains=(350, -75)).exists()
        )
