Pattern Matching Algorithm Readme
This repository contains the implementation of an efficient pattern matching algorithm that finds occurrences of a pattern p in a document x. The algorithm aims to achieve a time complexity close to the Knuth-Morris-Pratt algorithm while reducing the working memory to O(logm + logn).

Background
The problem involves finding occurrences of a pattern p of length m in a document x of length n. The naive algorithm takes O(mn) time, while the Knuth-Morris-Pratt algorithm improves this to O(m + n) time. However, it uses Θ(mlogm) bits of space. This project aims to design an algorithm with a similar time complexity but using only O(logm + logn) working memory.

Basic Idea
The algorithm leverages the 26-ary representation of strings over the uppercase Latin alphabet and computes the hash of the pattern p. It uses a prime number q to reduce the memory requirement to O(logq) bits. The algorithm computes the hash of substrings of x and compares them with the hash of p modulo q. This approach introduces false positives, controlled by choosing q carefully.

Design and Implementation
The repository contains Python implementations of the following functions:

randPrime(N): Returns a random prime number less than or equal to N.
findN(eps, m): Computes an appropriate N to satisfy the error bounds.
randPatternMatch(eps, p, x): Finds occurrences of p in x with one-sided error probability at most eps.
randPatternMatchWildcard(eps, p, x): Finds occurrences of a pattern p with wildcards in x.
Evaluation
The correctness of the modPatternMatch function will be assessed using an autograder. Manual grading will evaluate the space and time complexities of the solution, along with the correctness of other components. Theoretical time and space complexities will be considered, ignoring practical differences due to Python's semantics.

Example Test Cases
scss
Copy code
>>> modPatternMatch(1000000007, ‘CD’, ‘ABCDE’)
[2]
>>> modPatternMatch(1000000007, ‘AA’, ‘AAAAA’)
[0, 1, 2, 3]
>>> modPatternMatchWildcard(1000000007, ‘D?’, ‘ABCDE’)
[3]
>>> modPatternMatch(2, ‘AA’, ‘ACEGI’)
[0, 1, 2, 3]
>>> modPatternMatchWildcard(1000000007, ‘?A’, ‘ABCDE’)
[0, 1, 2, 3]
Submission
Please ensure that your implementation of modPatternMatch, modPatternMatchWildcard, and findN are completed in the provided a4.py file before submission.

For any queries or clarifications, feel free to reach out.

Best regards,
[Your Name]