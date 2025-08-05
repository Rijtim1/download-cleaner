# Download Cleaner

## Overview

Download Cleaner is a tool designed to automate the cleanup of your Downloads folder. It identifies and removes unnecessary files, ensuring your Downloads folder remains organized and clutter-free.

## Features

- Automated Cleanup: Cleans up files in the Downloads folder based on predefined criteria.
- Standalone Executable: Built using PyInstaller for ease of use.
- Continuous Integration and Deployment: Utilizes GitHub Actions for automated builds and releases.

## Requirements

- Python 3.9
- GitHub account with repository access
- GitHub Actions enabled

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/Rijtim1/download-cleaner.git
    cd download-cleaner
    ```

2. **Install Dependencies:**

    ```sh
    python -m pip install --upgrade pip
    pip install pyinstaller
    pip install -r requirements.txt
    ```

## Usage

1. **Build the Executable:**

    ```sh
    pyinstaller --onefile clean.py
    ```

2. **Run the Executable:**
    - Navigate to the `dist` folder where the executable is created.
    - Run the executable:

        ```sh
        ./clean.exe
        ```

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment. The workflow is triggered on pushes to the `master` branch and performs the following steps:

1. **Build Job:**
    - Checks out the code.
    - Sets up Python 3.9.
    - Installs dependencies.
    - Builds the executable using PyInstaller.
    - Uploads the executable as an artifact.

2. **Release Job:**
    - Downloads the artifact from the build job.
    - Generates a version tag.
    - Generates release notes based on the latest commit messages.
    - Creates a GitHub release.
    - Uploads the executable to the release.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, feel free to open an issue or contact the project maintainer.

Enjoy your clean and organized Downloads folder!
