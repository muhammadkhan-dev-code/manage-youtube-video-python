import sqlite3
connection= sqlite3.connect('youtube_manager.db')

cursor= connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )

''')


def main():
    while True:
        print("\nYouTube  Manager App With DB")
        print("1 List Videos")
        print("2. Add Video")
        print("3 update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        


if __name__ == '__main__':
    main()
