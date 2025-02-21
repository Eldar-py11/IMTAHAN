import os 
import time 
import random
import shutil 
from datetime import datetime

file_type = {
    ".txt": "Documents",
    ".jpg": "Images",
    ".png": "Images",
}

def create_file():
    try:
        file_name = input("Enter the name of the file: ") 
        content = input("Enter the content for the file (or press Enter to leave it empty): ")  
        
        with open(file_name, "w") as file:
            file.write(content)
        
        print(f"File '{file_name}' has been created successfully!")
    except Exception as mkdir:
        print(f"ERROR: {mkdir}")



def file_move(file_names, destination_folder):   # file moved function
    try:
        if os.path.exists(file_names):
            os.makedirs(destination_folder, exist_ok=True)
            os.shutil.move(file_names, os.path.join(destination_folder, file_names))
            print(f"{file_names} currenly {destination_folder} She moved to her folder ")
        else:
            print(f"ERROR: folder not found!!")
    except Exception as moved:
        print(f"ERROR: {moved}") 

def rename_file(old_name, new_name):  # file rename function
    try:
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"{old_name} currenly {new_name} is named")
        else:
            print(f"ERROR: folder not found!!")
    except Exception as rename:
        print(f"ERROR: {rename}")

def delete_file(file_name):  # file delete functions 
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} Successfully deleted!") 
        else:
            print(f"ERROR: folder not found! ")
    except Exception as delete:
        print(f"ERROR: {delete}")


def generate_report(directory):
    try:
        files = os.listdir(directory)
        report = {}
        
        for file in files:
            extension = os.path.splitext(file)[1]  # file extension almaq
            report[extension] = report.get(extension, 0) + 1  # sayisini artitirirq estensiona gore

        # ekrana yazdirmaq report
        print(f"\nReport  **{directory} folder**")
        for extension, x in report.items():
            print(f"{extension}: {x} folder") # x sayi olaraq qoydum yeni
    except Exception as report:
        print(f"ERROR: {report}")


def main_menu():
    while True:
        print("file manager system")
        print("1. Folder moved")
        print("2. folder rename")
        print("3. file remove")
        print("4. generate report")
        print("5. Create a new file")
        print("6. exit")


        user_choise = input("enter one choise >> ")

        if user_choise == "1":
            file_name = input("enter moved file name:")
            destination_folder = input("enter name of the destination:")
            file_move(file_name, destination_folder)
        elif user_choise == "2":
            old_name = input("enter old folder name: ")
            new_name = input("enter new folder name:")
            rename_file(old_name, new_name)
        elif user_choise == "3":
            file_name = input("enter name of the file to deleted")
            delete_file(file_name)
        elif user_choise == "4":
            directory = input("Enter the name of the folder for report")
            generate_report(directory)
        elif user_choise == "5":
            create_file()
            break
        else:
            print("invalid option please tyr again :)")

        # su icirdim :D

        
    
main_menu()