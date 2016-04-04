def load_sequences(filename):
    list_of_seqs = []
    
    fp = open(filename)
    for count, line in enumerate(fp):
        if (count % 4) == 1:
            seq = line.strip()
            list_of_seqs.append(seq)
    return list_of_seqs

def count_Ns(seq):
    # only valid input should be strings of ACGTN
    n_bases = len(seq)
    # Fixed to handle lower-case
    #  1) convert seq to be upper case
    #  2) count lower case 'n's as well

    seq = seq.upper()  # handle lower case input
    
    
    good_bases = seq.count('A') + seq.count('C') + seq.count('G') + \
        seq.count('T') + seq.count('N')
    
    # Error handling
    if len(seq) != good_bases:
        raise ValueError("error, sequence contains non-DNA")
    
    
    n_ns = seq.upper().count('N')
    return (n_bases, n_ns)




def count_Ns_case(seq):
    n_bases = len(seq)
    n_ns = seq.upper().count('N')
    return (n_bases, n_ns)

## Testing & Automated Tests

# Create an initial test function
def test_count_ns():
    seq = "NATGC"
    nb, nn = count_Ns(seq)
    
    assert nb==5, "nb should be 5"
    assert nn==1

    
# Create a new test function: lower case input
def test_count_ns_2():
    seq = "nATGC"
    nb, nn = count_Ns_case(seq)
    
    assert nb==5, "nb should be 5"
    assert nn==1

    
def test_bad_input():
    print('running test_count_ns')
    seq = "nATGCmy favorite sequence"
    
    # Runs correctly if there is an error
    #  Throws an error if the input is correct 
    try:
        nb, nn = count_Ns(seq)
        assert False, "count_Ns should break on this input"
    except ValueError:
        pass

    

# test_count_ns() # This runs every time jfaUtils.py is IMPORTED

# This fixes it so that when jfaUtils.py is run as a script 
# at the command line

