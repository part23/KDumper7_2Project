import os
import glob
import shutil

def get_latest_game_name(base_path):
    folders = [f for f in glob.glob(base_path + "\\*") if os.path.isdir(f)]
    latest_folder = max(folders, key=os.path.getmtime)
    game_name = latest_folder.split('-')[-1]
    return game_name, latest_folder

def copy_cpp_sdk_files(source_sdk_path, dest_path):
    for item in os.listdir(source_sdk_path):
        source_item = os.path.join(source_sdk_path, item)
        dest_item = os.path.join(dest_path, item)
        if os.path.isdir(source_item):
            shutil.copytree(source_item, dest_item, dirs_exist_ok=True)
        else:
            shutil.copy2(source_item, dest_item)
