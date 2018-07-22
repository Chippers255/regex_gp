import string
import random


TERMINAL_SET = []
FUNCTION_SET = []


def longest_common_substring(string_1, string_2):
    m = [[0] * (1 + len(string_2)) for _ in range(1 + len(string_1))]

    longest, x_longest = 0, 0
    for x in range(1, 1 + len(string_1)):
        for y in range(1, 1 + len(string_2)):
            if string_1[x - 1] == string_2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0

    return string_1[x_longest - longest: x_longest]
# end def longest_common_substring


def get_characters(accept_list, reject_list):
    accept_characters = []
    reject_characters = []

    for word in accept_list:
        for character in word:
            if character not in accept_characters:
                accept_characters.append(character)

    for word in reject_list:
        for character in word:
            if character not in reject_characters:
                reject_characters.append(character)

    accept_characters.sort()
    reject_characters.sort()

    return accept_characters, reject_characters
# end def get_characters


def get_ranges(character_list):
    character_range = []

    for set in [string.digits, string.ascii_lowercase, string.ascii_uppercase]:
        for i, start in enumerate(list(set)):
            a = start
            if a in character_list:
                for j, current in enumerate(list(set)):
                    c = current
                    if c in character_list:
                        if a != c and i < j:
                            character_range.append(a + '-' + c)
                    else:
                        break

    return character_range
# end def get_ranges


def get_substrings(accept_list, reject_list):
    substrings = []

    for list in [accept_list, reject_list]:
        for word_1 in list:
            for word_2 in list:
                if word_1 != word_2:
                    lcs = longest_common_substring(word_1, word_2)
                    if lcs not in substrings and len(lcs) >= 2:
                        substrings.append(lcs)

    return substrings
# end def get_substrings


def build_terminal_set(accept_list, reject_list):
    global TERMINAL_SET

    accept_characters, reject_characters = get_characters(accept_list, reject_list)

    accept_ranges = get_ranges(accept_characters)
    reject_ranges = get_ranges(reject_characters)

    substrings = get_substrings(accept_list, reject_list)

    TERMINAL_SET.extend(accept_characters)
    TERMINAL_SET.extend(reject_characters)
    TERMINAL_SET.extend(accept_ranges)
    TERMINAL_SET.extend(reject_ranges)
    TERMINAL_SET.extend(substrings)
    TERMINAL_SET.extend(['.', '0-9', 'a-z', 'A-Z', ' '])
    TERMINAL_SET.extend(['\A', '\b', '\B', '\d', '\D', '\s', '\S', '\w', '\W', '\Z'])
# end def build_terminal_set


def build_function_set():
    global FUNCTION_SET

    FUNCTION_SET.extend(['_|_', '{_,_}', '(_)', '[_]', '{_}', '_*+', '_++', '_+?', '[^_]', '^_$', '_+', '_*', '_?',
                         '_*?', '_??', '_**', '_+*', '_?*', '_?+', '(?=_)', '(?!_)', '(?<=_)', '__', '__', '__', '__'])
# end def build_function_set


def random_value():
    set = random.choice([FUNCTION_SET, TERMINAL_SET])
    value = random.choice(set)

    if value in TERMINAL_SET:
        return value, 0
    elif value in ['_|_', '{_,_}', '__']:
        return value, 2
    else:
        return value, 1
# end def random_value
