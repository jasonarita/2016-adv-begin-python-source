def load_sequences(filename):
    list_of_seqs = []
    
    fp = open(filename)
    for count, line in enumerate(fp):
        if (count % 4) == 1:
            seq = line.strip()
            list_of_seqs.append(seq)
    return list_of_seqs

def count_Ns(seq):
    n_bases = len(seq)
    n_ns = seq.count('N')
    return (n_bases, n_ns)
