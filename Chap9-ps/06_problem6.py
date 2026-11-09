#Mine a log file and tell wheeter it has "Python in it "

with open("Chap9-ps/06_problem6.txt") as f:
    content = f.read()
    if "Python" in content:
        print("Yes, Python is present in the file")
    else:
        print("No, Python is not present in the file")