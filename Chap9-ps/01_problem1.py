with open("Chap9-ps/01_problem1.py") as f:
    content = f.read()
    if("twinkle" in content):
        print("Twinkle is present in the file")
    else:
        print("Twinkle is not present in the file")