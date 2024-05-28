# Download Cleaner

## Overview

Download Cleaner is a tool designed to automate the cleanup of your Downloads folder. It identifies and removes unnecessary files, ensuring your Downloads folder remains organized and clutter-free. This project includes a GitHub Actions CI/CD pipeline that builds and releases the tool as a standalone executable.

## Features

- **Automated Cleanup:** Automatically cleans up files in the Downloads folder based on predefined criteria.
- **Standalone Executable:** Built using PyInstaller, the tool is distributed as a standalone executable for ease of use.
- **Continuous Integration and Deployment:** Utilizes GitHub Actions for automated builds and releases.

## Requirements

- Python 3.9
- GitHub account with repository access
- GitHub Actions enabled

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/download-cleaner.git
   cd download-cleaner
   ```

2. **Install Dependencies:**

   ```bash
   python -m pip install --upgrade pip
   pip install pyinstaller
   pip install -r requirements.txt
   ```

## Usage

1. **Build the Executable:**

   ```bash
   pyinstaller --onefile clean.py
   ```

2. **Run the Executable:**
   - Navigate to the `dist` folder where the executable is created.
   - Run the executable:

     ```bash
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

## GitHub Actions Workflow

```yaml
name: Build and Release

on:
  push:
    branches:
      - master

jobs:
  build:
    runs-on: windows-latest

    steps:
    - name: Check out the code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      shell: bash
      run: |
        python -m pip install --upgrade pip
        pip install pyinstaller
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    - name: Build .exe with PyInstaller
      run: pyinstaller --onefile clean.py

    - name: Upload artifact
      uses: actions/upload-artifact@v3
      with:
        name: clean
        path: dist/clean.exe

  release:
    needs: build
    runs-on: ubuntu-latest

    steps:
    - name: Check out the code
      uses: actions/checkout@v3

    - name: Download artifact
      uses: actions/download-artifact@v3
      with:
        name: clean
        path: .

    - name: Generate tag name
      id: generate_tag
      run: echo "tag=v1.0.${{ github.run_number }}" >> $GITHUB_ENV

    - name: Generate release notes
      id: generate_notes
      uses: actions/github-script@v6
      with:
        script: |
          const { execSync } = require('child_process');
          const commits = execSync('git log --pretty=format:"* %s" -n 10').toString();
          return commits;

    - name: Create GitHub Release
      id: create_release
      uses: actions/create-release@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        tag_name: ${{ env.tag }}
        release_name: Release ${{ env.tag }}
        body: ${{ steps.generate_notes.outputs.result }}
        draft: false
        prerelease: false

    - name: Upload Release Asset
      uses: actions/upload-release-asset@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        upload_url: ${{ steps.create_release.outputs.upload_url }}
        asset_path: ./clean.exe
        asset_name: clean.exe
        asset_content_type: application/octet-stream
```

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

---

By following this README, you should be able to set up, build, and use the Download Cleaner tool with ease. The CI/CD pipeline will ensure that any changes are automatically built and released, keeping the process smooth and efficient.
