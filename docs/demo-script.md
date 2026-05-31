# Demo Script

Two scripts for showing EngineeringTeam, plus the lone-agent vs expert-team
contrast. The worked example lives in `examples/buggy-python-service/`.

## 60-second demo

**Goal:** show that EngineeringTeam selects the right expert panel, proves shared understanding, then edits only the correct seam.

1. Open `examples/buggy-python-service/`. Show the green suite:

   ```bash
   cd examples/buggy-python-service
   python3 -m unittest discover -s tests -v
   ```

   Talking point: "Suite is green. Looks fine."

2. Reproduce the hidden bug:

   ```bash
   python3 -c "from src.api import checkout; print(checkout({'items':[{'name':'w','unit_price_cents':1000,'quantity':2}],'discount_percent':20}))"
   ```

   Output:

   ```text
   ValueError: discount_fraction must be in [0, 1], got 20
   ```

3. Paste the prompt from `examples/buggy-python-service/prompts/engineering-team.md`.

   Talking point: "Instead of acting like a lone implementer patching the traceback, the lead routes codebase, contract, evidence, and verification lenses. The panel proves the units mismatch — then fixes the adapter, not the guard."

## 5-minute demo

1. **Frame the problem (30s).** A lone agent patches the first symptom. On legacy
   code that creates new bugs. EngineeringTeam behaves like a small expert panel:
   lead engineer, codebase investigator, evidence skeptic, and verification engineer
   join only because this task needs those lenses. Show `prompts/raw-agent.md` and
   the three tempting symptom patches it lists.

2. **Run the raw-agent prompt (60s).** Optional: let a raw agent loosen the
   `[0,1]` guard. Show that the reported case passes but the domain contract is
   now broken for every correct caller.

3. **Run the EngineeringTeam prompt (2m).** Walk through how the lead selects the
   useful experts and how their artifacts build shared understanding, comparing to
   `examples/buggy-python-service/expected-artifacts/`:
   - Repo Atlas: two layers, `unittest`, run command.
   - Component Brief: owning path is `checkout` → `compute_total_cents`.
   - Contract Graph: the `checkout → compute_total_cents` edge carries a
     percentage where a fraction is required.
   - Evidence Ledger: contract proven by docstring + guard; defect proven by
     `src/api.py`; coverage gap proven by `test_api.py`.

4. **Show the fix (60s).** Convert at the boundary (`discount_percent / 100`),
   add a regression test, rerun the suite:

   ```bash
   python3 -m unittest discover -s tests -v
   ```

5. **Close (30s).** The diff is one line plus a test, but the artifacts prove
   *why* it is correct and safe — that is the reviewable difference.

## Lone agent vs expert EngineeringTeam

| Dimension | Lone agent | EngineeringTeam |
|---|---|---|
| First move | Edit the line in the traceback | Lead routes a focused expert panel |
| Orientation | Local traceback only | Codebase investigator maps repo and call path |
| Where it edits | `src/pricing.py` guard (wrong seam) | `src/api.py` boundary (right seam) |
| Contract awareness | None | Contract graph shows the mismatch |
| Evidence | Implicit | Evidence skeptic forces a ledger with confidence |
| Blast radius | Breaks other callers | Localized, contract preserved |
| Verification | "It runs" | Verification engineer adds regression test + full suite |
| Reviewability | Diff only | Panel routing, atlas, brief, contract graph, evidence, verification |

## Expected talking points

- Green tests are not proof of correctness; coverage gaps hide contract bugs.
- The cheapest correct fix is often at a boundary, not at the crash site.
- The artifacts make the panel's reasoning inspectable: who was needed, what they
  learned, and why the change is trustworthy.
