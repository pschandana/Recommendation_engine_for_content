import hashlib
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# ===== Password Utilities =====
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password


# ===== KNN Book Recommendation =====
# File paths (update to your actual location)
books_filename = "dataset/BX-Books.csv"
ratings_filename = "dataset/BX-Book-Ratings.csv"

# Load datasets once
df_books = pd.read_csv(
    books_filename,
    encoding="ISO-8859-1",
    sep=";",
    usecols=['ISBN', 'Book-Title', 'Book-Author'],
    dtype={'ISBN': 'str', 'Book-Title': 'str', 'Book-Author': 'str'}
)
df_books.rename(columns={
    'ISBN': 'isbn',
    'Book-Title': 'title',
    'Book-Author': 'author'
}, inplace=True)

df_ratings = pd.read_csv(
    ratings_filename,
    encoding="ISO-8859-1",
    sep=";",
    usecols=['User-ID', 'ISBN', 'Book-Rating'],
    dtype={'User-ID': 'int32', 'ISBN': 'str', 'Book-Rating': 'float32'}
)
df_ratings.rename(columns={
    'User-ID': 'user',
    'ISBN': 'isbn',
    'Book-Rating': 'rating'
}, inplace=True)
# Filter low-activity users/books
filter_1 = df_ratings['user'].value_counts()
filter_2 = df_ratings['isbn'].value_counts()
df_ratings = df_ratings[
    ~df_ratings['user'].isin(filter_1[filter_1 < 200].index) &
    ~df_ratings['isbn'].isin(filter_2[filter_2 < 100].index)
]

# Create pivot table
df_table = df_ratings.pivot_table(index='isbn', columns='user', values='rating').fillna(0)
df_table.index = df_table.join(df_books.set_index('isbn'))['title']

# Train KNN once
knn_model = NearestNeighbors(n_neighbors=6, metric="cosine")
knn_model.fit(df_table.values)

def get_similar_books(book_title):
    """
    Return a list of (title, distance) for books similar to the given title.
    """
    

    if book_title not in df_table.index:
        raise KeyError(f"Book '{book_title}' not found in dataset.")

    distances, indices = knn_model.kneighbors(
        # [df_table.loc[book_title].values],
        df_table.loc[book_title].values.reshape(1, -1),

        n_neighbors=6
    )

    recommendations = []
    for i in range(1, 6):  # Skip the first (it’s the same book)
        title = df_table.index[indices[0][i]]
        distance = distances[0][i]
        recommendations.append((title, distance))

    return recommendations
#Where the Heart Is (Oprah's Book Club (Paperback))
#I'll Be Seeing You"(47-50), 'The Weight of Water', 'The Surgeon', 'I Know This Much Is True,Isle of Dogs
#The Joy Luck Club--69

# import hashlib
# import pandas as pd
# from sklearn.neighbors import NearestNeighbors
# import streamlit as st

# # ===== Password Utilities =====
# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# def verify_password(password, hashed_password):
#     return hash_password(password) == hashed_password


# # ===== Cached Model & Data =====
# @st.cache_resource
# def load_model_and_data():
#     books_filename = "dataset/BX-Books.csv"
#     ratings_filename = "dataset/BX-Book-Ratings.csv"

#     # Load books
#     df_books = pd.read_csv(
#         books_filename,
#         encoding="ISO-8859-1",
#         sep=";",
#         usecols=['ISBN', 'Book-Title', 'Book-Author'],
#         dtype={'ISBN': 'str', 'Book-Title': 'str', 'Book-Author': 'str'}
#     ).rename(columns={
#         'ISBN': 'isbn',
#         'Book-Title': 'title',
#         'Book-Author': 'author'
#     })

#     # Load ratings
#     df_ratings = pd.read_csv(
#         ratings_filename,
#         encoding="ISO-8859-1",
#         sep=";",
#         usecols=['User-ID', 'ISBN', 'Book-Rating'],
#         dtype={'User-ID': 'int32', 'ISBN': 'str', 'Book-Rating': 'float32'}
#     ).rename(columns={
#         'User-ID': 'user',
#         'ISBN': 'isbn',
#         'Book-Rating': 'rating'
#     })

#     # Filter low activity
#     filter_1 = df_ratings['user'].value_counts()
#     filter_2 = df_ratings['isbn'].value_counts()
#     df_ratings = df_ratings[
#         ~df_ratings['user'].isin(filter_1[filter_1 < 200].index) &
#         ~df_ratings['isbn'].isin(filter_2[filter_2 < 100].index)
#     ]

#     # Pivot table
#     df_table = df_ratings.pivot_table(index='isbn', columns='user', values='rating').fillna(0)
#     df_table.index = df_table.join(df_books.set_index('isbn'))['title']

#     # Store the column order
#     train_columns = df_table.columns

#     # Train model
#     knn_model = NearestNeighbors(n_neighbors=6, metric="cosine")
#     knn_model.fit(df_table.values)

#     return knn_model, df_table, train_columns


# # Load once
# knn_model, df_table, train_columns = load_model_and_data()


# # ===== Recommendation Function =====
# def get_similar_books(book_title):
#     if book_title not in df_table.index:
#         raise KeyError(f"Book '{book_title}' not found in dataset.")

#     # Ensure column order is identical
#     book_vector = df_table.loc[book_title][train_columns].values.reshape(1, -1)

#     distances, indices = knn_model.kneighbors(book_vector, n_neighbors=6)

#     recommendations = []
#     for i in range(1, 6):  # skip itself
#         title = df_table.index[indices[0][i]]
#         distance = distances[0][i]
#         recommendations.append((title, distance))

#     return recommendations
