#! /usr/bin/env python3
# create a wordlist out of any text document. Filter by wordlength if desired.

import argparse
import string

version = 1.0

# parse args
parser = argparse.ArgumentParser(prog='Listinator')
parser.add_argument('--version', '-v', action='version', version=f'%(prog)s {version}', help='Current version number')
parser.add_argument('--max', '-M', dest='max_len', default=None, help='Maximum word length (inclusive) to filter by. Default: None')
parser.add_argument('--min', '-m', dest='min_len', default=None, help='Minimum word length (inclusive) to filter by. Default: None')
parser.add_argument('--source', '-s', dest='source_file', default=None, required=True, help='Path of source file to create wordlist from.')

args = parser.parse_args()

min_len = args.min_len
max_len = args.max_len
source_file = args.source_file
# source_file = input('enter path to file:\n')


def filter_by_len(words) -> list:
    """filter words by min length and/or max length if given. Else return """
    filtered_list = [word for word in words]
    if not min_len and not max_len:
        return filtered_list
    if min_len:
        print(f'Filtering by min length: {min_len}...')
        filtered_list = [word for word in filtered_list if len(word) >= int(min_len)]
    if max_len:
        print(f"Filtering by max length: {max_len}...")
        filtered_list = [word for word in filtered_list if len(word) <= int(max_len)]
    return filtered_list


def remove_punctuation(words) -> list:
    """strip all punctuation and return stripped words as sorted list"""
    # burninating the punctuation
    stripped = set([word.translate(str.maketrans('', '', string.punctuation)) for word in words])
    return sorted(list(stripped))


def get_word_set() -> set:
    """read source file and return set of words"""
    with open(source_file, 'r') as f:
        words = f.read().lower().split()
        words_set = set(words)
        return words_set


def write_to_file(words) -> None:
    """write each word on a new line and save as word_list.txt"""
    with open(f'word_list.txt', 'w') as new:
        for word in words:
            new.writelines(f'{word}\n')


def main() -> None:
    """create a wordlist out of any text document. Filter by word length if desired."""
    word_set = get_word_set()
    stripped_words = remove_punctuation(word_set)
    filtered_words = filter_by_len(stripped_words)
    print(f"Filtered words = {filtered_words}")
    write_to_file(filtered_words)


if __name__ == "__main__":
    main()


