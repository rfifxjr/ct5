import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Подключение к Базе данных произоша успешно!")

    dogs_table = '''
      CREATE TABLE IF NOT EXISTS Dogs (
          ID INTEGER PRIMARY KEY,
          Name TEXT,
          Image TEXT,
          Breed TEXT,
          SubBreed TEXT
      );
      '''
    cursor.execute(dogs_table)
    print("Таблица собак создана!")

    pitomnik_table = '''
      CREATE TABLE IF NOT EXISTS Pitomnik (
          ID INTEGER PRIMARY KEY,
          Country TEXT,
          City TEXT
      );
      '''
    cursor.execute(pitomnik_table)
    print("Таблица питомников создана!")

    buyers_table = '''
      CREATE TABLE IF NOT EXISTS Buyers (
          ID INTEGER PRIMARY KEY,
          FirstName TEXT,
          LastName TEXT,
          PreferredBreeds TEXT
      );
      '''
    cursor.execute(buyers_table)
    print("Таблица потенциальныx покупателей создана")

    sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка подключения к базе данных", error)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение к БД закрыто")

