try:
    with open("old.txt") as f:
        content = f.read()
except FileNotFoundError:
    # Create old.txt if it doesn't exist
    content = "This is the old file content.\nIt will be copied to renamed_by_python.txt"
    with open("old.txt", "w") as f:
        f.write(content)

with open("renamed_by_python.txt", "w") as f:
    f.write(content)