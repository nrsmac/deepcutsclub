import wikipediaapi


def fetch_entities(artist_name):
    wiki_api = wikipediaapi.Wikipedia(
        language="en", user_agent="DeepCutsClub (noahrschill@gmail.com)"
    )
    page = wiki_api.page(artist_name)
    if not page.exists():
        print(f"Page '{artist_name}' does not exist on Wikipedia.")
        return

    entities = {
        "music_artists": [],
        "engineers": [],
        "venues": [],
        "other_entities": [],
    }

    # Extract links from the page
    links = page.links

    # Classify links into categories based on keywords
    for title, link in links.items():
        lowercase_title = title.lower()
        if "musician" in lowercase_title or "artist" in lowercase_title:
            entities["music_artists"].append(title)
        elif "engineer" in lowercase_title:
            entities["engineers"].append(title)
        elif "venue" in lowercase_title or "concert hall" in lowercase_title:
            entities["venues"].append(title)
        else:
            entities["other_entities"].append(title)

    return entities


def main(artist_name):
    entities = fetch_entities(artist_name)

    print(f"Music Artists: {entities['music_artists']}")
    print(f"Engineers: {entities['engineers']}")
    print(f"Venues: {entities['venues']}")
    print(f"Other Entities: {entities['other_entities']}")


if __name__ == "__main__":
    artist_name = input("Enter the name of the music artist (as on Wikipedia): ")
    main(artist_name)
