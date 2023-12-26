import sqlite3
import pytest
import allure

@pytest.fixture(scope='session')
def database_connection():
    connection = sqlite3.connect('sqlite_python.db')
    yield connection
    connection.close()
@pytest.fixture()
def name():
    return "Бобик"

@pytest.fixture()
def breed():
    return "Той-терьер"

def test_insert_dog(database_connection):
    with allure.step("Выполнение INSERT-запроса"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Dogs (Name, Breed) VALUES (?, ?)", ("Бобик", "Той-терьер"))
            conn.commit()

        with allure.step("Проверка добавления строки"):
            test_dog_add(database_connection, "Бобик", "Той-терьер")

def test_dog_add(database_connection, name, breed):
    with allure.step("Проверка добавления собаки"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Name, Breed FROM Dogs WHERE Name = ? AND Breed = ?", (name, breed))
            result = cursor.fetchone()
            assert result is not None

def test_select_dog(database_connection):
    with allure.step("Выполнение SELECT-запроса"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Name, Breed FROM Dogs WHERE Name = ?", ("Бобик",))
            result = cursor.fetchone()
            assert result is not None

def test_update_dog(database_connection):
    with allure.step("Выполнение UPDATE-запроса"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Dogs SET Breed = ? WHERE Name = ?", ("Лабрадор", "Бобик"))
            conn.commit()

        with allure.step("Проверка обновления строки"):
            with database_connection as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT Breed FROM Dogs WHERE Name = ?", ("Бобик",))
                result = cursor.fetchone()
                assert result is not None

def test_delete_dog(database_connection):
    with allure.step("Выполнение DELETE-запроса"):
        with database_connection as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Dogs WHERE Name = ?", ("Бобик",))
            conn.commit()


if __name__ == '__main__':
    pytest.main([file])

