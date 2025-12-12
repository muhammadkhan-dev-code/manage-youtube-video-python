from pymongo import MongoClient
from bson import ObjectId


MONGO_URL ="mongodb+srv://youtubepy:youtubepy@cluster0.64l0fwr.mongodb.net/?"

client = MongoClient(MONGO_URL, tlsAllowInvalidCertificates=True)
# print(client)

db=client["ytmanager"]
video_collection=db["videos"]
# print(video_collection)

def list_videos():
     print("\n","★ "* 5 ," Youtube Videos ", "★ "* 5)  
     for video in  video_collection.find({}):
         print(f"★ Video ID: {video['_id']} Video Name: {video['name']} ★ Video Time: {video['time']} ")
      
def add_video(name, time):
    video_collection.insert_one({
        "name":name,
        "time":time
    })
    print(f"\n ★ Video '{name}' added successfully! ★")

def update_video(vidId, name , time):
    
    video_collection.find_one_and_update({
        "_id":ObjectId(vidId)
    },{
        "$set":{
            "name":name,
            "time":time
        }
    })
    print(f"\n ★ Video with ID '{vidId}' updated successfully! ★")

def delete_video(vidId):
    video_collection.delete_one({
        "_id":ObjectId(vidId)
    })
    print(f"\n ★ Video with ID '{vidId}' deleted successfully! ★")


def main():
    while True:
        print("\nYouTube  Manager App With  MONGO DB")
        print("1 List Videos")
        print("2. Add New Video")
        print("3 update Existing Video")
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


if __name__=="__main__":
    main()

