def test_preprocess_data():
    import pandas as pd
    from src.data.preprocessor import preprocess_data

    # Sample data for testing
    sample_data = pd.DataFrame({
        'user_id': [1, 2, 1, 2],
        'movie_id': [101, 102, 103, 104],
        'rating': [5, 4, 3, 2]
    })

    # Preprocess the sample data
    processed_data = preprocess_data(sample_data)

    # Assertions to verify the preprocessing
    assert not processed_data.isnull().values.any(), "Data contains null values after preprocessing"
    assert processed_data.shape[0] == sample_data.shape[0], "Number of rows should remain the same after preprocessing"
    assert 'user_id' in processed_data.columns, "Processed data should contain 'user_id' column"
    assert 'movie_id' in processed_data.columns, "Processed data should contain 'movie_id' column"
    assert 'rating' in processed_data.columns, "Processed data should contain 'rating' column"