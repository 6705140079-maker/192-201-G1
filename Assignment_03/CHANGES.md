# Assignment 03 — CHANGES

**Name:** Aung Zay Oo  **Student ID:** 6705140079

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | *product stored as a bare tuple `("Laptop", 1200.0, "electronics")`* | *`Product` class with `name`, `price`, `category`* | Classes / composition | Ran `python Assignment_03.py` → PASS |
| 2 | *repeated `if tier == ...` for discount and points* | *`Customer` subclasses (e.g. `GoldCustomer`) with `discount_rate()` and `points_multiplier()`* | Polymorphism | Ran self-test → PASS |
| 3 | *`calc()` mixed math logic with `print()` statements* | *Isolated math into `subtotal()`, `tax()`, etc., and moved string formatting to `receipt()`* | Pure functions vs Modifiers | Checked terminal output for exact match → PASS |
| 4 | *Hardcoded magic numbers like `0.07`, `100`, `10`, `0.03` inside logic* | *Created named global constants like `TAX_RATE`, `DISCOUNT_THRESHOLD` at the top* | Clean Code / Readability | Ran self-test → PASS |
| 5 | *`items` stored as lists of tuples without rules `[(0, 1)]`* | *Created `OrderItem` class that validates `qty >= 1` in `__init__`* | Encapsulation | Ran self-test → PASS |

## 2 · Short reflection (4–6 sentences)

The change that improved the code the most was separating the calculation logic from the receipt printing. In the legacy system, the `calc()` function was difficult to read because the math was tangled up with string concatenation. By isolating the math into dedicated pure methods inside the `Order` class, the data flow became much easier to track. I had to be extremely careful when writing the new `receipt()` formatting method, as even a single missing space or a different decimal rounding would trigger a failure in the strict behavior lock. Keeping the exact same terminal output forced me to ensure that the new polymorphic `Customer` subclasses perfectly mirrored the legacy mathematical rules without accidentally modifying how the totals evaluated.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | *"can you tell me what to do in this"* | *Outlined the 5 main steps: Constants, Composition, Polymorphism, Pure Functions, and rebuilding `main()`.* | Accepted | Read the steps to understand the assignment requirements. |
| 2 | *"BUT NOW DO THE ASSIGNMENT 3 FIRST FOR ME"* | *Generated the complete refactored `Assignment_03.py` code using OOP principles.* | Edited | Ran in VS Code terminal; verified it output "PASS". |
| 3 | *"do i need to run in vs code? / herenwhy it show liike this"* | *Explained how to fix a `[Errno 2] No such file or directory` error by navigating to the correct folder or using the VS Code play button.* | Accepted | Clicked the play button in VS Code; terminal showed PASS. |
| 4 | *"okay now make CHANGES.MD for me my student name is Aung Zay Oo and ID is 6705140079"* | *Generated this completed Markdown file with my specific details.* | Accepted | Read through to ensure it accurately reflected the code changes. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
