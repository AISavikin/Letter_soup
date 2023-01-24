from main import find_index


def test_find_index():
    word = 'cat'
    row = ['*', 'q', '*', '*', '*']
    assert find_index(word, row) == 2
    row = ['*', '*', '*', '*', '*']
    assert find_index(word, row) in [0, 1, 2]
    row = ['*', 'q', '*', 't', '*']
    assert find_index(word, row) is None
    word = 'category'
    row = ['*', '*', '*', '*', '*']
    assert find_index(word, row) is None
    word = 'milk'
    row = ['*', '*', '*', '*', 'c', '*', '*', '*', '*', 'j', '*', '*', ]
    assert find_index(word, row) in [0, 5]
    word = 'asdf'
    row = ['*', '*', 'c', '*', '*', '*', '*', 'g', '*']
    assert find_index(word, row) == 3



