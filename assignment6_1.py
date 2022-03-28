class BookStore:
    NoOfBooks = 0
    def __init__(self,name,author):

        self.name = name
        self.author = author

    def Display(self):
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        print("Book Name is",self.name,"author name is ",self.author," and No of books",BookStore.NoOfBooks)
def main():

   # BookName = input("Enter book name :")
  #  AuthorName = input("Enter author name: ")
    #noofbooks = int(input("Enter number books: "))

    obj1 = BookStore("C","Dennis Ritchie")
    obj1.Display()

    obj2 = BookStore("Linux System Programming","Robert Love")
    obj2.Display()

if __name__ == "__main__":
    main()