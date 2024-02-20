import unittest
from src.lab4.task_one.task_one import MovieRecommendedService


class TestMovieRecommendedService(unittest.TestCase):
    def setUp(self):
        self.service = MovieRecommendedService()

    def test_read_movie(self):
        predict = ['Inception', 'The Shawshank Redemption', 'The Godfather', 'Pulp Fiction', 'The Dark Knight',
                   "Schindler's List", 'Forrest Gump', 'Fight Club', 'The Matrix',
                   'The Lord of the Rings: The Return of the King']
        with open("movies.txt", 'r') as file:
            lines = file.readlines()
        movies_list = [line.strip().split(',', 1)[1] for line in lines]
        self.assertListEqual(predict, movies_list)

    def test_read_history(self):
        predict = [[6, 9, 2], [5, 10, 9], [1, 8, 5, 10, 6, 7, 9, 4, 2, 3], [5, 9], [4, 6]]
        with open("history.txt", 'r') as file:
            lines = file.readlines()
        history_list = [list(map(int, line.strip().split(','))) for line in lines]
        self.assertListEqual(predict, history_list)

    def test_recommend(self):
        user_history = "6,9,2"
        answer = "Inception"
        recommendation = self.service.recommend(user_history)
        self.assertEqual(answer, recommendation)
