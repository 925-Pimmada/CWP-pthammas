import sys

if len(sys.argv) != 2:
    print("none")
else:
    found = False

    for char in sys.argv[1]:
        if char == "z":
            print("z")
            found = True

    if not found:
        print("none")