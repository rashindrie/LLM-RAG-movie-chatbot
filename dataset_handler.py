# Import the Movies Data
import pandas as pd

"""
Read the dataset and perform basic pre-processing.
"""
def read_data(dataset_file_path):
    # Read the dataset
    movies_raw = pd.read_csv(dataset_file_path)

    # Rename primaryTitle, Description columns. Assign to movies.
    movies = movies_raw.rename(columns = {
        "primaryTitle": "movie_title",
        "Description" : "movie_description"
    })

    # Add source column from tconst
    movies["source"] = "https://www.imdb.com/title/" + movies["tconst"]

    # Subset for titleType equal to "movie"
    # Select movie_title, movie_description, source, genres columns
    movies = movies.loc[
        movies["titleType"] == "movie",
        ["movie_title", "movie_description", "source", "genres"]
    ]

    return movies
