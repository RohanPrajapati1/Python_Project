import json

def load_notes():
    try:
        with open("notes.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_notes(note):
    try:
        with open("notes.txt" , "w") as file:
            json.dump(note , file)
    except Exception as e:
        print(f"Error saving notes: {e}")

def add_note(note):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    note.append({'title':title , 'content':content})
    save_notes(note)

def view_notes(note):
    for i , nt in enumerate(note , start=1):
        print(f"{i}. Title: {nt['title']} , Content: {nt['content']}")

def delete_note(note):
    view_notes(note)
    if note:
        try:
            index = int(input("Enter the number of the note to delete: ")) - 1
            if 0 <= index < len(note):
                note.pop(index)
                save_notes(note)
                print("Note deleted successfully.")
            else:
                print("Invalid note number.")
        except ValueError:
            print("Please enter a valid number.")

def search_note(note):
    keyword = input("Enter keyword to search: ")
    found_notes = [nt for nt in note if keyword.lower() in nt['title'].lower() or keyword.lower() in nt['content'].lower()]
    
    if found_notes:
        print("Search results:")
        for i, nt in enumerate(found_notes, start=1):
            print(f"{i}. Title: {nt['title']} , Content: {nt['content']}")
    else:
        print("No notes found with the given keyword.")

def main():
    while True:
        notes = load_notes()
        print("Welcome to Personal Note Manager!")
        print("1. Add note.")
        print("2. View notes.")
        print("3. Delete note.")
        print("4. Search note.")
        print("5. Exit.")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                add_note(notes)
            case 2:
                view_notes(notes)
            case 3:
                delete_note(notes)
            case 4:
                search_note(notes)
            case 5:
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()