class Book:
    genre = 'Empty'
    def __init__(self, title, author, pages, prices = 0):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__prices = prices
    def __str__(self):
        return f"{self.__title} by {self.__author} with {self.__pages} pages, ${self.__prices}"
    
    def pageofBook(self):
        return self.__pages
    
    def getTitle(self):
        return self.__title
    
    # Getter method for title
    @property
    def title(self):
        return self.__title
    
    #Setter method for title
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and new_title:
            self.__title = new_title
        else:
            raise ValueError("New title is empty/not a string")
    
    @title.deleter
    def title(self):
        del self.__title

    @classmethod
    def creatBookFromDict(cls, dictBook):
        return cls(dictBook['Title'], dictBook['author'], dictBook['pages'], dictBook['Prices'])
    
    @classmethod
    def creatBookFromList(cls, listBook):
        books = []
        for bookdata in listBook:
            title = bookdata[0]
            author = bookdata[1]
            pages = bookdata[2]
            Prices = bookdata[3]
            book = cls(title, author, pages, Prices)
            books.append(book)
        return books
    
    @classmethod
    def updateGenreBook(cls):
        cls.genre = "Python Programming"
    
    #Khong dung cham gi voi thuoc tinh cua doi tuong
    @staticmethod
    def averageBookPrice(books):
        total_price = 0
        for book in books:
            total_price += book.__price
        return total_price / len(books) if books else 0
    
    def __eq__(self, orther):
        return self.__title == orther.__title and self.__author == orther.__author
    
    def __sub__(self, orther):
        return self.__prices - orther.__prices
#Create the instances from book class
book1 = Book("Python Programming", "Author 1", 160, 3.5)
book2 = Book("Learning Python", "Author 2", 311, 2.6)

print(book1) #print book information using __str__

#Instance method
print(f"{book2.getTitle()} has {book1.pageofBook()} pages")

#Create a new book from dictionary
dictBook = {'Title' : 'OOP in Python',
            'author' : 'Author 3',
            'pages' : 213,
            'Prices': 5.4}
book4 = Book.creatBookFromDict(dictBook)
print(book4)

#Create a new book from list
listBook = [
    ['web application with Python', 'Author 4', 272, 4.3],
    ['Game programming with Python', 'Author 5', 150, 6.4],
    ['Machine learning with Python', 'Author 6', 200, 8.5]
]

bookFromlist = Book.creatBookFromList(listBook)
for book in bookFromlist:
    print(book)

print(book1 - book2)
print(book1 == book1) #False
print(book1 == book2) #True

#it nhat 10000 sample
#NCKH: 20000