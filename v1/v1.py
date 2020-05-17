import os
import sys
import time


def directory_traversal(path):
    line = "-" * 100
    if not os.path.isabs(path):
        path = os.path.abspath(path)
        
    if os.path.exists(path):
        for folder, subfolders, files in os.walk(path):
            print("\n\nDirectory :\t", folder)
            for subfolder in subfolders:
                print(f"Sub-folders in the directory :\t", subfolder)
            print("Files inside the directory :\n")
            for filename in files:
                print("\t", filename)
            print("\n", line)
                
    else:
        print("Invalid path")


def main():
    print(f"\n\n\t\t\tDIRECTORY TRAVERSAL\n\n")
    
    if len(sys.argv) < 2:
        print("\nInvalid commands. Please type -h (for help) or -u (for usage) after the application name.")
        return
    
    if (sys.argv[1].lower()) == '-h':
        print("This script lists all the directories and files present in the given ABSOLUTE PATH.")
        return
    elif (sys.argv[1].lower()) == '-u':
        print("This script uses command line arguments."
              "\nExample of how to run this script:\tpython3 script_name.py absolute_path_of_directory.")
    else:
        print(f"\npath specified : \t{sys.argv[1]}\n\n")
        try:
            start_time = time.time()
            directory_traversal(sys.argv[1])
            end_time = time.time()
            print("\n\nTime Elapsed:\t", end_time - start_time, "\n\n")
        except Exception:
            print("Error: Invalid Input")


if __name__ == "__main__":
    main()
