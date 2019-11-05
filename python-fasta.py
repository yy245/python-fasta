import sys

def read_fasta(filename):
    """
    Read in a file in FASTA format
    """
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            seq = seq + line #only keep the line if it's not an identifier line that begins with '>'
    f.close()
    return seq

if len(sys.argv) < 2:
	print ("Need to provide filename as argument")
	exit(1)

print(read_fasta(sys.argv[1]))


#test 
