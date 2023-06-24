import os
import shutil
import time
import tqdm
import user_path_util


file_categories = {
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt'],
    'Spreadsheets': ['.xls', '.xlsx', '.ods'],
    'Presentations': ['.ppt', '.pptx', '.odp'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'],
    'Music': ['.mp3', '.wav', '.aac', '.m4a', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Executables': ['.exe', '.msi', '.dmg'],
    'Scripts': ['.py', '.sh', '.js', '.php', '.pl'],
    'Databases': ['.db', '.sqlite', '.mdb'],
    'Webpages': ['.html', '.htm', '.css', '.xml'],
    'Misc': []
}


class Clean:
    def __init__(self, path):
        self.path = path
        self.start = time.time()

    def list_files(self):
        items = os.listdir(self.path)
        self.files = [item for item in items if os.path.isfile(
            os.path.join(self.path, item))]

    def get_file_extension(self):
        self.extensions = []
        for file in self.files:
            split = os.path.splitext(file)
            if split[1] not in self.extensions:
                self.extensions.append(split[1])

    def setup(self):
        with tqdm.tqdm(total=len(self.extensions), desc="Setting up directories") as pbar:
            for extension in self.extensions:
                for key, value in file_categories.items():
                    if extension in value:
                        category_dir = os.path.join(self.path, key)
                        if not os.path.exists(category_dir):
                            os.mkdir(category_dir)
                        extension_dir = os.path.join(category_dir, extension)
                        if not os.path.exists(extension_dir):
                            os.mkdir(extension_dir)
                pbar.update(1)

    def move_files(self):
        extension_map = {}
        for category, extensions in file_categories.items():
            for extension in extensions:
                extension_map[extension] = category

        file_counts = {}

        with tqdm.tqdm(total=len(self.files), desc="Moving files") as pbar:
            for file in self.files:
                extension = os.path.splitext(file)[1]
                category = extension_map.get(extension, "Misc")
                dest_dir = os.path.join(self.path, category)
                dest_file = os.path.join(dest_dir, file)
                if not os.path.exists(dest_dir):
                    os.mkdir(dest_dir)
                if os.path.exists(dest_file):
                    count = file_counts.get(file, 0) + 1
                    new_file_name = f"{os.path.splitext(file)[0]}_{count}{extension}"
                    dest_file = os.path.join(dest_dir, new_file_name)
                    file_counts[file] = count
                shutil.move(os.path.join(self.path, file), dest_file)
                pbar.update(1)


def get_path():
    return user_path_util.get_path()


def organize_folder(path):
    print(f"Organizing folder at {path}")
    clean = Clean(path)
    clean.list_files()
    clean.get_file_extension()
    clean.setup()
    clean.move_files()
    print(f"Total time taken: {time.time() - clean.start:.2f} seconds")
    print(f"Total files moved: {len(clean.files)}")


def main():
    path = get_path()
    if os.path.exists(path):
        organize_folder(path)
    else:
        print(f"Invalid path: {path}")


if __name__ == "__main__":
    main()
