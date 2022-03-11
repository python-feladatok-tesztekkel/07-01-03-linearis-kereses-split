from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestBukasok(TestCase):
    def test_feladat01(self):
        adat=""
        aktualis = feladatok.bukott_e(adat)
        elvart = None
        self.assertEqual(elvart, aktualis, "Üres adatok esetén nem None értékkel tért vissza")
    def test_feladat02(self):
        adat="5, 3, 3, 4, 5, 2, 3, 4, 5"
        aktualis = feladatok.bukott_e(adat)
        elvart = False
        self.assertEqual(elvart, aktualis, "Helytelenül határozta meg, hogy a diák bukott-e")
    def test_feladat03(self):
        adat="5, 3, 3, 4, 5, 2, 3, 4, 1"
        aktualis = feladatok.bukott_e(adat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Helytelenül határozta meg, hogy a diák bukott-e")
    def test_feladat04(self):
        adat="5, 1, 3, 4, 5, 2, 3, 4, 1"
        aktualis = feladatok.bukott_e(adat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Helytelenül határozta meg, hogy a diák bukott-e")
    def test_feladat05(self):
        adat="1, 1, 1, 1, 1, 1, 1, 1, 1"
        aktualis = feladatok.bukott_e(adat)
        elvart = True
        self.assertEqual(elvart, aktualis, "Helytelenül határozta meg, hogy a diák bukott-e")