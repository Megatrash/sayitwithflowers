#!/usr/bin/env python3

import itertools
import argparse
import numpy as np

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
alphabet = {
    'a':
    [[0, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1]],
    'c':
    [[1, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 1, 1, 1]],
    'd':
    [[1, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 0]],
    'e':
    [[1, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 1, 1, 0],
     [1, 0, 0, 0],
     [1, 1, 1, 1]],
    'f':
    [[1, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 1, 1, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0]],
    'h':
    [[1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1]],
    'i':
    [[1, 1, 1],
     [0, 1, 0],
     [0, 1, 0],
     [0, 1, 0],
     [1, 1, 1]],
    'k':
    [[1, 0, 0, 1],
     [1, 0, 1, 0],
     [1, 1, 0, 0],
     [1, 0, 1, 0],
     [1, 0, 0, 1]],
    'l':
    [[1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 1, 1, 1]],
    'n':
    [[1, 0, 0, 0, 1],
     [1, 1, 0, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 0, 1, 1],
     [1, 0, 0, 0, 1]],
    'o':
    [[1, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 1]],
    'p':
    [[1, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 1, 1, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0]],
    'r':
    [[1, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 1, 1, 0],
     [1, 0, 1, 0],
     [1, 0, 0, 1]],
    's':
    [[0, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 1],
     [1, 1, 1, 0]],
    't':
    [[1, 1, 1],
     [0, 1, 0],
     [0, 1, 0],
     [0, 1, 0],
     [0, 1, 0]],
    'u':
    [[1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 1]],
    ' ':
    [[0],
     [0],
     [0],
     [0],
     [0]]
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


def check_text_letters(text):
    letters_not_available = []
    for letter in text:
        if letter not in alphabet.keys():
            letters_not_available.append(letter)
    if len(letters_not_available):
        print "One or more letters are not available. "\
            "Please contribute : %s" % letters_not_available
        return False
    return True


def main():
    # Prepare keys
    keys = alphabet.keys()
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

    if not check_text_letters(text):
        return

    formated = []
    for idx, letter in enumerate(text):
        fg = fgflowers[idx % len(fgflowers)]
        formated = zip_arrays(formated, flower_letter_grid(
            alphabet[letter], fg, bgflower))

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
