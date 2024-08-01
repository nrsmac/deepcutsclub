"""Collection information."""

from deepcuts_api.schemas import Album

my_collection = [
    Album(artist_name=artist_name, title=title)
    for title, artist_name in [  # pragma: no cover
        ("To Pimp A Butterfly", "Kendrick Lamar"),
        ("Cosmogramma", "Flying Lotus"),
        ("Kid A", "Radiohead"),
        ("Endtroducing.....", "DJ Shadow"),
        ("The College Dropout", "Kanye West"),
        ("The Chronic", "Dr. Dre"),
        ("The Marshall Mathers LP", "Eminem"),
        ("The Miseducation of Lauryn Hill", "Lauryn Hill"),
        ("Tread", "Ross From Friends"),
        ("Turn On The Bright Lights", "Interpol"),
        ("Either / Or", "Elliott Smith"),
        ("Kid A", "Radiohead"),
        ("Capacity", "Big Thief"),
        ("The Idler Wheel...", "Fiona Apple"),
        ("The ArchAndroid", "Janelle Monáe"),
        ("Dragon New Warm Mountain I Believe In You", "Big Thief"),
        ("The Suburbs", "Arcade Fire"),
        ("Jassbusters", "Connann Mockasin"),
        ("Bravado", "Kirin J Callinan"),
        ("Con Todo El Mundo", "Khruangbin"),
        ("Donuts", "J Dilla"),
        ("It Is What It Is", "Thundercat"),
        ("Homogenic", "Björk"),
        ("Voodoo", "D'Angelo"),
        ("Fatigue", "L'Rain"),
        ("Grinning Cat", "Susumu Yokota"),
        ("Metaphorical Music", "Nujabes"),
        ("Modal Soul", "Nujabes"),
        ("Spiritual State", "Nujabes"),
        ("BRAT", "Charlie XCX"),
    ]
]
