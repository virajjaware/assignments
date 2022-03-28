i = 1

def rec_fun():
    global i
    if (i < 6):
        print(i,end = ' ')
        i = i + 1
        rec_fun()

def main():
    rec_fun()

if __name__ == "__main__":
    main()