import os
import shutil

def organize_directory(path):
    """
    Organizes files in the specified directory into folders based on extensions.
    """
    # Dictionary mapping folder names to file extensions
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv'],
        'Music': ['.mp3', '.wav', '.flac', '.aac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java']
    }

    # Ensure the path exists
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return

    print(f"Scanning directory: {path}...")
    
    count = 0
    # Iterate over files in the directory
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Skip directories and this script itself
        if os.path.isdir(file_path) or filename == os.path.basename(__file__):
            continue

        moved = False
        # Check file extension against our dictionary
        for folder_name, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                # Create destination folder if it doesn't exist
                dest_folder = os.path.join(path, folder_name)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                # Move the file
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                count += 1
                moved = True
                break
        
        # If extension not found in list, move to 'Others'
        if not moved:
            other_folder = os.path.join(path, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} -> Others/")
            count += 1

    print(f"\nDone! Organized {count} files.")

if __name__ == "__main__":
    # Get the current working directory
    current_dir = os.getcwd()
    
    user_input = input(f"Do you want to organize the current directory ({current_dir})? (y/n): ").lower()
    
    if user_input == 'y':
        organize_directory(current_dir)
    else:
        custom_path = input("Please enter the full path of the directory to organize: ")
        organize_directory(custom_path)
