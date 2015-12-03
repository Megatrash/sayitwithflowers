#!/usr/bin/env python3

import sys
import itertools
import argparse

# CONSTS
flowers = {
    'h': 'hibiscus',
    'b': 'blossom',
    'r': 'rose',
    't': 'tulip',
    'c': 'cherry_blossom',
    '.': 'herb'}
fgflowers = ['h', 'r', 't', 'c']
bgflower = 'b'
border = '.'

# ALPHABET
letters = {
    'c':
    [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1]],
    'd':
    [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0]],
    'e':
    [[1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 1]],
    'f':
    [[1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
    'h':
    [[1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1]],
    'i':
    [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
    'k':
    [[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]],
    'l':
    [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1]],
    'o':
    [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]],
    'r':
    [[1, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 1]],
    'u':
    [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]],
    ' ': [[0], [0], [0], [0], [0]]
    }


# ZIP LETTERS
def zip_arrays(groupa, groupb):
    if groupa == []:
        return groupb

    newgroup = []
    for linea, lineb in zip(groupa, groupb):
        newgroup.append(list(itertools.chain(linea, lineb)))
    return newgroup


# GENERATE FLOWER LETTER
def flower_letter_grid(letter, style, bg):
    height = len(letter)
    # blank bg frame
    frame = []
    for idx in range(0, height):
        line = letter[idx]
        frame.append(map(lambda x: style if x else bg, line))
    return list(frame)


# FRAMING
def lateral_framing(line):
    return border + bgflower + line + bgflower + border


def vertical_framing(lenline, orientation):
    border_rule = border * (lenline + 4)
    fill = border + (bgflower * (lenline + 2)) + border
    if orientation == 't':
        return [border_rule, fill]
    else:
        return [fill, border_rule]


def full_framing(formated):
    text = []
    for vf in vertical_framing(len(formated[0]), 't'):
        text.append(vf)
    for line in formated:
        text.append(lateral_framing(''.join(line)))
    for vf in vertical_framing(len(formated[0]), 'b'):
        text.append(vf)
    return text


def frame_array_to_string(text):
    text_string = ''
    for t in text:
        text_string += t + '\n'
    return text_string


def main():
    # Prepare keys
    keys = letters.keys()
    keys.remove(' ')
    keys.append('<space>')

    parser = argparse.ArgumentParser(
        description='Print some flowers.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', metavar='t', type=str,
                        help='The text to print, letters must be within : %s'
                        % (', '.join(keys)))
    parser.add_argument('--spaced', action='store_true', dest='spaced',
                        default=False, help='Spaces between letters')

    args = parser.parse_args()

    # TEXT PREPARATION
    if args.spaced:
        text = ' '.join(list(args.text))
    else:
        text = str(args.text)

    formated = []
    for idx, letter in enumerate(text):
        fg = fgflowers[idx % len(fgflowers)]
        formated = zip_arrays(formated, flower_letter_grid(
            letters[letter], fg, bgflower))

    text = full_framing(formated)
    text_string = frame_array_to_string(text)

    # FLOWING PRINTING
    result = ""
    for f in text_string:
        if f == '\n':
            result += f
            continue
        result += ':' + flowers[f] + ': '

    print result

if __name__ == "__main__":
    main()
