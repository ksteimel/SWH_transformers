__author__ = "Kenneth Steimel"
__date__ = "2022-03-19"

from pathlib import Path
from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing

# Initialize a basic BPE tokenizer
tokenizer = ByteLevelBPETokenizer()

# Point to the file path for training data
file_path = "/mnt/data/corpora/swh/train.txt"
# These special tokens are used by roberta-like models such the model that
# will be trained using this tokenizer.
special_tokens = ["<s>", "<pad>", "</s>", "<unk>", "<mask>"]
# Train the tokenizer with a vocab size of 52,000 and the specified special tokens.
tokenizer.train(files=[file_path], vocab_size=52000, min_frequency=2, 
                special_tokens=special_tokens)
tokenizer.save_model(".", "swh_basic_bpe")
