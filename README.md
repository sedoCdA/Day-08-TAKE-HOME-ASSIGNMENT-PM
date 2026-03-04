# Day 8 PM — Loops: for, while, break, continue, nested loops

**Course:** AI/ML Bootcamp
**Session:** Day 8 · PM
**Due:** Fri 06/03/2026 — 7:15pm

---

## Files

| File | Part | Description |
|------|------|-------------|
| `password_analyzer.py` | A | Password strength analyzer + generator |
| `interview_answers.md` | B | break/continue, loop-else, pairs, is_prime fix |
| `diamond_pattern.py` | C | Diamond pattern using nested loops only |
| `ai_evaluation.md` | C | AI prompt, output, and critical evaluation |
| `transaction_analyzer.py` | D | Paytm transaction dashboard (bonus) |

---

## Part A — Password Analyzer & Generator
```bash
python password_analyzer.py
```

**Scoring system:**

| Criteria | Points |
|----------|--------|
| Length ≥ 8 | +1 |
| Length ≥ 12 | +2 |
| Length ≥ 16 | +3 |
| Has uppercase | +1 |
| Has lowercase | +1 |
| Has digit | +1 |
| Has special char (!@#$%^&*) | +1 |
| No 3+ repeats in a row | +1 |

**Strength ratings:** Weak (0-2) / Medium (3-4) / Strong (5-6) / Very Strong (7+)

Uses a `while` loop to keep asking until score ≥ 5.

---

## Part B — Interview Answers

See `interview_answers.md` for:
- `break` vs `continue` with examples
- Loop `else` clause explained with search pattern use case
- `find_pairs()` — O(n²) nested loops and O(n) set versions
- `is_prime()` bug fixed — O(n) → O(√n) optimisation

---

## Part C — Diamond Pattern
```bash
python diamond_pattern.py
```

Uses **nested `for` loops only** — no string multiplication.

Example output for `rows = 4`:
```
   *
  ***
 *****
*******
 *****
  ***
   *
```

See `ai_evaluation.md` for the full critique of the AI-generated version.

---

## Part D — Transaction Analyzer (Bonus)
```bash
python transaction_analyzer.py
```

Features:
- `while` loop accepts transactions until user types `done`
- Flags any transaction > ₹10,000 as high value
- Bar chart of last 10 transactions (★ = ₹1,000)
- Category spending breakdown (food/travel/bills/other)
- Full summary: credits, debits, net balance, average, highest

---

## Concepts Covered

| Concept | Where used |
|---------|-----------|
| `for` loop with `range()` | Password scoring, pattern printing |
| `for` loop with `enumerate()` | Transaction bar chart |
| `while` loop | Password input loop, transaction collector |
| `break` | Exit while loop when password is strong enough |
| `continue` | Skip invalid inputs |
| `loop-else` | Explained in interview answers with search example |
| Nested loops | Diamond pattern (upper + lower half) |
| O(n) vs O(n²) | find_pairs and is_prime optimisations |

---

## Code Quality
- ✅ PEP 8 — snake_case throughout
- ✅ All functions have docstrings
- ✅ Input validation on every field
- ✅ No hardcoded values — uses constants
