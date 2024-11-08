import time

file_path = "index.html"

while True:
    with open(file_path, "a") as file:
        file.write(f"<!-- Updated at {time.ctime()} -->\n")
    print("Appended new content.")
    time.sleep(10)  # Wait for 10 seconds before the next update
