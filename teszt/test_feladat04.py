from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestFelvettDiakokAtlaga(TestCase):
    def test_feladat01(self):
        adat="70, 55, 70, 70, 69, 70"
        aktualis = feladatok.felvett_diakok_atlaga(adat)
        elvart = 70
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a felvett diákok átlagát")
    def test_feladat02(self):
        adat="71, 55, 66, 65, 69"
        aktualis = feladatok.felvett_diakok_atlaga(adat)
        elvart = 71
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a felvett diákok átlagát")
    def test_feladat03(self):
        adat="58, 55, 66, 65, 71"
        aktualis = feladatok.felvett_diakok_atlaga(adat)
        elvart = 71
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a felvett diákok átlagát")
    def test_feladat04(self):
        adat="98, 55, 86, 65, 71, 72, 56, 79, 68, 99, 66, 58, 71, 98, 70"
        aktualis = feladatok.felvett_diakok_atlaga(adat)
        elvart = 82.66666666666667
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg a felvett diákok átlagát")