## Pattern Matching Algorithm

This repository contains a Python implementation of an efficient pattern matching algorithm. The algorithm aims to find occurrences of a pattern `p` in a document `x` with a time complexity close to Knuth-Morris-Pratt while using minimal working memory.

### Background

The problem involves finding occurrences of a pattern `p` of length `m` in a document `x` of length `n`. The naive algorithm takes O(mn) time, while the Knuth-Morris-Pratt algorithm improves this to O(m + n) time. However, it uses Θ(mlogm) bits of space. This project aims to design an algorithm with a similar time complexity but using only O(logm + logn) working memory.

### Implementation

- `randPrime(N)`: Returns a random prime number less than or equal to `N`.
- `findN(eps, m)`: Computes an appropriate `N` to satisfy the error bounds.
- `randPatternMatch(eps, p, x)`: Finds occurrences of `p` in `x` with controlled error probability.
- `randPatternMatchWildcard(eps, p, x)`: Finds occurrences of a pattern `p` with wildcards in `x`.



### Example Test Cases

modPatternMatch(1000000007, ‘CD’, ‘ABCDE’)

[2]

modPatternMatch(1000000007, ‘AA’, ‘AAAAA’)

[0, 1, 2, 3]


modPatternMatchWildcard(1000000007, ‘D?’, ‘ABCDE’)

[3]

modPatternMatch(2, ‘AA’, ‘ACEGI’)

[0, 1, 2, 3]

modPatternMatchWildcard(1000000007, ‘?A’, ‘ABCDE’)

[0, 1, 2, 3]





