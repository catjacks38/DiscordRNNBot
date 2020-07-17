from textgenrnn import textgenrnn
import sys

textgen = textgenrnn('textgenrnn_weights.hdf5')

while(1):
	text = textgen.generate(temperature=float(sys.argv[1]), return_as_list=True)
	
	text = "".join(text)
	
	print(text)
	input("Press Enter to continue...")