from django.test import TestCase
from .models import SBox


class SboxTestCase(TestCase):
    def setUp(self):
        self.wrapping_area = SBox.objects.create(area=((340, -20), (10, 20)))
        self.a = SBox.objects.create(area=((0, 0), (5, 5)))
        self.b = SBox.objects.create(area=((140, -80), (150, -70)))

    def test_sbox_units(self):
        self.assertAlmostEqual(self.a.area[0][0], 0.0)
        self.assertAlmostEqual(self.a.area[0][1], 0.0)
        self.assertAlmostEqual(self.a.area[1][0], 5.0)
        self.assertAlmostEqual(self.a.area[1][1], 5.0)
        self.assertAlmostEqual(self.b.area[0][0], 140.0)
        self.assertAlmostEqual(self.b.area[0][1], -80.0)
        self.assertAlmostEqual(self.b.area[1][0], 150.0)
        self.assertAlmostEqual(self.b.area[1][1], -70.0)

    def test_sbox_contains(self):
        self.assertTrue(
            SBox.objects.filter(area__contains=(1, 1)).exists()
        )
        self.assertTrue(
            SBox.objects.filter(area__contains=(145, -75)).exists()
        )

    def test_wrapping(self):
        self.assertEqual(
            SBox.objects.get(area__contains=(350, -10)),
            self.wrapping_area
        )
        self.assertEqual(
            SBox.objects.get(area__contains=(5, 10)),
            self.wrapping_area
        )
