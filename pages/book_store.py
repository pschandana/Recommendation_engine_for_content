# import streamlit as st
# from utils import get_similar_books

# st.title("📚 Book Store - Find Similar Books")

# book_name = st.text_input("Enter a book title:")

# if st.button("Find Recommendations"):
#     try:
#         recommendations = get_similar_books(book_name)
#         st.subheader(f"Books similar to '{book_name}':")
#         for title, score in recommendations:
#             st.write(f"📖 {title} (Similarity: {1 - score:.2f})")
#     except KeyError:
#          st.error("Book not found. Please check the title and try again.")
import streamlit as st
from utils import get_similar_books

# Set page config if needed
# st.set_page_config(page_title="Book Store", layout="wide")

# Function to set a background image via CSS
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            filter: brightness(0.85);
        }}
        .stApp::before {{
            content: "";
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.4);
            z-index: 0;
        }}
        .main {{
            position: relative;
            z-index: 1;
            color: #fff;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# URL of the background image you’d like to use
background_url = "https://images8.alphacoders.com/411/thumb-1920-411522.jpg"
set_background(background_url)

# Main Application UI
st.title("📚 Book Store - Find Similar Books", anchor=None)
book_name = st.text_input("Enter a book title:")

if st.button("Find Recommendations"):
    try:
        recommendations = get_similar_books(book_name)
        st.subheader(f"Books similar to '{book_name}':")
        for title, score in recommendations:
            st.write(f"📖 {title} (Similarity: {1 - score:.2f})")
    except KeyError:
        st.error("Book not found. Please check the title and try again.")

