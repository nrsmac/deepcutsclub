import spacy
import wikipediaapi

nlp = spacy.load("en_core_web_sm")


# Function to fetch Wikipedia content
def get_wikipedia_content(artist_name):
    wiki_wiki = wikipediaapi.Wikipedia("en")
    page = wiki_wiki.page(artist_name)

    if not page.exists():
        return None

    return page.text


def artist_link_with_spacy(link):
    doc = nlp(link)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return False


# Example function to extract links and classify them
def extract_links_and_labels(artist_name):
    wiki_api = wikipediaapi.Wikipedia(language="en", user_agent="DeepCutsClub (noahrschill@gmail.com)")
    page = wiki_api.page(artist_name)

    if not page.exists():
        return []

    # content = page.text
    links = page.links

    examples = []
    for link_name, url in links.items():
        if ":" not in link_name and "(" not in link_name and "|" not in link_name:
            if is_artist := artist_link_with_spacy(link_name):
                examples.append((link_name, url, is_artist))

    return examples


# Example main function
def main():
    artist_name = "Michael Jackson"
    examples = extract_links_and_labels(artist_name)

    if not examples:
        print(f"No related artists found for {artist_name} on Wikipedia.")
        return

    for link, _, is_artist in examples:
        if is_artist:
            print(f"{link} is likely an artist.")
        else:
            print(f"{link} is not likely an artist.")


if __name__ == "__main__":
    main()
