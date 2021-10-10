from typing import Dict

from .base import sh


def get_students_dict() -> Dict[str, str]:
    githubs = sh.col_values(3)[2:]
    dict_ = {}
    for idx, key in enumerate(sh.col_values(2)[2:]):
        dict_[key.lower()] = (idx+2, githubs[idx].lower())
    return dict_


def get_hm_to_do():
    return sh.row_values(2)[3:]


class Students:
    __dict = get_students_dict()
    __hm_to_do = get_hm_to_do()

    def __getitem__(self, item):
        if item not in Students.__dict:
            __dict = get_students_dict()
        return Students.__dict.get(item, None)

    @staticmethod
    def items():
        return Students.__dict.items()

    def get_undone_homework(self, student):
        students_tuple = self[student]
        if students_tuple is None:
            return None
        hm_to_do = []
        for idx, hm in enumerate(sh.row_values(students_tuple[0]+1)[3:]):
            if hm != 'Done':
                hm_to_do.append(self.__hm_to_do[idx])
        if idx < len(self.__hm_to_do):
            hm_to_do.extend(self.__hm_to_do[idx+1:])
        return hm_to_do


if __name__ == "__main__":
    a = Students()
    print(a.get_undone_homework('@teadove'))
