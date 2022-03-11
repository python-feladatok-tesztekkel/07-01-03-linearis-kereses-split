from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestLeghidegebbNap(TestCase):
    def test_feladat01(self):
        adat=""
        aktualis = feladatok.leghidegebb_nap_sorszama(adat)
        elvart = None
        self.assertEqual(elvart, aktualis, "Üres adatok esetén nem None értékkel tért vissza")
    def test_feladat02(self):
        adat="3, 2, 2, 0, -1, 3, 5"
        aktualis = feladatok.leghidegebb_nap_sorszama(adat)
        elvart = 5
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg, hogy melyik a leghidegebb nap sorszáma")
    def test_feladat03(self):
        adat="-3, 2, 2, 0, -1, 3, 5"
        aktualis = feladatok.leghidegebb_nap_sorszama(adat)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg, hogy melyik a leghidegebb nap sorszáma")
    def test_feladat04(self):
        adat="3, 2, 2, 0, -1, 3, -5"
        aktualis = feladatok.leghidegebb_nap_sorszama(adat)
        elvart = 7
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg, hogy melyik a leghidegebb nap sorszáma")