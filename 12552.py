import itertools
from functools import lru_cache

"""
AMM 12552 recursive solution
problem def'n:
Let the alphabet = {0,1,2}
Let Tn = { set of all possible strings length n \ all strings containing the substring '20'}

Find the sum of 1's over all x in Tn
"""

# the brute force stuff
def count_valid(strings):
    return sum("20" not in s for s in strings)

def total_ones_over_valid(strings):
    return sum(s.count('1') for s in strings if "20" not in s)

ALPHABET = "012"

def generate_Tn(n: int, as_set: bool = False):
    """
    Return all length-n strings over {0,1,2}.
    If as_set=True, return a set; otherwise return a list (lexicographic order).
    """
    if n < 0:
        raise ValueError("n must be nonnegative")
    it = (''.join(t) for t in itertools.product(ALPHABET, repeat=n))
    return set(it) if as_set else list(it)

# -------------------

def num_valid_strings(n: int) -> int:
    # S(n) base cases
    if n == 0: return 1       # empty string
    if n == 1: return 3       # "0","1","2"
    return 3*num_valid_strings(n-1) - num_valid_strings(n-2)

@lru_cache(None)
def num_ones(n: int) -> int:
    # O(n) base cases
    if n == 0: return 0
    if n == 1: return 1       # only "1" contributes
    return 3*num_ones(n-1) + num_valid_strings(n-1) - num_ones(n-2)

# ---- quick checks ----
for n in range(0, 8):  # brute force is O(3^n)
    Tn = generate_Tn(n)
    brute_valid = count_valid(Tn)
    brute_ones  = total_ones_over_valid(Tn)
    rec_valid   = num_valid_strings(n)
    rec_ones    = num_ones(n)
    print(f"n={n}: valid  brute={brute_valid:>4}  rec={rec_valid:>4} | ones  brute={brute_ones:>4}  rec={rec_ones:>4}")
    assert brute_valid == rec_valid
    assert brute_ones  == rec_ones

# Example single n
n = 3
Tn = generate_Tn(n)
print("\nExample:")
print("count_valid(Tn)       =", count_valid(Tn))        # expected 21 for n=3
print("num_valid_strings(3)  =", num_valid_strings(3))   # 21
print("total_ones_over_valid =", total_ones_over_valid(Tn))
print("num_ones(3)           =", num_ones(3))            # 25