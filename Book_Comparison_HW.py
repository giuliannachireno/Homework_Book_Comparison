import requests
import string

def get_unique_word_count(url):
    """Download a book from a URL, clean the text, and return the count of unique words."""
    response = requests.get(url)

    punctuation_remove = ",.!?;"
    punctuation_space = "'\"()[]=-_"

    unique_words = {}

    lines = response.text.split('\n')
    for line in lines:
        for c in punctuation_remove:
            line = line.replace(c, "")
        for c in punctuation_space:
            line = line.replace(c, " ")

        words = line.split()

        for word in words:
            word = word.lower().strip(string.punctuation)  # Ensure clean words
            if word:  # Ignore empty strings
                unique_words[word] = unique_words.get(word, 0) + 1

    return len(unique_words)

pride_prejudice_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
yellow_wallpaper_url = "https://www.gutenberg.org/cache/epub/75392/pg75392.txt"

pride_prejudice_unique_words = get_unique_word_count(pride_prejudice_url)
yellow_wallpaper_unique_words = get_unique_word_count(yellow_wallpaper_url)

print(f"Pride and Prejudice (Jane Austen) unique words: {pride_prejudice_unique_words}")
print(f"The Yellow Wallpaper (Charlotte Perkins Gilman) unique words: {yellow_wallpaper_unique_words}")

if pride_prejudice_unique_words > yellow_wallpaper_unique_words:
    print("Jane Austen used more unique words.")
else:
    print("Charlotte Perkins Gilman used more unique words.")