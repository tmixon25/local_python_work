from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count words
    words = contents.split()
    num_words = len(words)
    print(f"The File {path} has about {num_words} words.")