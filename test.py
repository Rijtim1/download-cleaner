import os
import shutil
import time
import unittest
from clean import FileOrganizer, file_categories, get_downloads_path, organize_folder

class FileOrganizationTestCase(unittest.TestCase):
    def setUp(self):
        # Create a temporary test folder for each test case
        self.test_folder = os.path.join(os.getcwd(), "test_folder")
        os.mkdir(self.test_folder)

    def tearDown(self):
        # Remove the temporary test folder after each test case
        shutil.rmtree(self.test_folder)

    def test_empty_folder(self):
        # Test scenario: Empty Folder
        clean = FileOrganizer(self.test_folder)
        clean.list_files()
        self.assertEqual(len(clean.files), 0)

        clean.get_file_extension()
        self.assertEqual(len(clean.extensions), 0)

        clean.setup()
        clean.move_files()

        # Verify that no files were moved
        self.assertEqual(len(os.listdir(self.test_folder)), 0)

    def test_folder_with_files(self):
        # Test scenario: Folder with Files
        # Create test files with different extensions in the test folder
        file_names = ["file1.txt", "file2.docx", "file3.jpg", "file4.mp3"]
        for file_name in file_names:
            file_path = os.path.join(self.test_folder, file_name)
            with open(file_path, "w") as file:
                file.write("Test content")

        organize_folder(self.test_folder)

        # Verify that files are moved to the appropriate directories
        for file_name in file_names:
            file_path = os.path.join(self.test_folder, file_name)
            extension = os.path.splitext(file_name)[1]
            category = None
            for cat, ext_list in file_categories.items():
                if extension in ext_list:
                    category = cat
                    break
            if category:
                expected_path = os.path.join(self.test_folder, category, extension, file_name)
            else:
                expected_path = os.path.join(self.test_folder, "Misc", file_name)
            self.assertTrue(os.path.exists(expected_path))

    def test_duplicate_files(self):
    # Test scenario: Duplicate Files
    # Create duplicate files with different extensions in the test folder
        file_name = "readme.txt"
        file_path1 = os.path.join(self.test_folder, file_name)
        file_path2 = os.path.join(self.test_folder, "readme_1.txt")
        with open(file_path1, "w") as file1, open(file_path2, "w") as file2:
            file1.write("Test content")
            file2.write("Test content")

        organize_folder(self.test_folder)

        # Verify that duplicate files are moved with unique names
        expected_path1 = os.path.join(self.test_folder, "Documents", ".txt", file_name)
        expected_path2 = os.path.join(self.test_folder, "Documents", ".txt", "readme_1.txt")
        self.assertTrue(os.path.exists(expected_path1))
        self.assertTrue(os.path.exists(expected_path2))

    def test_existing_destination_directories(self):
    # Test scenario: Existing Destination Directories
    # Create existing destination directories
        existing_directories = [
            os.path.join(self.test_folder, "Documents", ".txt"),
            os.path.join(self.test_folder, "Images", ".jpg")
        ]
        for directory in existing_directories:
            os.makedirs(directory)

        # Create test files with corresponding extensions
        file_names = ["file1.txt", "file2.jpg"]
        for file_name in file_names:
            file_path = os.path.join(self.test_folder, file_name)
            with open(file_path, "w") as file:
                file.write("Test content")

        organize_folder(self.test_folder)

        # Verify that files are moved to the existing directories without recreating them
        for file_name in file_names:
            file_path = os.path.join(self.test_folder, file_name)
            extension = os.path.splitext(file_name)[1]
            category = None

            # Find the category for the given extension
            for cat, exts in file_categories.items():
                if extension in exts:
                    category = cat
                    break

            expected_path = os.path.join(self.test_folder, category, extension, file_name)

            self.assertTrue(os.path.exists(expected_path))


    def test_execution_time(self):
        # Test scenario: Execution Time
        # Create a large number of test files in the test folder
        file_names = [f"file{i}.txt" for i in range(1000)]
        for file_name in file_names:
            file_path = os.path.join(self.test_folder, file_name)
            with open(file_path, "w") as file:
                file.write("Test content")

        start_time = time.time()
        organize_folder(self.test_folder)
        execution_time = time.time() - start_time

        # Verify that the execution time is reasonable
        self.assertLess(execution_time, 5.0)

    def test_error_handling(self):
        # Test scenario: Error Handling
        # Test with an invalid folder path
        invalid_folder = os.path.join(self.test_folder, "nonexistent_folder")
        with self.assertRaises(FileNotFoundError):
            organize_folder(invalid_folder)

    def test_custom_file_categories(self):
    # Test scenario: Custom File Categories
    # Create custom file categories and extensions
        custom_categories = {
            "Custom1": [".xyz"],
            "Custom2": [".abc"],
            "Custom3": [".123"]
        }
        custom_file_categories = {**file_categories, **custom_categories}

        # Create files with custom extensions in the test folder
        file_names = ["file1.xyz", "file2.abc", "file3.123", "file4.unknown"]
        for file_name in file_names:
            file_path = os.path.join(self.test_folder, file_name)
            with open(file_path, "w") as file:
                file.write("Test content")

        organize_folder(self.test_folder)

        # Verify that files with custom extensions are moved to their respective categories,
        # and unrecognized extensions are moved to the "Misc" category with extension-specific subfolders
        for file_name in file_names:
            file_path = os.path.join(self.test_folder, file_name)
            extension = os.path.splitext(file_name)[1]
            category = custom_file_categories.get(extension, "Misc")  # Default to "Misc" if extension not recognized

            if category == "Misc":
                expected_path = os.path.join(self.test_folder, category, extension, file_name)
            else:
                expected_path = os.path.join(self.test_folder, category, file_name)

            self.assertTrue(os.path.exists(expected_path))

if __name__ == "__main__":
    unittest.main()
