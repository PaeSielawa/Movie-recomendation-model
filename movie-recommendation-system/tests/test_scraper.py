import unittest
import pandas as pd
from src.scraper.letterboxd_scraper import scrape_user_ratings

class TestLetterboxdScraper(unittest.TestCase):
    def test_scrape_single_user_ratings(self):
        """Test scraping ratings for a single user"""
        username = 'paesielawa'

        ratings = scrape_user_ratings(username)
        
        # Verify the structure of returned data
        self.assertIsInstance(ratings, pd.DataFrame)
        self.assertTrue(len(ratings) > 0)
        
        # Check if all required columns are present
        required_columns = ['movie_id', 'movie_title', 'rating', 'date']
        for column in required_columns:
            self.assertIn(column, ratings.columns)
        
        # Check if ratings are within valid range (0.5-5.0)
        self.assertTrue(all(ratings['rating'].astype(float).between(0.5, 5.0)))

    def test_scrape_multiple_users(self):
        """Test scraping ratings for multiple users"""
        usernames = ['paesielawa', 'kabarecik']
        all_ratings = []
        
        for username in usernames:
            user_ratings = scrape_user_ratings(username)
            user_ratings['user_id'] = username  # Add user_id column
            all_ratings.append(user_ratings)
        
        combined_ratings = pd.concat(all_ratings, ignore_index=True)
        
        # Verify the combined dataset
        self.assertIsInstance(combined_ratings, pd.DataFrame)
        self.assertTrue(len(combined_ratings) > 0)
        self.assertEqual(len(combined_ratings['user_id'].unique()), len(usernames))

    def test_invalid_username(self):
        """Test handling of invalid username"""
        invalid_username = 'this_user_definitely_does_not_exist_123456789'
        
        with self.assertRaises(Exception):
            scrape_user_ratings(invalid_username)

    def test_empty_ratings(self):
        """Test handling of user with no ratings"""
        # Replace with a known username that has no ratings
        empty_username = 'new_user_with_no_ratings'
        
        ratings = scrape_user_ratings(empty_username)
        self.assertEqual(len(ratings), 0)

if __name__ == '__main__':
    unittest.main()