from pathlib import Path


def get_res_dict() -> dict:
    res_dict_ = {}
    for file in Path("app/res").iterdir():
        res_dict_[file.stem] = open(file, 'r').read()
    return res_dict_


res_dict = get_res_dict()
