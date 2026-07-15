# Checksum Policy

Every imported template file should have a sha256 checksum before it is referenced by examples or workflows.

## Why

- Conference templates can change after initial release.
- Users need reproducible paper builds.
- Agents should not silently update style files.

## Record

For each imported file, record:

```text
sha256  relative/path/to/file
```

## Rules

- If upstream changes, create a new import record.
- Do not replace old checksums in place unless correcting an error.
- If a paper project locks a template version, do not update it without explicit user approval.
- If license status is unclear, prefer source reference over committing the file.
