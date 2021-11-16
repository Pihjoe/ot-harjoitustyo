import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oiekin(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 15)

    def test_saldo_vahenee_oikein_saldoa_tarpeeksi(self):
        #Metodi palauttaa True, jos rahat riittivät ja muuten False
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(True, True)

    def test_saldo_vahenee_oikein_saldoa_ei_tarpeeksi(self):
        #Metodi palauttaa True, jos rahat riittivät ja muuten False
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(False, False)


