# Comp382: Assignment 1

Attached is my COMP382: Assignment 1 submission with my partner Prasoon Tyagi. I selected to answer the following prompt:

Explain why for some even constant k the language B = {w<sub>1</sub>w<sub>2</sub>...w<sub>n-1</sub>w<sub>n</sub>w<sub>2</sub>w<sub>4</sub>...w<sub>k</sub> | w is a binary string }
is regular.

Prasoon and I decided to write a Python program to prove regularity among various test cases, as well as creating a report explaining the logical explanation of the Binary Non-Deterministic Finite Automaton (BNFA).


# How we split our work:

### Ryan:

* Wrote report in LaTeX, illustrating the Binary NFA State Diagram for Language B in the general case and involving step-by-step logic and explanation of the NFA.

* Wrote formal 5-tuple definition, as well as design choices and justification.

* Revised Prasoon's initial Python Binary Non-Deterministic Finite Automaton implementation.

* Included test cases for even values of k (program accepts k = 2, 4, 6, 8).

* Incorporated user option of inputting a custom binary string, concatenates the proper suffix, and returns the appropriate accepted string. As there is much room for error here, I implemented error handling for values other than binary.


### Prasoon:

* Implemented initial version of Binary NFA program.