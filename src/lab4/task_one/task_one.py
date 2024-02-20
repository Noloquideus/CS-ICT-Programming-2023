from accessify import private
from typing import List, Tuple


class MovieRecommendedService:

    def __init__(self):
        self.movies_file: str = "movies.txt"
        self.history_file: str = "history.txt"
        self.movies_list: List[str] = self.read_movies()
        self.history_list: List[List[int]] = self.read_history()

    @private
    def read_movies(self) -> List[str]:
        """
        Read the movies from the specified file, extract the movie names, and return a list of movie names.
        """
        with open(self.movies_file, 'r') as file:
            lines = file.readlines()
        movies_list = [line.strip().split(',', 1)[1] for line in lines]
        print(f"Прочитанные фильмы из файла {self.movies_file}:", movies_list)
        return movies_list

    @private
    def read_history(self) -> List[List[int]]:
        """
        Read the history from the specified file and return it as a list of lists of integers.
        """
        with open(self.history_file, 'r') as file:
            lines = file.readlines()
        history_list = [list(map(int, line.strip().split(','))) for line in lines]
        print(f"Прочитанные истории из файла {self.history_file}:", history_list)
        return history_list

    def recommend(self, user_history_input: str) -> str:
        """
         A function that takes user's history input, processes it, and recommends a movie to watch based on user preferences.

         Args:
             user_history_input (str): A string of comma-separated user history of watched movies.

         Returns:
             str: The recommended movie for the user to watch.
         """
        user_history: List[int] = list(map(int, user_history_input.split(',')))

        # Select users with at least half of the matching movies
        matching_users: List[Tuple[int, List[int]]] = []
        for i, history in enumerate(self.history_list):
            common_movies = set(history) & set(user_history)
            similarity = len(common_movies) / len(user_history)
            if similarity >= 0.5:
                matching_users.append((i + 1, history))  # Add the user ID and history

        # Excluding movies that the user has already watched
        filtered_users: List[Tuple[int, List[int]]] = []
        for user_id, history in matching_users:
            filtered_history = [movie for movie in history if movie not in user_history]
            filtered_users.append((user_id, filtered_history))

        # Counting the total number of views for each movie
        movie_views_count: dict = {}
        for user_id, filtered_history in filtered_users:
            for movie in filtered_history:
                movie_views_count[movie] = movie_views_count.get(movie, 0) + 1

        # Select the movie with the maximum number of views
        recommended_movie_id: int = max(movie_views_count, key=movie_views_count.get)
        recommended_movie: str = self.movies_list[recommended_movie_id - 1]

        print(f"\nРекомендуем вам посмотреть: {recommended_movie}")
        return recommended_movie
