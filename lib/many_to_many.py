# from datetime import date

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.add_to_all(self)
        
    @classmethod
    def add_to_all(cls, author):
        if not isinstance(author, Author):
            raise ValueError('Fail to add to all, author is not an instance of Author class!')
        cls.all.append(author)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.add_to_all(self)
    
    @classmethod
    def add_to_all(cls, book):
        if not isinstance(book, Book):
            raise ValueError('Fail to add to all, book is not an instance of Book class!')
        cls.all.append(book)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.add_to_all(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError('author must be an instance of Author class!')
        self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise ValueError('book must be an instnace of Book class!')
        self._book = book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError('data must be a string!')
        self._date = date
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise ValueError('royalties must be an integer!')
        self._royalties = royalties

    @classmethod
    def add_to_all(cls, contract):
        if not isinstance(contract, Contract):
            raise ValueError('Fail to add to all, contract is not an instance of Contract class!')
        cls.all.append(contract)

    @classmethod
    def contracts_by_date(cls, date):
        return sorted([contract for contract in cls.all if contract.date == date], key=lambda contract: contract.royalties)
