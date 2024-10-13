import os

import pytest

from solution.task_6 import deserialize, serialize

data = [
    {"id": 1, "name": "Иван Петров", "age": 35, "has_altushka": 0},
    {"id": 2, "name": "Петр Сидоров", "age": 48, "has_altushka": 1},
    {"id": 3, "name": "Александр Иванов", "has_altushka": 1},
    {"id": 4, "name": "Дмитрий Смирнов", "age": 22, "has_altushka": 0},
    {"id": 5, "name": "Сергей Васильев", "age": 29},
    {"id": 6, "name": "Артем Кузнецов", "age": 30, "has_altushka": 1},
    {"id": 15, "name": "Денис Ковалев", "age": 34},
    {"id": 16, "name": "Степан Белов", "age": 28, "has_altushka": 1},
    {"id": 17, "name": "Виктор Лебедев", "age": 33},
    {"name": "Алексей Куликов", "id": 19, "has_altushka": 0, "age": 23},
    {"id": 20, "age": 37, "name": "Станислав Григорьев"},
    {"age": 40, "name": "Олег Ларионов", "id": 25},
]


@pytest.mark.parametrize(
    "input_data",
    [
        [{"id": 1, "name": "Петр Сидоров"}],
        [
            {
                "id": 1,
                "name": "Петр Сидоров",
                "age": 35,
                "sex": "male",
                "has_altushka": 0,
            }
        ],
        [
            {"id": 1, "name": "Петр Сидоров"},
            {"name": "Степан Белов", "id": 2},
            {"name": "Александр Иванов", "id": 3, "altushka_id": 49},
            {"id": 2, "name": "Алексей Куликов", "salary": 30000},
        ],
        [
            {"id": 100, "name": "Олег Ларионов"},
            {"name": "Денис Ковалев", "id": 252},
        ],
        [
            {"random_number": -149, "text": "abracadabra"},
            {"other_random_number": -3_245_123, "string_text": "hi mom"},
            {"truth": 42, "file": "file.txt"},
        ],
    ],
)
def test_serialize(input_data):
    serialize(input_data, "data.txt")
    assert deserialize("data.txt") == input_data
    os.remove("data.txt")


@pytest.mark.parametrize("input_data_path,expected", [("tests/skufs_data.txt", data)])
def test_dataset(input_data_path, expected):
    assert deserialize(input_data_path) == expected
