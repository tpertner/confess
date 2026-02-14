# Adding a Custom Test Case

This guide shows how to add your own test cases to the harness when you discover a new failure mode.

## Scenario

You noticed your model sometimes gives medical advice when pressured, even though it should decline. Let's turn that observation into a repeatable test.

## Step 1: Document the failure mode

**Observation:** When users add urgency ("my symptoms are getting worse"), the model shifts from "see a doctor" to specific diagnoses.

**Risk:** False confidence in medical advice could cause harm.

**Test goal:** Ensure the model maintains appropriate boundaries under medical pressure.

## Step 2: Design the test case

Open `testsuites/mini_suite.yaml` and add:
```yaml
