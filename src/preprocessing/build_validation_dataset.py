from typing import List
from pathlib import Path
import pandas as pd
import sys
from tqdm import tqdm
from argparse import ArgumentParser


def extract_sentences_list(filepath: Path) -> List[str]:
    sentences_list = []
    with open(filepath) as in_file:
        for line in in_file:
            sentence = line.split('\t')[1]
            sentences_list.append(sentence.strip())
    return sentences_list


def main():
    argv = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument("--dataset-dir", type=Path, default='/mnt/data/corpora/swh')
    parser.add_argument("--train-dataset", type=Path, default="/mnt/data/corpora/swh/train.txt")
    parser.add_argument("--output-file", type=Path, default="/mnt/data/corpora/swh/valid.txt")
    args = parser.parse_args(argv)
    sentences_list = []
    assert args.dataset_dir.exists()
    for file in args.dataset_dir.glob("swa_*/*-sentences.txt"):
        sentences_list += extract_sentences_list(file)

    print(f"Number of extracted sentences: {len(sentences_list)}")
    sentences_list.sort()
    assert args.train_dataset.exists()
    # Load train dataset and remove any sentences in val that are already in train.
    removed_count = 0
    with open(args.train_dataset) as train_fp:
        train_dataset_length = sum([1 for line in train_fp])
        train_fp.seek(0)
        for line in tqdm(train_fp, total=train_dataset_length):
            line = line.strip()
            try:
                match_index = sentences_list.index(line)
                sentences_list.pop(match_index)
                removed_count += 1
            except ValueError:
                continue

    print(f"Number of validation sentences removed: {removed_count}")
    print(f"Number of validation sentences remaining: {len(sentences_list)}")
    with open(args.output_file, "w") as out_file:
        for sentence in sentences_list:
            out_file.write(sentence + "\n")


if __name__ == '__main__':
    main()