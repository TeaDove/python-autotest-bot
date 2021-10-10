import pytest

class TestChapter2:
    def test_module_integrity(self):
        from ..env_folder.itam_python_courses.homeworks.chapter_2 import task_2_1_1
        from ..env_folder.itam_python_courses.homeworks.chapter_2 import task_2_1_2
        from ..env_folder.itam_python_courses.homeworks.chapter_2 import task_2_1_3
        from ..env_folder.itam_python_courses.homeworks.chapter_2 import task_2_1_4
        from ..env_folder.itam_python_courses.homeworks.chapter_2 import task_2_2_1
        from ..env_folder.itam_python_courses.homeworks.chapter_2 import task_2_2_2

    @pytest.mark.parametrize('in_, out', [['Гендо Геннадий', 'Доброго времени суток, Гендо "Человек" Геннадий!'],
                                          ['Артём Соседка', 'Доброго времени суток, Артём "Человек" Соседка!']])
    def test_2_1_1(self, in_: str, out: str):
        from ..env_folder.itam_python_courses.homeworks.chapter_2 import task_2_1_1
        assert task_2_1_1.greeting(in_) == out
