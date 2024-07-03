# Project Creator for UnrealEngine Dumper7 SDK

## Overview

This project automates the creation of Visual Studio solution (.sln) and project (.vcxproj) files for the latest game folder found in a specified directory. It also copies the necessary C++ SDK files and generates a basic `Main.cpp` file.

The main purpose of this project is to quickly set up and test the Dumper7 SDK. The example code included in `Main.cpp` is based on the Unreal Engine console code provided in `UsingTheSDK.md`.

## Directory Structure

project_creator/
├── main.py
├── file_utils.py
├── project_generator.py
├── vcxproj_templates.py
├── settings.ini

## Configuration

1. Create or edit the `settings.ini` file in the project directory with the following content:

    ```ini
    [Paths]
    base_path = C:\Dumper-7
    repos_path = C:\Users\KAI\source\repos
    ```

    Replace `C:\Dumper-7` and `C:\Users\KAI\source\repos` with your actual paths.

## Usage

1. Run the `main.py` file:
    ```bash
    python main.py
    ```

    The program will read the paths from `settings.ini`, locate the latest game folder in `base_path`, generate the Visual Studio project and solution files, and copy the necessary C++ SDK files.

## File Descriptions

- `main.py`: The entry point of the program, orchestrating the overall process.
- `file_utils.py`: Contains utility functions for file and directory operations:
  - `get_latest_game_name(base_path)`: Finds the latest game folder and returns the game name and path.
  - `copy_cpp_sdk_files(source_sdk_path, dest_path)`: Copies C++ SDK files.
- `project_generator.py`: Contains functions to generate Visual Studio project and solution files:
  - `create_vcxproj_file(project_path, project_name)`: Creates the `.vcxproj` file.
  - `create_vcxproj_filters_file(project_path, project_name)`: Creates the `.vcxproj.filters` file.
  - `create_sln_file(project_path, project_name)`: Creates the `.sln` file.
  - `create_main_cpp_file(project_path)`: Creates the `Main.cpp` file.
  - `create_empty_project_with_settings(base_path, repos_path)`: Generates and configures the entire project.
- `vcxproj_templates.py`: Contains template content for Visual Studio project and solution files:
  - `get_vcxproj_content(project_name)`: Returns the template content for the `.vcxproj` file.
  - `get_vcxproj_filters_content()`: Returns the template content for the `.vcxproj.filters` file.
  - `get_sln_content(project_name)`: Returns the template content for the `.sln` file.
  - `get_main_cpp_content()`: Returns the template content for the `Main.cpp` file.
- `settings.ini`: Configuration file containing paths for the base directory and repository directory.
- `UsingTheSDK.md`: Contains detailed instructions and examples for using the Dumper7 SDK, including the Unreal Engine console code example.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
