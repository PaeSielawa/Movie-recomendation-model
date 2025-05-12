import unittest
from src.models.recommender import Recommender

class TestRecommender(unittest.TestCase):

    def setUp(self):
        self.recommender = Recommender()
        self.sample_data = {
            'user_id': [1, 2, 3],
            'movie_id': [101, 102, 103],
            'rating': [5, 4, 3]
        }
        self.recommender.fit(self.sample_data)

    def test_recommend(self):
        recommendations = self.recommender.recommend(user_id=1, num_recommendations=2)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

    def test_fit(self):
        self.assertIsNotNone(self.recommender.model)

if __name__ == '__main__':
    unittest.main()