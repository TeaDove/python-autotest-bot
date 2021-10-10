from pathlib import Path
import shutil
import subprocess


def download(url: str):
    env_folder = Path('app/tests/env_folder')
    shutil.rmtree(env_folder, ignore_errors=True)
    env_folder.mkdir()
    subprocess.call(['git', 'clone', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=env_folder)


if __name__ == '__main__':
    download('https://github.com/johan4ik/itam_python_courses')
