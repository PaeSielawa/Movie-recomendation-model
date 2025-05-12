def load_data():
    import pandas as pd

    # Load user ratings and movie data from Letterboxd
    user_ratings = pd.read_csv('path/to/user_ratings.csv')  # Update with actual path
    movie_data = pd.read_csv('path/to/movie_data.csv')      # Update with actual path

    # Merge or process data as needed
    dataset = pd.merge(user_ratings, movie_data, on='movie_id')

    return dataset