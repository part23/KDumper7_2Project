import os
from file_utils import get_latest_game_name, copy_cpp_sdk_files
from vcxproj_templates import get_vcxproj_content, get_vcxproj_filters_content, get_sln_content, get_main_cpp_content

def create_vcxproj_file(project_path, project_name):
    vcxproj_content = get_vcxproj_content(project_name)
    with open(os.path.join(project_path, f"{project_name}.vcxproj"), "w") as file:
        file.write(vcxproj_content)

def create_vcxproj_filters_file(project_path, project_name):
    vcxproj_filters_content = get_vcxproj_filters_content()
    with open(os.path.join(project_path, f"{project_name}.vcxproj.filters"), "w") as file:
        file.write(vcxproj_filters_content)

def create_sln_file(project_path, project_name):
    sln_content = get_sln_content(project_name)
    with open(os.path.join(project_path, f"{project_name}.sln"), "w") as file:
        file.write(sln_content)

def create_main_cpp_file(project_path):
    main_cpp_content = get_main_cpp_content()
    with open(os.path.join(project_path, "Main.cpp"), "w") as file:
        file.write(main_cpp_content)

def create_empty_project_with_settings(base_path, repos_path):
    project_name, latest_folder = get_latest_game_name(base_path)
    project_path = os.path.join(repos_path, project_name)
    
    if not os.path.exists(project_path):
        os.makedirs(project_path)

    create_vcxproj_file(project_path, project_name)
    create_vcxproj_filters_file(project_path, project_name)
    create_sln_file(project_path, project_name)
    create_main_cpp_file(project_path)

    source_sdk_path = os.path.join(latest_folder, "CppSDK")
    copy_cpp_sdk_files(source_sdk_path, project_path)

    print(f"Created and configured project: {project_name} at {project_path}")
