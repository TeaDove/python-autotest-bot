import subprocess
from pathlib import Path

import json as ujson


def start_tests() -> dict:
    module_folder = Path('app/tests/')
    subprocess.Popen(['pytest', '--json-report', '-v'], stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL, cwd=module_folder)
    output = ujson.load(open(module_folder / '.report.json'))
    return output


def gen_summary() -> dict:
    output = start_tests()
    summary = {'chapters': {}, 'tasks': {}}
    for test in output['tests']:
        idx = test['nodeid'].find('[')
        if idx != -1:
            names = test['nodeid'][:idx].split('/')[1].split('::')[1:]
        else:
            names = test['nodeid'].split('/')[1].split('::')[1:]
        passed = test['outcome'] == 'passed'
        chapter = names[0][4:]
        task = names[1][5:]

        if chapter not in summary['chapters']:
            summary['chapters'][chapter] = (int(passed), 1)
        else:
            chapter_data = summary['chapters'][chapter]
            summary['chapters'][chapter] = (chapter_data[0] + passed, chapter_data[1] + 1)

        if task not in summary['tasks']:
            summary['tasks'][task] = (int(passed), 1)
        else:
            task_data = summary['tasks'][task]
            summary['tasks'][task] = (task_data[0] + passed, task_data[1] + 1)

    return summary


if __name__ == "__main__":
    print(ujson.dumps(gen_summary()))
