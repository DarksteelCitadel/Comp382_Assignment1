class LanguageBinaryNFA:
    def __init__(self, k):
        if k % 2 != 0 or k < 2:
            print("k must be an even integer greater than or equal to 2.")
            raise ValueError("Invalid value for k.")
        self.k = k

    def accepts(self, input_string):
        """
        Simulates the NFA for language B.
        Returns True if accepted, False otherwise.
        """

        # Input must be long enough to contain k chars + k/2 suffix
        if len(input_string) < self.k + self.k // 2:
            return False

        # Split: w is everything except the last k/2 characters
        split = len(input_string) - self.k // 2
        w = input_string[:split]
        suffix = input_string[split:]

        # Suffix must have exactly k/2 symbols
        if len(suffix) != self.k // 2:
            return False

        # w must be at least length k (not the other way around!)
        if len(w) < self.k:
            return False

        # Remember w2, w4, ..., wk (positions 2, 4, 6, ..., k in w)
        remembered_w = []
        for i in range(2, self.k + 1, 2):
            remembered_w.append(w[i - 1])  # zero-indexed


        # Verify suffix matches remembered positions
        if remembered_w == list(suffix):
            return True

        return False


# Enter value for even k

print("Please enter an even integer greater than or equal to 2 for k (currently supported k=2,4,6,8):")
k = int(input().strip())
nfa = LanguageBinaryNFA(k)


## Provided test cases for k=2,4,6,8 ##

test_cases = [ ## test_str, expected_bool, description, test_k ## 
    # k=2 test cases
    ("000", True, "k=2: w=00, suffix=0", 2),
    ("111", True, "k=2: w=11, suffix=1", 2),
    ("010", False, "k=2: w=01, suffix=0 (wrong! suffix should be 1)", 2),

    
    # k=4 test cases
    ("011111", True, "k=4: w=0111, suffix=11 (positions 2,4 are 1,1)", 4),
    ("100000", True, "k=4: w=1000, suffix=00 (positions 2,4 are 0,0)", 4),
    ("110010", True, "k=4: w=1100, suffix=10 (positions 2,4 are 1,0)", 4),
    ("011110", False, "k=4: w=0111, suffix=10 (wrong! suffix should be 11)", 4),
    
    # k=6 test cases
    ("01110000110", True, "k=6: w=01110000, suffix=110 (positions 2,4,6 are 1,1,0)", 6),
    ("1010101010001", False, "k=6: w=1010101010, suffix=001 (wrong! suffix should be 000)", 6),
    
    # k=8 test cases
    ("010101011111", True, "k=8: w=01010011, suffix=1101 (pos 2,4,6,8 = 1,1,0,1)", 8),
    ("0000111010011100011", False, "k=8: w=000011001001110, suffix=0011 (wrong! suffix should be 0010)", 8)
]

print(f"\nTesting provided test cases with k={k}:\n")
matching_tests = [t for t in test_cases if t[3] == k]
if not matching_tests:
    print(f"No test cases available for k={k}. Try k=2, 4, 6, or 8.")
else:
    for test_str, expected, description, test_k in matching_tests:
        result = nfa.accepts(test_str)
        print(f"{test_str:20} -> {'ACCEPTED' if result else 'REJECTED':8} | {description}")

## Custom user input test

print(f"\nEnter a custom string w to test k={k} (or press Enter to skip):")
custom_w = input().strip()
if custom_w:
    # Compute expected suffix
    char = ''
    if any(char not in '01' for char in custom_w):
        print("Input string must be binary (only '0' and '1').")
    else:
        
        if len(custom_w) >= k:
            expected_suffix = ''.join(custom_w[i-1] for i in range(2, k+1, 2))
            full_string = custom_w + expected_suffix
            print(f"For w='{custom_w}', expected full string: '{full_string}'")
            result = nfa.accepts(full_string)
            print(f"Result: {'ACCEPTED' if result else 'REJECTED'}")
        else:
            print(f"w must be at least length {k}.")
    




