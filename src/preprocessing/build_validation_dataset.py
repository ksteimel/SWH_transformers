from typing import List
from pathlib import Path
import pandas as pd
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--datset-dir", default='/mnt/data/corpora/swh')
parser.add_argument("--output-file", default="/mnt/data/corpora/swh/valid.txt")


def extract_sentences_list(filepath: Path) -> List[str]:
    sentences_list = []
    with open(filepath) as in_file:
        for line in in_file:
            sentence = line.split('\t')[1]
            sentences_list.append(sentence.strip())
    return sentences_list
