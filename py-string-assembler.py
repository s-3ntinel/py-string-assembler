#!/usr/bin/python3

import argparse


def assemble_string(string, delim):
    """Assemble a string using only characters from native class docstrings"""
    chars_found_idxs = []
    missing_chars = []

    for char in string:
        found = False

        for class_idx in range(0, len(().__class__.__base__.__subclasses__())):
            # look in docstring of a class and find index of wanted character
            char_doc_idx = str(().__class__.__base__.__subclasses__()[class_idx].__doc__).find(char)

            if char_doc_idx == -1:  # char was not found in current class docstring
                continue

            else:
                chars_found_idxs.append(
                    '().__class__.__base__.__subclasses__()[' + str(class_idx) + '].__doc__[' + str(char_doc_idx) + ']')
                found = True
                break

        # char was not found in any available class docstring
        if not found:
            missing_chars.append(char)

    # print unavailable chars
    if missing_chars:
        print('[+] Character(s) \'' + '\', \''.join(
            map(str, missing_chars)) + '\' not found in any available class docstrings')
        return ''

    return delim.join(chars_found_idxs)


def main():
    parser = argparse.ArgumentParser(
        description='Program used for constructing strings in python without usage of characters \' or \". \
        Constructed string does not require any builtin methods. \
        String is constructed by joining individual characters found in available docstrings of native python classes. \
        Output may vary on different versions of python since the docstrings are different.'
    )

    parser.add_argument('-s', '--string', help='Source string', required=True)
    parser.add_argument('-d', '--delimiter', help='Delimiter used to join individual characters', default='+')
    args = parser.parse_args()

    print(assemble_string(args.string, args.delimiter))


if __name__ == '__main__':
    main()
