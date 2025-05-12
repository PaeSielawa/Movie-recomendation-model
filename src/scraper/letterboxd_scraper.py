import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Dict, List
from time import sleep


class LetterboxdScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        self.base_url = "https://letterboxd.com"

    def get_user_ratings(self, username: str) -> pd.DataFrame:
        """
        Scrapes movie ratings for a given Letterboxd user.
        
        Args:
            username (str): Letterboxd username
            
        Returns:
            pd.DataFrame: DataFrame with columns [movie_id, movie_title, rating, date]
        """
        ratings: List[Dict] = []
        page = 1
        
        while True:
            try:
                # Construct URL for current page
                url = f"{self.base_url}/{username}/films/page/{page}/"
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()
                
                # Parse the page
                soup = BeautifulSoup(response.text, 'html.parser')
                films = soup.select('li.poster-container')
                
                if not films:
                    break
                    
                # Process each film on the page
                for film in films:
                    try:
                        # Get movie info from poster
                        poster = film.select_one('div.film-poster')
                        if not poster:
                            continue
                            
                        movie_id = poster.get('data-film-slug', '').strip('/')
                        movie_title = poster.select_one('img').get('alt')
                        
                        # Get rating from viewing data
                        rating_elem = film.select_one('span.rating.-micro')
                        rating = None
                        if rating_elem:
                            rated_class = next(
                                (c for c in rating_elem['class'] if c.startswith('rated-')), 
                                None
                            )
                            if rated_class:
                                rating = float(rated_class.replace('rated-', '')) / 2
                        
                        if movie_id and movie_title:
                            ratings.append({
                                'movie_id': movie_id,
                                'movie_title': movie_title,
                                'rating': rating,
                                'date': None  # TODO: Add date parsing
                            })
                            
                    except Exception as e:
                        print(f"Error processing film: {e}")
                        continue
                
                print(f"Page {page}: Found {len(films)} films")
                page += 1
                sleep(1)  # Be nice to the server
                
            except requests.exceptions.RequestException as e:
                print(f"Error fetching page {page}: {e}")
                break
                
        return pd.DataFrame(ratings)