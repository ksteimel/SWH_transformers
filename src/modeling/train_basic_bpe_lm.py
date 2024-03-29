import os
import tokenizers
from tokenizers.implementations import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing
from transformers import RobertaConfig
from transformers import RobertaTokenizerFast
from transformers import RobertaForMaskedLM
from transformers import LineByLineTextDataset
from transformers import DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
from transformers import EarlyStoppingCallback

import torch
# Set up the neural network parameters
config = RobertaConfig(
    vocab_size=52000,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1
)
model_save_path = "./models/swh_basic_bpe"
# Load tokenizer generated by tokenizers/train_basic_bpe_tokenizer.py
tokenizer = RobertaTokenizerFast.from_pretrained(model_save_path, max_len=512)
model = RobertaForMaskedLM(config=config)
# Create a dataset to process each line in the training data
# TODO: rewrite this dataset to be lazy, this currently loads everything into memory which
# consumes a large amount of ram.
train_dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path="/mnt/data/corpora/swh/train.txt",
    block_size=512
)
validation_dataset = LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path="/mnt/data/corpora/swh/valid.txt",
    block_size=512
)
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=True, mlm_probability=0.15
)
early_stopper = EarlyStoppingCallback(early_stopping_patience=2,
                                      early_stopping_threshold=0.05
        )
checkpoint_path = model_save_path + "_checkpoints"
training_args = TrainingArguments(
    output_dir=checkpoint_path,
    overwrite_output_dir=False,
    num_train_epochs=50,
    per_device_train_batch_size=16,
    #save_steps=10_000,
    save_strategy="epoch",
    gradient_accumulation_steps=2,
    save_total_limit=2,
    prediction_loss_only=True,
    evaluation_strategy="epoch",
    load_best_model_at_end=True
)
print(f"Training dataset length: {len(train_dataset.examples)}")
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=validation_dataset,
    callbacks=[early_stopper]
)
# Train the thing and monitor progress
trainer.train()
# Save the trained model so we can load it later
trainer.save_model(model_save_path)
