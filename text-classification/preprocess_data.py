# Note: This example code is written for Python 3.6+!
import sys
import json
from pathlib import Path

reviews_data = Path(sys.argv[1])
fasttext_data = Path(sys.argv[2])

with reviews_data.open() as input, fasttext_data.open("w") as output:
    for line in input:
        review_data = json.loads(line)

        rating = review_data['stars']
        text = review_data['text'].replace("\n", " ")

        fasttext_line = "__label__{} {}".format(rating, text)

        output.write(fasttext_line + "\n")
