#!/usr/bin/env python3

from fnmatch import filter
from random import choice
import re

def run():
    with open('files.txt') as files:
        all_files = files.readlines()
    for batch in batchify(all_files):
        print(len(batch))

def batchify(all_files, max_files=20):
    if len(all_files) < max_files:
        return all_files
    batch = bundle(all_files[0], all_files, all_files[1:])
    new_files = list(set(all_files) - set(batch))
    yield batch
    yield from batchify(new_files, max_files)

def bundle(match, all_files, old_matches, max_files=20):
    print(match)
    matches = filter(all_files, match)
    if len(matches) > max_files:
        return old_matches
    if len(matches) == max_files:
        return matches

    new_match = match.strip()[0:-1] + '*'
    nonwild = [x for x, _ in enumerate(new_match) if x != '*']
    replace = choice(nonwild)
    new_match = new_match[:replace] + '*' + new_match[replace+1:]
    new_match = re.sub('\**\*','*', new_match)
    return bundle(new_match, all_files, matches)


if __name__ == '__main__':
    run()
