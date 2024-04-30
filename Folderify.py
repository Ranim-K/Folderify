import inquirer
import os
import subprocess
import pyfiglet
from colorama import Fore
import sys


def display_ascii_art():
    ascii_art = pyfiglet.figlet_format("Sortify")
    print(Fore.BLUE + ascii_art)


def create_folder():
    while True:
        try:
            folders_number = int(input("How many folders do you want to create? "))

            if folders_number <= 0:
                raise ValueError("Number of folders must be a positive integer.")

            parent_dir = input("Where do you want to put them? ")

            while not os.path.exists(parent_dir):
                print("Invalid directory path.")
                parent_dir = input("Please enter a valid directory path: ")

            questions = [
                inquirer.List('choice',
                              message='How do you want to name them?',
                              choices=[
                                  ('Numbers', '1'),
                                  ('Alphabetic', '2'),
                                  ('Custom', '3')
                              ],
                              ),
            ]
            answers = inquirer.prompt(questions)
            choice = answers['choice']

            if choice not in ["1", "2", "3"]:
                raise ValueError("Invalid choice. Please select a valid option.")

            if choice == "1":
                for i in range(1, folders_number + 1):
                    folder_name = str(i)
                    folder_path = os.path.join(parent_dir, folder_name)
                    os.makedirs(folder_path)
                print("The folders have been created successfully!")
                subprocess.Popen(["Explorer", os.path.realpath(parent_dir)])
            elif choice == "2":
                case_choice = input("Do you want to create folders in uppercase or lowercase? (U/u for uppercase, L/l for lowercase): ")
                if case_choice.lower() == 'u':
                    folders = [chr(i) for i in range(65, 91)]
                elif case_choice.lower() == 'l' :
                    folders = [chr(i) for i in range(97, 123)]  
                else:
                    print("Invalid choice. Please enter U/u for uppercase or L/l for lowercase.")
                    exit(1) 
                for i in range(folders_number):
                    folder_name = folders[i % len(folders)]
                    if i >= len(folders):
                        folder_name += str(i // len(folders))
                    folder_path = os.path.join(parent_dir, folder_name)
                    os.makedirs(folder_path)
                print("The folders have been created alphabetically!")
                subprocess.Popen(["Explorer", os.path.realpath(parent_dir)])
                                
            elif choice == "3":
                folder_name = input("Enter Folder Name: ")
                folder_path = os.path.join(parent_dir, folder_name)
                os.makedirs(folder_path)
                print("The folders have been created successfully!")
                subprocess.Popen(["Explorer", os.path.realpath(parent_dir)])
            break

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def return_to_menu():
    input("Press enter to return to the main menu....")
    main()


def main():
    display_ascii_art()
    while True:
        questions = [
            inquirer.List('choice',
                          message='Menu',
                          choices=[
                              ("Create Folders", "1"),
                              ("Rename folder or file", "2"),
                              ("Organize files", "3"),
                              ("Exit", "4")
                          ],
                          ),
        ]
        answers = inquirer.prompt(questions)
        choice = answers['choice']

        if choice == '1':
            try:
                create_folder()
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        elif choice == '2':
            print('two')
        elif choice == '3':
            print('three')
        elif choice == '4':
            sys.exit()


if __name__ == '__main__':
    main()
