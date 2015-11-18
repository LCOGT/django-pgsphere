from django.test import TestCase
from .models import SBox, SPoint


class SboxTestCase(TestCase):
    def setUp(self):
        self.a = SBox.objects.create(area=((0, 0), (5, 5)))
        self.b = SBox.objects.create(area=((140, -80), (150, -70)))
        self.wrapping_area = SBox.objects.create(area=((340, -20), (10, 20)))
        self.pole_area = SBox.objects.create(area=((150, 90), (0, 80)))

    def test_units(self):
        self.assertAlmostEqual(self.a.area[0][0], 0.0)
        self.assertAlmostEqual(self.a.area[0][1], 0.0)
        self.assertAlmostEqual(self.a.area[1][0], 5.0)
        self.assertAlmostEqual(self.a.area[1][1], 5.0)
        self.assertAlmostEqual(self.b.area[0][0], 140.0)
        self.assertAlmostEqual(self.b.area[0][1], -80.0)
        self.assertAlmostEqual(self.b.area[1][0], 150.0)
        self.assertAlmostEqual(self.b.area[1][1], -70.0)

    def test_contains(self):
        self.assertIn(
            self.a,
            SBox.objects.filter(area__contains=(1, 1))
        )
        self.assertIn(
            self.b,
            SBox.objects.filter(area__contains=(145, -75))
        )

    def test_wrapping(self):
        self.assertIn(
            self.wrapping_area,
            SBox.objects.filter(area__contains=(350, -10))
        )
        self.assertIn(
            self.wrapping_area,
            SBox.objects.filter(area__contains=(5, 10))
        )

    def test_poles(self):
        self.assertEqual(
            self.pole_area,
            SBox.objects.get(area__contains=(140, 85))
        )


class SpointTestCase(TestCase):
    def setUp(self):
        self.a = SPoint.objects.create(location=(20, 30))
        self.b = SPoint.objects.create(location=(30, -40))
        self.edge_point = SPoint.objects.create(location=(359, 20))
        self.pole_point = SPoint.objects.create(location=(10, 90))

    def test_units(self):
        self.assertAlmostEqual(self.a.location[0], 20.0)
        self.assertAlmostEqual(self.a.location[1], 30.0)
        self.assertAlmostEqual(self.b.location[0], 30.0)
        self.assertAlmostEqual(self.b.location[1], -40.0)

    def test_inradius(self):
        self.assertIn(
            self.a,
            SPoint.objects.filter(location__inradius=((20, 30), 10))
        )
        self.assertIn(
            self.b,
            SPoint.objects.filter(location__inradius=((35, -45), 10))
        )

    def test_wrapping(self):
        self.assertIn(
            self.edge_point,
            SPoint.objects.filter(location__inradius=((5, 20), 10))
        )

    def test_poles(self):
        self.assertIn(
            self.pole_point,
            SPoint.objects.filter(location__inradius=((120, 85), 10))
        )
