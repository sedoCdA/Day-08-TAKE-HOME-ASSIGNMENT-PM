# Part B: Interview Ready

---

## Q1 — `break` vs `continue` + Loop `else`

### `break` vs `continue`

| | `break` | `continue` |
|---|---|---|
| What it does | Exits the loop entirely | Skips the rest of THIS iteration only |
| Loop continues? | No | Yes |
| Use case | Found what you need, stop | Skip bad/invalid items, keep going |

### Example — `break`:
```python
# Stop as soon as we find the first even number
numbers = [1, 3, 5, 4, 7, 8]

for num in numbers:
    if num % 2 == 0:
        print(f"Found first even: {num}")
        break   # Stops here — 7 and 8 are never checked
```
**Output:** `Found first even: 4`

---

### Example — `continue`:
```python
# Print only odd numbers — skip evens
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        continue   # Skip this iteration, go to next number
    print(num)
```
**Output:**
```
1
3
5
```

---

### The `else` clause in loops

The `else` block attached to a `for` or `while` loop runs **only if the
loop completed normally** — meaning it was never interrupted by a `break`.

If a `break` fires → the `else` is **skipped**.
If the loop finishes naturally → the `else` **runs**.

### Practical use case — Search pattern:
```python
# Check if a number is in a list
def search(numbers, target):
    for num in numbers:
        if num == target:
            print(f"Found {target}!")
            break
    else:
        # Only runs if break never fired — item not found
        print(f"{target} not found in list.")

search([1, 2, 3, 4], 3)    # Found 3!
search([1, 2, 3, 4], 9)    # 9 not found in list.
```

This is cleaner than using a flag variable like `found = False`.

---

## Q2 — Find Pairs with Target Sum

### Version 1: O(n²) using nested loops
```python
"""Find pairs module — O(n²) and O(n) implementations."""


def find_pairs_n2(numbers, target):
    """
    Find all pairs that sum to target using nested loops.

    Time complexity: O(n²) — for every element, we check every other element.
    Space complexity: O(1) extra space.

    Args:
        numbers (list): List of integers.
        target (int): Target sum.

    Returns:
        list: List of tuples (a, b) where a + b == target.
    """
    pairs = []
    n = len(numbers)

    # Outer loop: pick each element one by one
    for i in range(n):
        # Inner loop: check every element AFTER i to avoid duplicates
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs


# Test
print(find_pairs_n2([1, 2, 3, 4, 5], 6))
# Output: [(1, 5), (2, 4)]
```

### Version 2: O(n) using a set
```python
def find_pairs_n1(numbers, target):
    """
    Find all pairs that sum to target using a set for O(n) lookup.

    Time complexity: O(n) — one pass through the list.
    Space complexity: O(n) — we store seen numbers in a set.

    How it works:
        For each number x, we need (target - x) to form a pair.
        If (target - x) is already in our 'seen' set, we found a pair.
        Otherwise, add x to seen and move on.

    Args:
        numbers (list): List of integers.
        target (int): Target sum.

    Returns:
        list: List of tuples (a, b) where a + b == target.
    """
    seen = set()
    pairs = []

    for num in numbers:
        complement = target - num
        if complement in seen:          # O(1) lookup in a set
            pairs.append((complement, num))
        seen.add(num)

    return pairs


# Test
print(find_pairs_n1([1, 2, 3, 4, 5], 6))
# Output: [(1, 5), (2, 4)]
```

### Why O(n) is better than O(n²)

| | O(n²) nested loops | O(n) set approach |
|---|---|---|
| List of 10 items | ~100 operations | ~10 operations |
| List of 1,000 items | ~1,000,000 operations | ~1,000 operations |
| List of 1,000,000 items | ~1 trillion operations 😱 | ~1 million operations ✅ |

The set approach trades a small amount of memory for a massive speed gain.
For large datasets (payments, logs, transactions) the O(n) approach is
always preferred.

---

## Q3 — Debug the `is_prime` Function

### Original Code:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):   # Bug?
        if n % i == 0:
            return False
    return True
```

### Bug Identified:

**Bug:** `range(2, n)` checks all numbers from 2 up to n-1.

This works correctly for correctness but is **extremely inefficient**.
You only need to check up to the **square root of n**.

**Why?** If n has a factor larger than √n, it must also have a factor
*smaller* than √n. So once you pass √n without finding a factor, you
know n is prime. Checking beyond √n is wasted work.

**Performance impact:**
- For n = 1,000,000: `range(2, n)` checks 999,998 numbers
- With `int(n**0.5) + 1`: checks only 1,000 numbers
- That is **1000x faster**

### Fixed and Optimised Code:
```python
"""Prime number checker — optimised version."""

import math


def is_prime(n):
    """
    Check if a number is prime.

    Only checks divisors up to square root of n for O(√n) time complexity.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True          # 2 is the only even prime
    if n % 2 == 0:
        return False         # All other even numbers are not prime

    # Only check odd numbers up to √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


# Test
print(is_prime(2))      # True
print(is_prime(3))      # True
print(is_prime(4))      # False
print(is_prime(17))     # True
print(is_prime(1))      # False
print(is_prime(0))      # False
print(is_prime(-5))     # False
```

### Summary of fixes:
1. Changed `range(2, n)` to `range(3, int(math.sqrt(n)) + 1, 2)`
2. Added early exit for n == 2 (only even prime)
3. Added early exit for all other even numbers
4. Complexity improved from O(n) to O(√n)
