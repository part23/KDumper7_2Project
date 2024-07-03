import configparser
from project_generator import create_empty_project_with_settings

def read_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    base_path = config.get('Paths', 'base_path')
    repos_path = config.get('Paths', 'repos_path')
    return base_path, repos_path

if __name__ == "__main__":
    base_path, repos_path = read_settings()
    create_empty_project_with_settings(base_path, repos_path)
