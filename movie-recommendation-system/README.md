# Movie Recommendation System

## Overview
The Movie Recommendation System is a project designed to recommend movies to users based on their ratings on the Letterboxd platform. By utilizing user data and advanced recommendation algorithms, the system aims to provide personalized movie suggestions.

## Project Structure
```
movie-recommendation-system
├── src
│   ├── data
│   │   ├── data_loader.py
│   │   └── preprocessor.py
│   ├── models
│   │   ├── recommender.py
│   │   └── utils.py
│   ├── scraper
│   │   └── letterboxd_scraper.py
│   └── config.py
├── tests
│   ├── test_data_loader.py
│   ├── test_preprocessor.py
│   └── test_recommender.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd movie-recommendation-system
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Load the data using the `load_data()` function from `data_loader.py`.
2. Preprocess the data with the `preprocess_data(data)` function from `preprocessor.py`.
3. Train the recommendation model using the `Recommender` class from `recommender.py`.
4. Generate movie recommendations for a user by calling the `recommend(user_id, num_recommendations)` method.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License
This project is licensed under the MIT License.