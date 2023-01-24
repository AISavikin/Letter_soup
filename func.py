from random import choice, shuffle
from string import ascii_uppercase
from docxtpl import DocxTemplate
from datetime import datetime


def show(matrix):
    for i in matrix:
        print(*i)


def fill(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '*':
                matrix[i][j] = choice(ascii_uppercase)


def save(matrix, words, path=''):
    shuffle(words)
    tpl = DocxTemplate('tpl.docx')
    context = {
        'matrix': matrix,
        'rows': len(matrix),
        'words': [len(words), words]
    }
    tpl.render(context)
    file_name = f'letter_soup_{datetime.now():%d-%m}.docx'
    tpl.save(f'{path}/{file_name}')
    return file_name


def gen_matrix(num=15):
    return [['*' for row in range(num + 5)] for col in range(num)]


def input_words():
    words = input('Введите слова через пробел: ').split()
    words.sort(key=len, reverse=True)
    return words


def find_index(word: str, row: list):
    indices = list(range((len(row) - len(word) + 1)))
    while indices:
        index = choice(indices)
        cnt = 0
        for i in range(len(word)):
            if row[index:][i] == '*':
                cnt += 1
            else:
                break
        if cnt == len(word):
            return index
        else:
            indices.remove(index)
    return


def get_coords(matrix, word, orientation):
    coords = []
    if orientation == 'v':
        matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    rows = list(range(len(matrix)))
    while rows:
        x = choice(rows)
        y = find_index(word, matrix[x])
        if y is not None:
            coords = [x, y]
            break
        else:
            rows.remove(x)

    if coords and orientation == 'v':
        coords[0], coords[1] = coords[1], coords[0]

    return coords


def put_word(matrix, word, orientation, coords):
    if not coords:
        print(f'слово {word} не влезает!')
    else:
        row, col = coords
        for let in word:
            matrix[row][col] = let
            if orientation == 'h':
                col += 1
            if orientation == 'v':
                row += 1
            if orientation == 'd':
                row += 1
                col += 1
    return matrix


def run(words):
    matrix = gen_matrix()
    orientations = ['h', 'v']
    for i in range(len(words)):
        orientation = orientations[i % len(orientations)]
        word = words[i].upper()
        coords = get_coords(matrix, word, orientation)
        matrix = put_word(matrix, word, orientation, coords)
    fill(matrix)
    # show(matrix)
    # save(matrix, words)
    return matrix


if __name__ == '__main__':
    words = input_words()
    matrix = run(words)
