#!/usr/bin/env python

import itertools
import argparse

# CONSTS
types = ['flowers', 'catz']

flowers = {
    'h': 'hibiscus',
    'b': 'blossom',
    'r': 'rose',
    't': 'tulip',
    'c': 'cherry_blossom',
    '.': 'herb'}

fgflowers = ['h', 'r', 't', 'c']
bgflower = 'b'

cats = {
    'c': 'cat',
    '2': 'cat2',
    's': 'smirk_cat',
    'k': 'kissing_cat',
    'm': 'smiley_cat',
    '.': 'herb'}

fgcats = ['c', 'k', 's', 'm']
bgcat = '2'
border = '.'

# ALPHABET
alphabet = {
    'a':
    [[0, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1]],
    'b':
    [[1, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 1, 1, 0]],
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
    'g':
    [[0, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 0, 1, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 0]],
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
    'j':
    [[0, 1, 1, 1],
     [0, 0, 1, 0],
     [0, 0, 1, 0],
     [1, 0, 1, 0],
     [0, 1, 1, 0]],
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
    'm':
    [[1, 0, 0, 0, 1],
     [1, 1, 0, 1, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1]],
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
    'q':
    [[0, 1, 1, 0],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 0, 1, 1],
     [0, 1, 1, 1]],
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
    'v':
    [[1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0]],
    'w':
    [[1, 0, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 1, 0, 1, 1],
     [1, 0, 0, 0, 1]],
    'x':
    [[1, 0, 1],
     [1, 0, 1],
     [0, 1, 0],
     [1, 0, 1],
     [1, 0, 1]],
    'y':
    [[1, 0, 1],
     [1, 0, 1],
     [0, 1, 0],
     [0, 1, 0],
     [0, 1, 0]],
    'z':
    [[1, 1, 1],
     [0, 0, 1],
     [0, 1, 0],
     [1, 0, 0],
     [1, 1, 1]],
    ' ':
    [[0],
     [0],
     [0],
     [0],
     [0]],
    '*':
    [[1, 0, 1, 0, 1],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 1, 1, 1, 0],
     [1, 0, 1, 0, 1]],
    '!':
    [[1],
     [1],
     [1],
     [0],
     [1]],
    '<':
    [[0, 0, 1],
     [0, 1, 0],
     [1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]],
    '3':
    [[1, 1, 0],
     [0, 0, 1],
     [1, 1, 0],
     [0, 0, 1],
     [1, 1, 0]]
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
def lateral_framing(line, bgsmiley, bordersmiley):
    return bordersmiley + bgsmiley + line + bgsmiley + bordersmiley


def vertical_framing(lenline, orientation, bgsmiley, bordersmiley):
    border_rule = bordersmiley * (lenline + 4)
    fill = border + (bgsmiley * (lenline + 2)) + bordersmiley
    if orientation == 't':
        return [border_rule, fill]
    else:
        return [fill, border_rule]


def full_framing(formated, bgsmiley, bordersmiley):
    text = []
    for vf in vertical_framing(len(formated[0]), 't', bgsmiley, bordersmiley):
        text.append(vf)
    for line in formated:
        text.append(lateral_framing(''.join(line), bgsmiley, bordersmiley))
    for vf in vertical_framing(len(formated[0]), 'b', bgsmiley, bordersmiley):
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


def check_type(smileytype):
    if smileytype not in types:
        print "The type is not available. "\
            "Please contribute. Available types : %s" % (types.keys())
        return False
    return True


def main():
    # Prepare keys
    keys = alphabet.keys()
    keys.remove(' ')
    keys.append('<space>')

    parser = argparse.ArgumentParser(
        description='Print some things.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('type', metavar='type', type=str,
                        help='Say it with what ? %s'
                        % (', '.join(types)))
    parser.add_argument('text', metavar='text', type=str,
                        help='The text to print, letters must be within : %s'
                        % (', '.join(keys)))
    parser.add_argument('--spaced', action='store_true', dest='spaced',
                        default=False, help='Spaces between letters')

    args = parser.parse_args()

    smileytype = args.type
    # CHECK GIVEN TYPE
    if not check_type(smileytype):
        return

    # TEXT PREPARATION
    if args.spaced:
        text = ' '.join(list(args.text))
    else:
        text = str(args.text)

    if not check_text_letters(text):
        return

    if smileytype == 'catz':
        smileys = cats
        fgsmileys = fgcats
        bgsmiley = bgcat
    elif smileytype == 'flowers':
        smileys = flowers
        fgsmileys = fgflowers
        bgsmiley = bgflower

    formated = []
    for idx, letter in enumerate(text):
        fg = fgsmileys[idx % len(fgsmileys)]
        formated = zip_arrays(formated, flower_letter_grid(
            alphabet[letter], fg, bgsmiley))

    text = full_framing(formated, bgsmiley, border)
    text_string = frame_array_to_string(text)

    # FLOWING PRINTING
    result = ""
    for f in text_string:
        if f == '\n':
            result += f
            continue
        result += ':' + smileys[f] + ': '

    print result

if __name__ == "__main__":
    main()
