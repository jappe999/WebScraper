from database import Database

def main(number):
    database = Database('root', '42069blazeIt', 'beta')
    data = database.fetch(number)


if __name__ == '__main__':
    main(100)
