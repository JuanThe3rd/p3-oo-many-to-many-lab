class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        count = 0

        for contract in Contract.all: 
            if contract.author == self:
                count += contract.royalties

        return count

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception
        
        Contract.all.append(self)

    def contracts_by_date():        
        sorted_dates = sorted([contract.date for contract in Contract.all])
        sorted_contracts = []

        for date in sorted_dates:
            for contract in Contract.all:
                if contract.date == date:
                    sorted_contracts.append(contract)

        return sorted_contracts


# It seems as if the unit tests and instructions ask for 2 different things
# down here is the solution for Contract.contracts_by_date() per the Canvas 
# instructions.

'''
@classmethod
    def contracts_by_date(cls, date):        
        return [contract for contract in cls.all if contract.date == date]
'''