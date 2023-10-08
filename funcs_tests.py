import unittest
from funcs import *


# here is a sample puzzle for you to use in your tests
puzzle = ["WAQHGTTWEE",
          "CBMIVQQELS",
          "AZXWKWIIIL",
          "LDWLFXPIPV",
          "PONDTMVAMN",
          "OEDSOYQGOB",
          "LGQCKGMMCT",
          "YCSLOACUZM",
          "XVDMGSXCYZ",
          "UUIUNIXFNU"]
puzzle1=["EOARBRNIAB",
         "ZEBRAEBRBH",
         "ARRACCOONR",
         "AACBRRCHEC",
         "CNABOZOBKA",
         "BONIRBBNCA",
         "EERTCBRAIA",
         "ABCERICRHR",
         "BOIORORCCO",
         "BOAAKRKEAR"]

class TestCases(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

   def test_find_up0(self):
      words=['UZMT','XWQ','ABKD','LSE','DLWIH']
      self.assertListAlmostEqual(find_up(puzzle,words),['UZMT', 9, 9,'XWQ', 3, 5, 'LSE', 2, 9, 'DLWIH', 4, 3])
   def test_find_up1(self):
      words=['UXYL','LACW','XXCM','DLWIXCDGSH']
      self.assertListAlmostEqual(find_up(puzzle,words),['UXYL', 9, 0,'LACW', 3, 0, 'XXCM', 9, 6,])
   def test_find_up2(self):
      words=['AAZE','OOBE','EBOO','EZAA']
      self.assertListAlmostEqual(find_up(puzzle1,words),['AAZE', 3, 0,'OOBE', 9, 1,])

   def test_find_down0(self):
      words=['AAZE','OOBE','EBOO','EZAA']
      self.assertListAlmostEqual(find_down(puzzle1,words),['EBOO', 6, 1,'EZAA', 0, 0])
   def test_find_down1(self):
      words=['WAQH','NGOK','KOGN','SE','ES']
      self.assertListAlmostEqual(find_down(puzzle,words),['KOGN', 6, 4, 'ES', 0, 9])

   def test_find_forward0(self):
      words=['WAQH','WEE','PIPV','VPIP','EEW', 'BOG', 'UN']
      self.assertListAlmostEqual(find_forward(puzzle,words),['WAQH', 0, 0, 'WEE', 0, 7, 'PIPV', 3,6, 'UN', 9, 3])
   def test_find_forward0(self):
      words=['RBBN','nBBR','RCCO','RKAA','AAKR', 'UN', 'NU']
      self.assertListAlmostEqual(find_forward(puzzle1,words),['RBBN', 5, 4, 'RCCO', 8, 6, 'AAKR', 9,2])

   def test_find_backward0(self):#MUST PASS UNSTRCTURED PUZZLE
      words=['NBBR','OCCR','RKAA','AAKR', 'UN', 'NU']
      print(find_backward(puzzle1, words))
      self.assertListAlmostEqual(find_backward("EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR",words),\
                                                ['NBBR', 5, 7, 'OCCR', 8, 9, 'RKAA', 9, 5])
   def test_find_backward0(self):#MUST PASS UNSTRCTURED PUZZLE
      words=['SLEQ','AVMT','XINU','AAKR', 'UN', 'NU']
      self.assertListAlmostEqual(find_backward("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU",words),\
                                                ['SLEQ', 1, 9, 'AVMT', 4, 7, 'XINU', 9, 6, 'UN', 9, 9, 'NU', 9, 4])

   def test_find_diagonal_dr0(self):
      words=['WBXL','TEIV','TEIVT','XU','XUUUU', 'UYUUUU', 'UYU']
      self.assertListAlmostEqual(find_diagonal_dr(puzzle, words[0]),('WBXL', 0, 0))
   def test_find_diagonal_dr1(self):
      words=['WBXL','TEIV','TEIVT','XU','XUUUU', 'UYUUUU', 'UYU']
      self.assertListAlmostEqual(find_diagonal_dr(puzzle, words[1]),('TEIV', 0, 6))
   def test_find_diagonal_dr2(self):
      words=['WBXL','TEIV','TEIVT','XU','XUUUU', 'UYUUUU', 'UYU']
      self.assertEqual(find_diagonal_dr(puzzle, words[2]), None)#########################
   def test_find_diagonal_dr3(self):
      words=['WBXL','TEIV','TEIVT','XU','XUUUU', 'UYUUUU', 'UYU']
      self.assertListAlmostEqual(find_diagonal_dr(puzzle, words[3]),('XU', 8,0))
   def test_find_diagonal_dr4(self):
      words=['WBXL','TEIV','TEIVT','XU','XUUUU', 'UYUUUU', 'UYU']
      self.assertEqual(find_diagonal_dr(puzzle, words[4]), None)#####################
   def test_find_diagonal_dr5(self):
      words=['WBXL','TEIV','TEIVT','XU','XUUUU', 'UYUUUU', 'UYU']
      self.assertEqual(find_diagonal_dr(puzzle, words[5]),  None) ##########################
   def test_find_diagonal_dr6(self):
      words=['WBXL','TEIV','TEIVT','XU','XUUUU', 'UYUUUU', 'UYU']
      self.assertListAlmostEqual(find_diagonal_dr(puzzle, words[6]),('UYU', 7, 7 ))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

