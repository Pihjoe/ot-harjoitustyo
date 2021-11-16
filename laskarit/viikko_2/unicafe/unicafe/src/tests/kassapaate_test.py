import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(400)

    def test_alustettu_kassapaate_oikein_ja_myydyt_oikein(self):
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_osto_onnistuu_kateisella(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertAlmostEqual(vaihtoraha, 60)
        self.assertAlmostEqual(self.kassapaate.edulliset, 1)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_osto_ei_onnistu_vajaalla_kateisella(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertAlmostEqual(vaihtoraha, 200)
        self.assertAlmostEqual(self.kassapaate.edulliset, 0)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_osto_onnistuu_kateisella(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertAlmostEqual(vaihtoraha, 100)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 1)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukas_osto_ei_onnistu_vajaalla_kateisella(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertAlmostEqual(vaihtoraha, 200)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 0)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_osto_onnistuu_kortilla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(vaihtoraha)
        self.assertAlmostEqual(self.kassapaate.edulliset, 1)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.maksukortti.saldo, 160)
    
    def test_maukas_osto_onnistuu_kortilla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(vaihtoraha)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 1)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.maksukortti.saldo, 0)

    def test_edullinen_osto_ei_onnistu_vajaalla_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        vaihtoraha = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertFalse(vaihtoraha)
        self.assertAlmostEqual(self.kassapaate.edulliset, 1)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.maksukortti.saldo, 160)
    
    def test_maukas_osto_ei_onnistu_vajaalla_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        vaihtoraha = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(vaihtoraha)
        self.assertAlmostEqual(self.kassapaate.maukkaat, 1)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.maksukortti.saldo, 0)

    def test_kortille_voi_ladata_rahaa_ja_kassapaate_paivittyy(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 600)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100600)
        self.assertAlmostEqual(self.maksukortti.saldo, 1000)

    def test_kortille_ei_voi_ladata_negatiivista_rahaa_ja_kassapaate_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -600)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertAlmostEqual(self.maksukortti.saldo, 400)
    
    





    
    #Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000 euroa, lounaita myyty 0)
        #huomaa, että luokka tallentaa rahamäärän sentteinä
    #Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
        #Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
        #Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
        #Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta
    #seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan oikein
    #Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
        #Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
        #Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
        #Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
        #Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    #Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
