# File Permission Errors and Recovery

## 1. Purpose

This document addresses NEITO evaluation
criterion 15: file permission errors,
write failures, exception handling,
data protection, and recovery procedures.

## 2. Relevant Source Files

- [storage.py](../storage.py)
- [main.py](../main.py)
- [Permission error tests](../tests/test_permission_errors.py)

QuizStorage handles persistent JSON data.

The console interface handles errors reported
by the storage layer.

## 3. PermissionError and OSError

PermissionError is a subclass of OSError.

Permission errors can occur when:

- A file cannot be read.
- A directory cannot be written.
- A temporary file cannot be created.
- A destination file cannot be replaced.
- Another application prevents file replacement.
- Operating system access permissions deny an operation.

The existing save_state() function catches
OSError, ValueError, and RuntimeError.

Therefore, PermissionError is handled by the
existing OSError exception handler.

PermissionError is not treated as corrupt JSON.

## 4. Read Permission Error

QuizStorage.load() propagates permission errors
to the application-level error handler.

A permission error must not be interpreted as
a missing or corrupted state file.

The existing file must be preserved.

Recovery procedure:

1. Check that state.json exists.
2. Check file and directory read permissions.
3. Close applications preventing access.
4. Restore authorized read access.
5. Restart the quiz application.
6. Confirm that saved questions and scores load.

Do not delete the existing state file merely
because access is denied.

## 5. Write Permission Error

A write operation may fail because the
destination directory is read-only or
access is otherwise denied.

The application reports a save failure
and returns False from save_state().

The current game object remains available
in memory while the application is running.

A failed save does not mean that the latest
changes have been persisted to disk.

## 6. Atomic File Replacement

The existing storage implementation:

1. Validates the game data.
2. Creates the destination directory if needed.
3. Writes JSON to state.json.tmp.
4. Flushes the temporary file.
5. Calls os.fsync().
6. Calls os.replace() to replace state.json.
7. Attempts to remove any remaining temporary file.

If writing or replacement fails before
the replacement succeeds, the original
state file remains unchanged in the
tested scenarios.

Atomic replacement reduces the risk of
leaving partially written JSON in the
destination file.

It does not guarantee recovery from
every possible operating system,
hardware, or concurrent-write failure.

## 7. User Recovery Procedure

If the application reports a save failure:

1. Keep the application running if possible.
2. Read the displayed error message.
3. Check authorized write permissions.
4. Check the available disk space.
5. Close applications locking the file.
6. Restore access to the destination folder.
7. Select Exit again to retry saving.
8. Confirm the save-completed message.
9. Restart the application.
10. Confirm that the saved data is restored.

Do not forcibly terminate the application
while important unsaved changes remain
in memory.

If access cannot be restored, seek assistance
from the system administrator.

Avoid changing unrelated security permissions.

## 8. Error Handling Matrix

| Scenario | Handling | Recovery |
|---|---|---|
| Missing state file | Load defaults | Save normally |
| Invalid JSON | Backup and restore defaults | Inspect backup |
| Read permission denied | Propagate error | Restore read access |
| Directory permission denied | Report save failure | Restore folder access |
| Temporary write denied | Report save failure | Restore write access |
| File replacement denied | Preserve original in tested case | Release lock and retry |
| Save failure | Retain active game data | Retry before exit |
| Successful retry | Persist latest data | Reload and verify |

## 9. Permission Error Test Design

The regression tests use Python's standard
unittest and unittest.mock modules.

PermissionError is injected at selected
file-system operation boundaries.

All test state files are created in isolated
temporary directories.

The user's actual state.json is not used
as the test destination.

| Test | Verification |
|---|---|
| 01 | PermissionError inheritance |
| 02 | Read denial and original preservation |
| 03 | Temporary file write denial |
| 04 | Destination replacement denial |
| 05 | Directory creation denial |
| 06 | Console error message and memory retention |
| 07 | Save retry after permission restoration |
| 08 | Reload after successful retry |

## 10. Reproduction Commands

Run the permission-specific tests:

    python -m unittest discover -s tests -p "test_permission_errors.py" -v

Run all regression tests:

    python -m unittest discover -s tests -v

The expected test count is 156:
148 baseline tests and 8 new permission tests.

Actual pass counts must be taken from
the recorded execution logs.

## 11. Test Scope and Limitations

These tests simulate permission errors
using unittest.mock.

They do not modify Windows NTFS access
control lists or real file ownership.

They do not reproduce every operating
system-specific file locking behavior.

Cleanup itself can fail if permission
to remove the temporary file is denied.

In that case, a temporary file may remain
and require inspection after access
has been restored.

Concurrent application writers are not
covered by this test design.

## 12. Evaluation Mapping

NEITO criterion 15 is addressed through:

- Explicit PermissionError explanation.
- Read and write failure handling.
- User-visible error reporting.
- Original file preservation tests.
- Permission restoration and retry.
- Successful data reload verification.
- Reproducible automated tests.

Actual execution evidence will be linked
from the consolidated evaluation document
after revision verification.
