"""
In this task your goal is to implement a simple phone book manager. It should be able to process the
following types of user’s queries:

The comment-out methods use format {name: number} as dictionary schema.
The real methods use format {number: name} as dictionary schema.
"""


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


class PhoneBook:
    def __init__(self):
        self.book = {}
        self.n = len(self.book)

    def add(self, name, number):
        """
        add number name. It means that the user adds a person with name and phone number
        to the phone book. If there exists a user with such number already, then your manager
        has to overwrite the corresponding name.
        """
        """
        self.book[name] = number
        """
        self.book[number] = name

    def del_number(self, number):
        """
        It means that the manager should erase a person with number from the phone
        book. If there is no such person, then it should just ignore the query.
        """
        """
        target = None

        for k, v in self.book.items():
            if v == number:
                target = k
        try:
            del self.book[target]
        except KeyError:
            return
        """
        try:
            del self.book[number]
        except KeyError:
            return

    def find(self, number):
        """
        It means that the user looks for a person with phone number. The manager
        should reply with the appropriate name, or with string “not found" (without quotes) if there is
        no such person in the book
        """
        """
        try:
            name = list(self.book.keys())[list(self.book.values()).index(number)]
            return name
        except ValueError:
            return "not found"
        """
        try:
            return self.book[number]
        except KeyError:
            return "not found"


def read_file(file):
    queries = []

    if file:
        with open(file, "r") as f:
            l = f.readlines()
            n = int(l[0])
            for i in range(1, len(l)):
                query = Query(l[i].split())
                queries.append(query)
        assert n == len(queries)
    # print("the file is loaded.")
    return queries


if __name__ == "__main__":
    queries = read_file(file="phone_book_example1.txt")
    phone_book = PhoneBook()

    for query in queries:
        if query.type == "add":
            phone_book.add(query.name, query.number)
        elif query.type == "del":
            phone_book.del_number(query.number)
        elif query.type == "find":
            print(phone_book.find(query.number), end=" ")

