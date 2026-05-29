# Raw-agent prompt

This is the prompt a hurried user typically gives a coding agent. It invites a
fast symptom patch with no repo orientation.

```text
Checkout is throwing "ValueError: discount_fraction must be in [0, 1], got 20"
when I apply a 20% discount. Fix it.
```

## Likely raw-agent outcome

Without a workflow, the agent often jumps to the nearest line in the traceback
(`compute_total_cents` in `src/pricing.py`) and applies one of these symptom
patches:

- Loosen or remove the `0.0 <= discount_fraction <= 1.0` guard.
- Clamp the result with `max(total, 0)`.
- Divide by 100 *inside* `compute_total_cents`.

Each "works" for the reported input but is wrong:

- It silently breaks the documented domain contract (`discount_fraction` is a
  fraction in `[0, 1]`).
- It corrupts every other caller that already passes a correct fraction
  (a `0.20` discount would now become a `0.002` discount).
- It leaves the real defect — a unit mismatch at the request boundary — in
  place.

Compare with `engineering-team.md`.
