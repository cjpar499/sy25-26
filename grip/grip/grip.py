import glob

files= glob.glob("*.txt")
pattern= input("Enter the pattern to search for: ")

def grep(files, pattern):
    for f in files:
        files = open(f, "r")
        lines=files.readlines()
        for i, line in enumerate(lines):
            if pattern in line:
                print(f,(i+1),line.strip())


grep(files, pattern)