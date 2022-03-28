i = 0

def star_pattern():
    global i
    if (i < 5):
        print("*",end = ' ')
        i = i + 1
        star_pattern()

def main():
    star_pattern()

if __name__ == "__main__":
    main()