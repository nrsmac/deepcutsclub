import pickle

import streamlit as st
from streamlit_image_select import image_select

# Save selected albums into streamlit session state
# INitia


def home():
    st.title("DeepCuts")
    st.write("Welcome to your music home -- discover connections and explore new music!")


def my_albums():
    st.write("# My Albums:")

    with open("my_albums.pkl", "rb") as f:
        albums = pickle.load(f)

    # for album in albums:
    #     st.write(f"**{album.title}** by {album.artist_name}")
    #     st.image(album.image_url, use_column_width=True)
    #     st.write("---")

    img = image_select(
        "",
        [album.image_url for album in albums[:-1]],
        captions=[f"{album.title} \n by {album.artist_name}" for album in albums[:-1]],
        return_value="index",
    )


def app():
    """
    Streamlit app for discovering and exploring new music albums.
    Allows users to search for albums and add them to their collection.
    """

    st.sidebar.title("DeepCuts")

    page = st.sidebar.radio("Navigation", ["Home", "My Albums"])

    if page == "Home":
        home()
    elif page == "My Albums":
        my_albums()


if __name__ == "__main__":
    app()
