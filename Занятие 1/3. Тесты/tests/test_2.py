import pytest

from solution.task_2 import play


@pytest.mark.parametrize(
    "input_words,expected",
    [
        (["word1", "1word", "dword"], []),
        (["word1"], []),
        (["word", "word", "word", "word", "word"], [2, 3, 4, 5]),
        (["hello", "obstacles", "segway", "york"], []),
        (["bob", "book", "kengaroo", "book", "kengaroo", "ocean"], [4, 5]),
        (["river", "rabbit", "tree", "eagle", "elephant", "tree", "tank"], [6]),
        (
            ["tiger", "rabbit", "tiger", "rabbit", "tiger", "tornado", "tiger"],
            [3, 4, 5, 7],
        ),
    ],
)
def test_play(input_words, expected):
    assert play(input_words) == expected
