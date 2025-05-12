import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

def scrape_user_ratings(username):
    """
    Scrapes movie ratings for a specific Letterboxd user.
    
    Parameters:
        username (str): Letterboxd username
    
    Returns:
        pd.DataFrame: DataFrame with columns [movie_id, movie_title, rating, date]
    """
    base_url = f"https://letterboxd.com/{username}/films/rated/"
    ratings = []
    page = 1
    
    while True:
        url = f"{base_url}page/{page}/"
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all('div', class_='film-detail')
        
        if not movies:
            break
        
        for movie in movies:
            movie_id = movie['data-film-id']
            movie_title = movie.find('a', class_='film-title').text.strip()
            rating = movie.find('span', class_='rating').text.strip()
            date = movie.find('span', class_='date').text.strip()
            ratings.append([movie_id, movie_title, rating, date])
        
        page += 1
        sleep(1)
        
    return pd.DataFrame(ratings, columns=['movie_id', 'movie_title', 'rating', 'date'])
