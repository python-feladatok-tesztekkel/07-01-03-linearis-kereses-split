from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsztondijasok(TestCase):
    def test_feladat01(self):
        adat=""
        aktualis = feladatok.osztondijasok_szama(adat)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Üres adatok esetén nem jól határozta meg az ösztöndijasok számát!")
    def test_feladat02(self):
        adat="3.70"
        aktualis = feladatok.osztondijasok_szama(adat)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az ösztöndijaok számát!")
    def test_feladat03(self):
        adat="3.69, 4.70, 4.71"
        aktualis = feladatok.osztondijasok_szama(adat)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az ösztöndijaok számát!")
    def test_feladat04(self):
        adat="1.12, 2.70, 4.70"
        aktualis = feladatok.osztondijasok_szama(adat)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az ösztöndijaok számát!")
    def test_feladat05(self):
        adat="4.70, 1.12, 2.70"
        aktualis = feladatok.osztondijasok_szama(adat)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az ösztöndijaok számát!")
    def test_feladat06(self):
        adat="4.70, 4.12, 4.89, 1.98, 5.00, 4.8, 4.55"
        aktualis = feladatok.osztondijasok_szama(adat)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg az ösztöndijaok számát!")