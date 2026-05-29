# TDD Discipline

Use this reference when a feature or bug fix needs tests, regression coverage, or a new behavior contract.

## Core principle

Tests should verify behavior through public interfaces, not implementation details.

Good tests survive internal refactors because they assert what the system does. Bad tests mock internal collaborators, inspect private state, or assert the current shape of an implementation.

## Avoid horizontal slicing

Do not write all tests first and then all implementation.

```text
Wrong:
  RED: test1, test2, test3, test4
  GREEN: impl1, impl2, impl3, impl4

Right:
  RED -> GREEN: test1 -> impl1
  RED -> GREEN: test2 -> impl2
  RED -> GREEN: test3 -> impl3
```

Horizontal slicing creates tests for imagined behavior and locks in guessed interfaces too early.

## Tracer bullet loop

Use vertical slices:

1. Choose one observable behavior.
2. Write one test for that behavior through the public interface.
3. Run it and confirm it fails for the expected reason.
4. Implement the smallest code path that makes it pass.
5. Run the test again.
6. Repeat for the next behavior.

Never refactor while red. Get to green first, then improve structure in small steps with tests passing after each step.

## Test surface rules

- The interface is the test surface.
- Prefer integration-style tests that exercise real code paths.
- Mock at external boundaries, not internal module boundaries.
- Assert domain behavior, contract outputs, error modes, and side effects users can observe.
- Do not add tests that pass when the real behavior is broken.
- If no correct seam exists for a regression, record that as a testability finding instead of writing a misleading shallow test.

## Deep-module heuristic

During refactor, look for modules where the interface is almost as complex as the implementation. Deepen only when it improves locality or leverage:

- Locality: changes, bugs, and knowledge concentrate in one place.
- Leverage: callers get more behavior through a simpler interface.

Use the deletion test: if deleting a module makes complexity disappear, it may be a pass-through; if complexity reappears across many callers, the module was earning its keep.

## Per-cycle checklist

```md
- Test describes behavior, not implementation:
- Test uses public interface:
- Test fails for the expected reason:
- Code is minimal for this behavior:
- No speculative behavior added:
- Verification command:
```
