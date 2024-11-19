import os
cwd = os.getcwd()
file_path = os.path.join(cwd, 'demo_files/data.txt')

try:
    file = open(file_path)
except FileNotFoundError:
    print("File not found")