DATA_DIR=/mnt/data/corpora/swh
cat $DATA_DIR/*/sw.tok | sed -e 's/[[:space:]]*$//' | sort -u | tqdm > $DATA_DIR/train.txt
num_words=`wc -w $DATA_DIR/train.txt`
num_types=`cat $DATA_DIR/train.txt | tr ' ' '\n' | sort -u | wc -l | tqdm`
echo "Train dataset contains $num_words words"
echo "Train dataset contains $num_types unique words"