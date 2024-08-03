from pprint import pprint

import deepcuts_sdk
import streamlit as st
from deepcuts_sdk.exceptions import ApiException
from deepcuts_sdk.models.album import Album
from streamlit_image_select import image_select

st.set_page_config(
    page_title="DeepCuts",
    page_icon="🎵",
)


@st.cache_resource(show_spinner="Searching for albums...")
def search_for_albums_by_artist(artist: str):
    configuration = deepcuts_sdk.Configuration(host="http://localhost:8000")
    with deepcuts_sdk.ApiClient(configuration) as api_client:
        api_instance = deepcuts_sdk.DeepcutsApi(api_client)

        try:
            api_response = api_instance.deepcuts_get_albums_by_artist(artist)
            print("The response of DeepcutsApi->deepcuts_get_albums_by_artist:\n")
            pprint(api_response)
            if api_response.albums:
                return api_response.albums
            raise ValueError(f"No albums found for artist {artist}.")
        except ApiException as e:
            print(f"Exception when calling DeepcutsApi->deepcuts_get_albums_by_artist: {e}\n")


# @st.cache_data(show_spinner="Finding more deep cuts...")
def recommend_albums():
    configuration = deepcuts_sdk.Configuration(host="http://localhost:8000")
    with deepcuts_sdk.ApiClient(configuration) as api_client:
        api_instance = deepcuts_sdk.DeepcutsApi(api_client)

        try:
            api_response = api_instance.deepcuts_recommend_albums_from_albums(
                {
                    "album_titles": [album.title for album in get_collection()],
                    "artist_names": [album.artist_name for album in get_collection()],
                }
            )
            print("The response of DeepcutsApi->deepcuts_recommend_album:\n")
            pprint(api_response)
            if api_response.albums:
                return api_response.albums
            raise ValueError("No album found for recommendation.")
        except ApiException as e:
            print(f"Exception when calling DeepcutsApi->deepcuts_recommend_album: {e}\n")


def add_album_to_collection(album: Album):
    if album not in get_collection():
        st.session_state.collection.append(album)


def get_collection():
    return st.session_state.collection


# Initialize session state for collection if it doesn't exist
if "collection" not in st.session_state:
    st.session_state.collection = []


# Initialize session state for collection if it doesn't exist
if "collection" not in st.session_state:
    st.session_state.collection = []


def search_container():
    st.write("Welcome to your music home -- discover connections and explore new music!")
    st.write("Start by searching for an artist you like.")

    if artist := st.text_input("Search for an artist:"):
        album_results = [album for album in search_for_albums_by_artist(artist) if album not in get_collection()]
        albums_by_image_url = {album.image_url: album for album in album_results}

        if album_results:
            selected_image = image_select(
                "Select an album to add to your collection:",
                images=[album.image_url for album in album_results],
                captions=[album.title for album in album_results],
                use_container_width=False,
            )

            selected_album = albums_by_image_url.get(selected_image)

            select_button = st.button(f"Add {selected_album.title} to your collection")

            if select_button:
                add_album_to_collection(selected_album)
                st.rerun()


if "main_view" not in st.session_state:
    st.session_state.main_view = "search"


def app():
    """
    Streamlit app for discovering and exploring new music albums.
    Allows users to search for albums and add them to their collection.
    """

    st.title("DeepCuts")

    with st.sidebar:
        st.write(f"{len(get_collection())} records in your collection:")
        body = "\n".join([f"- **{album.title}** by {album.artist_name}" for album in get_collection()])
        st.markdown(body)

        can_recommend = len(get_collection()) >= 3
        if st.button("More Deep Cuts", disabled=not can_recommend):
            st.session_state.main_view = "recommend"

        if st.button("Clear collection", disabled=len(get_collection()) == 0):
            st.session_state.collection = []
            st.rerun()

    match st.session_state.main_view:
        case "search":
            search_container()

        case "recommend":
            recommendations = recommend_albums()
            # for album in recommendations:
            # Display album images next to their information in a grid

            if st.button("Go back to Search"):
                st.session_state.main_view = "search"
                st.rerun()

            for i, album in enumerate(recommendations):
                i *= 4
                with st.container():
                    for j, col in enumerate(st.columns(4)):
                        try:
                            album = recommendations[i + j]
                            col.image(album.image_url, width=150)
                            if col.button("Add to collection", key=album.spotify_url, type="secondary"):
                                add_album_to_collection(album)
                                recommendations.remove(album)
                                st.rerun()
                            col.link_button(url=album.spotify_url, label="Listen on Spotify")
                            col.markdown(f"**{album.title}** by {album.artist_name}")
                        except IndexError:
                            break
                # st.image(album.image_url, caption=f"{album.title} by {album.artist_name}", use_column_width=True)


if __name__ == "__main__":
    app()
