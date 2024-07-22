import spacy
import wikipediaapi

# Load the English NER model from spaCy
nlp = spacy.load("en_core_web_sm")


def fetch_wikipedia_content(artist_name):
    wiki_api = wikipediaapi.Wikipedia(
        language="en", user_agent="DeepCutsClub (noahrschill@gmail.com)"
    )
    page = wiki_api.page(artist_name)
    if not page.exists():
        return None
    return page.text


def extract_entities(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PERSON", "FAC"]:  # Filter relevant entity types
            entities.append((ent.text, ent.label_))
    return entities


def classify_entities(entities):
    classified_entities = {"PERSON": [], "ORG": [], "FAC": []}
    for entity, label in entities:
        classified_entities[label].append(entity)
    return classified_entities


def main(artist_name):
    # Fetch content from Wikipedia
    content = fetch_wikipedia_content(artist_name)
    if not content:
        print(f"Page '{artist_name}' does not exist on Wikipedia.")
        return

    # Extract entities using spaCy NER
    entities = extract_entities(content)

    # Classify entities into PERSON, ORG, FAC
    classified_entities = classify_entities(entities)

    # Print the classified entities
    print(f"PERSONS: {classified_entities['PERSON']}")
    print(f"ORGANIZATIONS: {classified_entities['ORG']}")
    print(f"FACILITIES: {classified_entities['FAC']}")


if __name__ == "__main__":
    artist_name = input("Enter the name of the music artist (as on Wikipedia): ")
    main(artist_name)
