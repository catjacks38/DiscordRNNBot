from textgenrnn import textgenrnn
import sys

textgen = textgenrnn()

textgen.train_from_file('Dataset Path', num_epochs=int(sys.argv[1]), batch_size=1024)

textgen.generate(5, temperature=1.0)

