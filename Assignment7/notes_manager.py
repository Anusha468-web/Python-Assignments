import os
import re

positive_words = ['happy', 'good', 'great', 'fantastic', 'awesome', 'positive', 'excellent']
negative_words = ['sad', 'bad', 'terrible', 'awful', 'negative', 'horrible']

notes_dir = 'usernotes'

if not os.path.exists(notes_dir):
    os.mkdir(notes_dir)

def read_note(file_name):
    try:
        with open(os.path.join(notes_dir, file_name), 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: The note does not exist.")
        return None

def analyze_sentiment(content):
    positive_count = len(re.findall(r'\b(?:' + '|'.join(positive_words) + r')\b', content, re.IGNORECASE))
    negative_count = len(re.findall(r'\b(?:' + '|'.join(negative_words) + r')\b', content, re.IGNORECASE))

    if positive_count > negative_count:
        return "Positive Sentiment"
    elif negative_count > positive_count:
        return "Negative Sentiment"
    else:
        return "Neutral Sentiment"
def create_new_note():
    filename = input("Enter the filename for your new note: ")
    content = input("Enter the content for your note: ")
    
    try:
        with open(os.path.join(notes_dir, filename), 'w') as file:
            file.write(content)
        print(f"Note '{filename}' created successfully!")
    except Exception as e:
        print(f"Error creating note: {e}")

def modify_note():
    notes = os.listdir(notes_dir)
    if not notes:
        print("No notes available to modify.")
        return
    print("Available notes:")
    for note in notes:
        print(note)
    filename = input("Enter the name of the note you want to modify: ")
    if filename in notes:
        content = read_note(filename)
        if content:
            print(f"\nCurrent content of '{filename}':\n{content}")
            new_content = input("\nEnter new content for the note: ")
            try:
                with open(os.path.join(notes_dir, filename), 'w') as file:
                    file.write(new_content)
                print(f"Note '{filename}' updated successfully!")
            except Exception as e:
                print(f"Error modifying note: {e}")
    else:
        print("Note not found. Please try again.")
def main():
    while True:
        print("1. Read & Analyze Notes")
        print("2. Create New Note")
        print("3. Modify Existing Note")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                print("\n--- Analyze Notes ---")
                print("1. Analyze all notes")
                print("2. Analyze a specific note")
                analyze_choice = int(input("Enter : "))
                
                if analyze_choice == 1:
                    notes = os.listdir(notes_dir)
                    if not notes:
                        print("No notes available to analyze.")
                    else:
                        for note in notes:
                            content = read_note(note)
                            if content:
                                print(f"\nAnalyzing '{note}':")
                                print(analyze_sentiment(content))
                elif analyze_choice == 2:
                    filename = input("Enter the filename to analyze: ")
                    content = read_note(filename)
                    if content:
                        print(f"\nSentiment analysis for '{filename}':")
                        print(analyze_sentiment(content))
                else:
                    print("Invalid choice. Please try again.")
            
            elif choice == 2:
                create_new_note()
            
            elif choice == 3:
                modify_note()
            
            elif choice == 4:
                print("Exiting the Notes Management System.")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()
