import unittest
import pandas as pd
from src.data.data_loader import load_data

class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        # Test if the data is loaded correctly
        data = load_data()
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()