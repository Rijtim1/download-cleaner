__all__ = ['FileOrganizer', 'organize_folder']
import os
import shutil
import tqdm


# Dictionary defining file categories and their associated extensions
file_categories = {
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt'],
    'Spreadsheets': ['.xls', '.xlsx', '.ods'],
    'Presentations': ['.ppt', '.pptx', '.odp'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'],
    'Music': ['.mp3', '.wav', '.aac', '.m4a', '.flac'],
    'Executables': ['.exe', '.msi', '.dmg'],
    'Scripts': ['.py', '.sh', '.js', '.php', '.pl'],
    'Databases': ['.db', '.sqlite', '.mdb'],
    'Webpages': ['.html', '.htm', '.css', '.xml'],
    'Text Files': ['.log'],
    'Code Files': ['.java', '.cpp', '.h'],
    'Compressed Files': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Misc': []
}


class FileOrganizer:
    def __init__(self, path):
        self.path = path

    def list_files(self):
        items = os.listdir(self.path)
        self.files = [item for item in items if os.path.isfile(os.path.join(self.path, item))]

    def get_file_extension(self):
        self.extensions = set(os.path.splitext(file)[1] for file in self.files)

    def create_directories(self):
        for extension in self.extensions:
            for category, extensions in file_categories.items():
                if extension in extensions:
                    category_dir = os.path.join(self.path, category)
                    if not os.path.exists(category_dir):
                        os.mkdir(category_dir)
                    extension_dir = os.path.join(category_dir, extension)
                    if not os.path.exists(extension_dir):
                        os.mkdir(extension_dir)

    def move_files(self):
        for file in tqdm.tqdm(self.files, desc="Moving files"):
            extension = os.path.splitext(file)[1]
            category = self.get_category(extension)
            category_dir = os.path.join(self.path, category)
            extension_dir = os.path.join(category_dir, extension)
            dest_file = self.get_unique_filename(file, extension_dir)

            if not os.path.exists(category_dir):
                os.mkdir(category_dir)

            if not os.path.exists(extension_dir):
                os.mkdir(extension_dir)

            shutil.move(os.path.join(self.path, file), dest_file)

    def get_category(self, extension):
        for category, extensions in file_categories.items():
            if extension in extensions:
                return category
        return 'Misc'

    def get_unique_filename(self, filename, directory):
        base_name, extension = os.path.splitext(filename)
        count = 1
        while os.path.exists(os.path.join(directory, filename)):
            filename = f"{base_name}_{count}{extension}"
            count += 1
        return os.path.join(directory, filename)

    def organize_files(self):
        self.list_files()
        self.get_file_extension()
        self.create_directories()
        self.move_files()


def organize_folder(path):
    print(f"Organizing folder at {path}")
    organizer = FileOrganizer(path)
    organizer.organize_files()


def get_user_preference():
    config_file = os.path.expanduser("~/.download_cleaner_config")
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            downloads_path = f.read().strip()
    else:
        print("Do you want to auto-detect the downloads folder or specify it?")
        print("1. Auto-detect")
        print("2. Specify")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            downloads_path = os.path.expanduser("~/Downloads")
        else:
            downloads_path = input("Enter the path to the downloads folder: ")
        with open(config_file, 'w') as f:
            f.write(downloads_path)
    return downloads_path

def main():
    downloads_path = get_user_preference()
    if os.path.exists(downloads_path):
        organize_folder(downloads_path)
    else:
        print(f"Folder {downloads_path} not found.")


if __name__ == "__main__":
    main()
