# This Python file uses the following encoding: utf-8
from sys import stdout
#TODO: import os + use os.get_terminal_size()
import math


def _bar_element_available(bar_element, encoding):
    try:
        bar_element.encode(encoding)
        return True
    except UnicodeEncodeError:
        return False


def _get_bar_element(frac=0):
    bar_char = u'\u2588'  # U+2588 'full block'

    if not _bar_element_available(bar_char, stdout.encoding):
        if (0 == frac):
            bar_char = u'#'
        else:
            bar_char = str(int(frac * 10))

    return bar_char


def _calc_scaling(data, width):
    """Calculates scaling factor for bar and padding for categories"""
    str_len = max(len(x) for x in data)

    # remaining chars until width reached:
    # four chars for whitespaces and separator
    remaining_width = width - str_len - 4

    max_entry = float(max(data.values()))
    scale_fac = max_entry / remaining_width

    return (str_len, scale_fac)


def barplot(data, width=60):
    """Print bar plot of categorical data to terminal"""
    bar_char = _get_bar_element()

    str_len, scale_fac = _calc_scaling(data, width)

    for entry in data:
        frac, whole = math.modf(data[entry] / scale_fac)
        last_bar_char = _get_bar_element(frac)

        print(u'{}: | {}{}'.format(
            entry.rjust(str_len), bar_char * int(whole), last_bar_char))


if __name__ == '__main__':

    test_data = {
        'a': 10,
        'b': 50,
        'c': 35,
        'd': 5
    }

    barplot(test_data)
