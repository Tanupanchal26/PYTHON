try:
    with open("log.txt") as f:
        content = f.read()
except FileNotFoundError:
    # Create log.txt if it doesn't exist
    content = "python is a great language\njava is also great\npython is easy to learn"
    with open("log.txt", "w") as f:
        f.write(content)

if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")