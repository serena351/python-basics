try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")