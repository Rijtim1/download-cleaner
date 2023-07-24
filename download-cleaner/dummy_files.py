import os
import random
import string
from tqdm import tqdm

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

# Path to the "Downloads" folder
downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

# Generate random files with progress bar
total_files = 10000
with tqdm(total=total_files, desc="Creating Files", unit="file") as pbar:
    for i in range(total_files):
        # Choose a random category
        category = random.choice(list(file_categories.keys()))

        # Choose a random extension from the selected category
        extensions = file_categories[category]
        extension = random.choice(extensions) if extensions else '.txt'

        # Generate a random filename
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        filename = filename + extension

        # Create an empty file with the generated filename in the "Downloads" folder
        file_path = os.path.join(downloads_dir, filename)
        with open(file_path, 'w') as file:
            pass

        pbar.update(1)

print("Random files created and saved in the 'Downloads' folder successfully!")
