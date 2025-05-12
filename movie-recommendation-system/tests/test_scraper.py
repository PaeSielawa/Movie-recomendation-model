import unittest
import pandas as pd
from src.scraper.letterboxd_scraper import LetterboxdScraper


class TestLetterboxdScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = LetterboxdScraper()
    
    def test_get_user_ratings_structure(self):
        """Test if the returned DataFrame has correct structure"""
        username = 'paesielawa'
        df = self.scraper.get_user_ratings(username)
        
        # Check if we got a DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        
        # Check if required columns are present
        required_columns = ['movie_id', 'movie_title', 'rating', 'date']
        for column in required_columns:
            self.assertIn(column, df.columns)
    
    def test_rating_values(self):
        """Test if ratings are within valid range"""
        username = 'paesielawa'
        df = self.scraper.get_user_ratings(username)
        
        # Check if there are any ratings
        self.assertTrue(len(df) > 0)
        
        # Check if ratings are within 0.5-5.0 range
        ratings = df['rating'].dropna()
        self.assertTrue(all(ratings.between(0.5, 5.0)))
    
    def test_invalid_username(self):
        """Test handling of invalid username"""
        username = 'this_user_definitely_does_not_exist_123456789'
        
        with self.assertRaises(Exception):
            self.scraper.get_user_ratings(username)


if __name__ == '__main__':
    unittest.main()