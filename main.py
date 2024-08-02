from pathlib import Path
from typing import List, Optional

wordlists_dir = Path().resolve() / "wordlists"

# If you want explicit topics then comment out the next line and uncomment the lists of files you want
wordlist_filenames: Optional[List[str]] = None
# wordlist_filenames = [
#     "animes.txt",
#     "asterix.txt",
#     "athletes.txt",
#     "authors.txt",
#     "avatar_the_last_airbender.txt",
#     "cars.txt",
#     "cartoon_characters.txt",
#     "common_folklore.txt",
#     "common_heroes_and_villains.txt",
#     "companies.txt",
#     "disney_and_pixar_characters.txt",
#     "dreamworks_characters.txt",
#     "famous_people.txt",
#     "gods.txt",
#     "harry_potter.txt",
#     "historical_figures.txt",
#     "lord_of_the_rings.txt",
#     "spongebob.txt",
#     "star_wars.txt",
#     "technology.txt",
#     "video_game_characters.txt",
#     "video_games.txt"
# ]

if wordlist_filenames is not None:
    wordlists = wordlist_filenames
else:
    wordlists = wordlists_dir.glob("*.txt")

words: List[str] = []

for wordlist in wordlists:
    file_path = wordlists_dir / wordlist
    with open(file_path, "r", encoding="utf-8") as word_stream:
        words.extend(word_stream.read().split("\n"))

# For codenames
with open("wordlist_for_codenames.txt", "w", encoding="utf-8") as codenames_stream:
    codenames_stream.write("\n".join(words))

# For skribbl.io
with open("wordlist_for_skribbl.txt", "w", encoding="utf-8") as skribbl_stream:
    skribbl_stream.write(",".join(words))
