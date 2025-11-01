import json
import time
def load_data():
    try:
        with open("youtubes1.txt","r") as file:
            try:
                rtn = json.load(file)
            except json.JSONDecodeError:
                # empty or invalid file -> treat as empty list
                return []
            return rtn
    except FileNotFoundError:
        return []       

def save_data(videos):
    # save to the same file we load from
    with open("youtubes1.txt","w") as file:
        json.dump(videos, file, indent=2)

def display_data(videos):
    print("*********************************")
    print()
    if not videos:
        print("No videos saved yet.")
        return

    for index, value in enumerate(videos):
        # value is expected to be a dict with 'title' and 'duration'
        title = value.get('title', '<no title>') if isinstance(value, dict) else str(value)
        duration = value.get('duration', '<no duration>') if isinstance(value, dict) else ''
        print(f"{index}. Title: {title}  Duration: {duration}")

def add_data(videos):
    title = input("Enter the title: ")
    duration = input("Enter the duration: ")
    videos.append({"title":title,"duration":duration})
    save_data(videos)

def update_data(videos):
    pass

def delete_data(videos):
    pass






videos = load_data()
while True:
    shown_data = ["1.List all videos","2.Add video","3.Update video","4.Delete Video","5.Exit"]
    for data in shown_data:
        print(data)
    user_input = int(input("Select any one: "))
    match user_input:
        case 1:
            display_data(videos)
        case 2:
            add_data(videos)
        case 3:
            update_data(videos)
        case 4:
            delete_data(videos)
        case 5:
            print("Exiting....")
            time.sleep(2)
            print("Exitted Successfully")
            break
        

    