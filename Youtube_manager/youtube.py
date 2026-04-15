import json

def load_data():
    try:
        with open("youtube_video.txt" , 'r') as file:
           return json.load(file)
    except FileNotFoundError:
        return []
    

def save_data(videos):
    with open('youtube_video.txt' ,'w') as file:
        json.dump(videos , file)        

def list_all_videos(videos):
    # add indexing to iterable data
    for index , video in enumerate(videos , start=1):
        print(f"{index}. {video['name']} , Duration: {video['time']} ")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name' : name , 'time' : time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    try:
        idx = int(input("Enter video number to update: ")) - 1
        if 0 <= idx < len(videos):
            videos[idx]["name"] = input("Enter new name: ")
            videos[idx]["time"] = input("Enter new time: ")
            save_data(videos)
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")



def delete_video(videos):
    list_all_videos(videos)
    try:
        idx = int(input("Enter video number to delete: ")) - 1
        if 0 <= idx < len(videos):
            videos.pop(idx)
            save_data(videos)
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video details ")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Thanks for visiting.....")
                break
            case _:
                print("Invaild choice ")

if __name__ == "__main__":
    main()