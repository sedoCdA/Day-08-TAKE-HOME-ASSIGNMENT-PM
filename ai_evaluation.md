# Part C: AI Diamond Pattern — Critical Evaluation

## Exact Prompt Used

> "Write a Python program that prints a diamond pattern of asterisks.
> The user inputs the number of rows for the upper half. Include proper
> spacing and use nested loops only (no string multiplication tricks)."

---

## AI-Generated Code (Original)
```python
n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

---

## Critical Evaluation

### What the AI Got Right

The mathematical logic is correct. The formula for spaces is `(n - i)`
and for asterisks is `(2 * i - 1)`. The output is visually accurate for
any positive integer n. The code is short and easy to read.

### What Was Wrong or Missing

**1. Used string multiplication tricks** — The prompt specifically
said "no string multiplication tricks" but the AI used `" " * (n - i)`
and `"*" * (2 * i - 1)`. This directly violates the requirement.
The whole point of the exercise is to practice nested `for` loops.

**2. No edge case handling** — The AI did not handle:
- `n = 0` → produces no output (should show an error message)
- `n = 1` → produces a single `*` (works, but worth verifying)
- Negative input → crashes with a confusing output
- Non-integer input → crashes with `ValueError`

**3. No function or docstring** — The code is just raw statements
at module level with no function, no docstring, no structure.
This would score very low on code quality in any real review.

**4. No input validation** — `int(input(...))` will crash immediately
if the user types a letter or a float like `3.5`.

**5. Time complexity not considered** — The AI did not mention that
this is O(n²) because for each of the O(n) rows, we print O(n)
characters. For large n this could be slow.

### What I Improved

- Replaced all string multiplication with proper nested `for` loops
- Added input validation with a `while` loop
- Added edge case handling for n=0 and n=1
- Wrapped everything in a function with a docstring
- Added a demo section showing multiple sizes
- Structured the code with a `main()` entry point

### Time Complexity

Both the AI version and my version are **O(n²)** — for n rows, each
row prints up to 2n characters, so total output is proportional to n².
For this kind of pattern problem, O(n²) is unavoidable and acceptable.
