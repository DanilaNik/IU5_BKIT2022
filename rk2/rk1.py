from operator import itemgetter

class Book:
    def __init__(self, id, title, number, library_id):
        self.id = id
        self.title = title
        self.number = number 
        self.library_id = library_id

class Library:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BookLibrary:
    def __init__(self, library_id, book_id):
        self.library_id = library_id
        self.book_id = book_id

#Библиотеки
libraries = [
    Library(1, 'Российская государственная библиотека'),
    Library(2, 'Библиотека имени Достоевского'),
    Library(3, 'Библиотека имени Некрасова'),
    Library(4, 'Библиотека-читальня имени И.С. Тургенева'),
    Library(5, 'Центральная библиотека имени Добролюбова'),
    Library(6, 'Российская национальная библиотека'),
]

#Книги
books = [
    Book(1, 'Горе от ума', 150, 1),
    Book(2, 'Преступление и наказание', 70, 2),
    Book(3, 'Отцы и дети', 100, 3),
    Book(4, 'Евгений Онегин', 50, 1),
    Book(5, 'Ревизор', 40, 6),
]

books_libraries = [
    BookLibrary(1,1),
    BookLibrary(1,2),
    BookLibrary(1,3),
    BookLibrary(1,4),
    BookLibrary(1,5),
    BookLibrary(2,2),
    BookLibrary(3,2),
    BookLibrary(4,3),
    BookLibrary(5,4),
    BookLibrary(6,1),
    BookLibrary(6,2),
    BookLibrary(6,4),
    BookLibrary(6,5),
]

    #Соединение данных один-ко-многим
def one_to_many(libraries, books):
    return[(b.title, b.number, l.name)
        for l in libraries
        for b in books
        if b.library_id == l.id]
    
    #Соединение данных многие-ко-многим
def many_to_many(libraries, books):
    many_to_many_temp = [(l.name, bl.library_id, bl.book_id)
        for l in libraries
        for bl in books_libraries
        if l.id == bl.library_id]
    return [(b.title, b.number, library_name)
        for library_name, library_id , book_id in many_to_many_temp
        for b in books
        if b.id == book_id]
         
def example_A1(libraries, books):
    res_11 = sorted(one_to_many(libraries, books), key = itemgetter(2))
    return res_11

def example_A2(libraries, books):
    res_12_unsorted = []
    for l in libraries:
        l_books = list(filter(lambda i: i[2] == l.name, one_to_many(libraries, books)))
        if len(l_books) > 0:
            l_numbers = [number for _,number,_ in l_books]
            l_numbers_sum = sum(l_numbers)
            res_12_unsorted.append((l.name, l_numbers_sum))
    
    res_12 = sorted(res_12_unsorted, key = itemgetter(1), reverse=True)
    return res_12

def example_A3(libraries, books):
    res_13 = {}
    for l in libraries:
        if "имени" in l.name:
            l_books = list(filter(lambda i: i[2] == l.name, many_to_many(libraries, books)))
            l_books_titles = [x for x,_,_ in l_books]
            res_13[l.name] = l_books_titles
    return res_13

if __name__ == '__main__':
    print('Задание A1')
    print(example_A1(libraries, books))
    print('Задание A2')
    print(example_A2(libraries, books))
    print('Задание A3')
    print(example_A3(libraries, books))
