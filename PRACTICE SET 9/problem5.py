words = ["Donkey", "bad", "ganda"]

try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    # Create a sample file if it doesn't exist
    content = "This is a sample text file. It contains some bad words like Donkey and ganda that need to be censored."
    with open("file.txt", "w") as f:
        f.write(content)

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)