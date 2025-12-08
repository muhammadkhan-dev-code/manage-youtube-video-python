import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file) # load the file and convert into json  type would be list 
    except FileNotFoundError:
        return []

# save data helper 
def save_data(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
     print("\n","★ "* 5 ," Youtube Videos ", "★ "* 5)    
     for idx, video in  enumerate(videos, start=1):
         print(f"{idx}: Name: {video['name']}, Duration: {video['time']}")

     print( "\t","★ "* 10)

         
def add_new_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")

    videos.append({'name':name , 'time':time})

    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    user_number=int(input ("\n Enter a number of Video to Update: "))

    if 1<= user_number<= len(videos):
        new_name=input("Enter a New Name for Video: ")
        new_time= input("Enter the new Time for  Video : ")

        videos[user_number-1]={'name':new_name, 'time':new_time}
        save_data(videos)
    else:
        print("★ Invalid Index Selected ★")

    
def delete_video(videos):
    list_all_videos(videos)
    index=int(input (" ★ Enter a number of Video to Delete:"))

    if 1<= index<= len(videos):
        del videos[index-1]
        print(" \n ★ Video Deleted Successfully ★ ")
        save_data(videos)
    else:
        print("★ Invalid video index selected ★ ")



def main():
    videos= load_data()
    while True:

        print("\n Youtube Manager | Choose any option")
        print(" 1 List all Youtube Videos ")
        print(" 2 Add a youtube video ")
        print(" 3 Update a youtube Video details")
        print(" 4 Delete a youtube Video from list")
        print(" 5 Exit  ")

        userChoice= input(" \n ★  Enter Your Choice: ")
        # print(videos)

        match userChoice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_new_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("\n ★ Thanks for Using Youtube  Video Manager ★")
                break
            case _:
                print("Invalid Choice ")


if __name__== "__main__":
    main()

