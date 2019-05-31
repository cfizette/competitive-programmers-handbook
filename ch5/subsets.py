
def _recursive_search(k, n, subset, subsets):
    # Function adds subsets to subsets
    if k == n:
        subsets.append(set(subset))
    else:
        # Create two more subsets, one containing k and one not, continue generating the subsets
        _recursive_search(k+1, n, subset, subsets)
        subset.append(k)
        _recursive_search(k+1, n, subset, subsets)
        subset.pop()

def recursive_serach(n):
    subset = []
    subsets = []
    _recursive_search(0, n, subset, subsets)
    return subsets


def bit_method_search(n):
    # set of n elements can be represented by n bits
    # kind of like one-hot vector
    # this function iterates through all numbers 0 -> 2^n - 1 and
    # uses their bit representations to generate the subsets

    bit_subsets = []
    int_subsets = []

    max_n = 2**n - 1 # could use bit shift here

    for i in range(max_n+1):
        bit_subsets.append(i)

    # Convert bit arrays to sets of integers
    for bits in bit_subsets:
        subset = set()
        for i in range(n):
            if bits & (1<<i): # if there is a 1 in the ith location
                subset.add(i)
        int_subsets.append(subset)
    
    return int_subsets




if __name__ == '__main__':
    print(recursive_serach(3))
    print(bit_method_search(3))