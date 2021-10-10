import subprocess
from pathlib import Path

import json as ujson


def start_tests() -> dict:
    module_folder = Path('app/tests/')
    subprocess.Popen(['pytest', '--json-report', '-v'], stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL, cwd=module_folder)
    output = ujson.load(open(module_folder / '.report.json'))
    return output


if __name__ == "__main__":
    start_tests()
