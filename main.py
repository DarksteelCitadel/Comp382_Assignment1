class LanguageBNFA:
    def init(self, k):
        if k % 2 != 0 or k < 2:
            raise ValueError("k must be an even integer ≥ 2")
        self.k = k

    def accepts(self, input_string):
        """
        Simulates the NFA for language B.
        Returns True if accepted, False otherwise.
        """

        # Input must be long enough to contain w and the suffix
        if len(input_string) < self.k:
            return False

        # Step 1: nondeterministically guess where w ends
        # Try all possible splits: input = w + suffix
        for split in range(self.k, len(input_string) + 1):
            w = input_string[:split]
            suffix = input_string[split:]

            # Suffix must have exactly k/2 symbols
            if len(suffix) != self.k // 2:
                continue

            # Step 2: remember w2, w4, ..., wk
            remembered = []
            try:
                for i in range(2, self.k + 1, 2):
                    remembered.append(w[i - 1])  # zero-based index
            except IndexError:
                continue

            # Step 3: verify suffix
            if remembered == list(suffix):
                return True

        return False


-----------------------
Example usage
-----------------------
nfa = LanguageBNFA(k=4)

tests = [
    "011111",  # w=0111, suffix=11 -> accept
    "100000",  # w=1000, suffix=00 -> accept
    "110010",  # w=1100, suffix=10 -> accept
    "011110",  # incorrect suffix -> reject
]

for t in tests:
    print(t, "ACCEPT" if nfa.accepts(t) else "REJECT")