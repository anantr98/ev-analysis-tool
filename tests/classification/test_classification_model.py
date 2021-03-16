

import unittest
import numpy as np
from classification_model import build_knn_model
from classification_model import recommended_EV
from classification_model import get_EV_stats


class TestClassification(unittest.TestCase):

    def test_knn_model(self):
        self.assertEqual(build_knn_model(['7', 1, 2, 0]),['12'])
        self.assertIsNot(build_knn_model(['7', 1, 2, 0]),['12'])
        self.assertEqual(build_knn_model(['5', 1, 2, 0]),['1'])
        self.assertIsInstance(recommended_EV(['7', 1, 2, 0]), object)
        self.assertNotIsInstance(recommended_EV(['7', 1, 2, 0][0]), int)
        self.assertIsInstance(recommended_EV(['7', 1, 2, 0][0]), str)

    def test_recommended_EV(self):
            self.assertEqual(recommended_EV(['12']),'BMW i4 ')
            self.assertIsNot(recommended_EV(['12']),'Tesla Model 3')
            self.assertEqual(recommended_EV(['1']),'Audi Q4 Sportback e-tron ')
            self.assertNotIsInstance(recommended_EV(['1']), int)
            self.assertIsInstance(recommended_EV(['1']), str)

    def test_get_EV_stats(self):
        stats_BMW = [13,'BMW ','i4 ',4.0,178,'650','Yes','RWD','Type 2 CCS','Sedan','D',5,'BMW i4 ',124.0,280.0,78000.0]
        stats_Audi = [76,'Audi ','Q4 Sportback e-tron ',6.3,188,'550','Yes','AWD','Type 2 CCS','SUV','D',5,'Audi Q4 Sportback e-tron ',112.0,255.0,69000.0]
        self.assertEqual(get_EV_stats('BMW i4 '),stats_BMW)
        self.assertIsInstance(get_EV_stats('BMW i4 '),list)
        self.assertNotIsInstance(get_EV_stats('BMW i4 '),str)
        self.assertNotIsInstance(get_EV_stats('BMW i4 '),int)
        self.assertEqual(get_EV_stats('BMW i4 '),stats_BMW)
        self.assertEqual(get_EV_stats('Audi Q4 Sportback e-tron '),stats_Audi)

if __name__ == '__main__':
    unittest.main()
