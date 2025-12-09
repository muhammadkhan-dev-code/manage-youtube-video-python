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

def list_videos():
    print("\n","★ "* 5 ," Youtube Videos ", "★ "* 5)  
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(f'ID: {row[0]}, Name: {row[1]}, Time: {row[2]}')
    
    print( "\t","★ "* 10)


def add_video(name, time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    connection.commit()


def update_video(vidId, new_name, new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (new_name, new_time, vidId))
    connection.commit()


def delete_video(vidId):
    cursor.execute("DELETE FROM videos WHERE id=?", (vidId,))
    connection.commit()
    
def main():
    while True:
        print("\nYouTube  Manager App With DB")
        print("1 List Videos")
        print("2. Add Video")
        print("3 update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("\n ★ Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name= input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice == '3':
            vidId= input ("Enter video Id to update: ")
            name= input("Enter the new video name: ")
            time=input("Enter the new video time: ")
            update_video(vidId, name , time)
        elif choice == '4':
            vidId= input ("Enter video Id to delete:")
            delete_video(vidId)
        elif choice == '5':
            print("\n ★ Thanks for Using Youtube  Video Manager ★")
            break
        else:
            print("Invalid choice. Please try again.")
    
    connection.close()

if __name__ == '__main__':
    main()
