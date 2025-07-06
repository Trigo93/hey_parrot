import sys
import os
from contextlib import contextmanager

@contextmanager
def suppress_olympe_logs():
    stderr_fileno = sys.stderr.fileno()

    # Save the current stderr
    saved_stderr = os.dup(stderr_fileno)

    # Redirect stderr to null
    with open(os.devnull, 'w') as null:
        os.dup2(null.fileno(), stderr_fileno)
        try:
            yield
        finally:
            # Restore original stderr
            os.dup2(saved_stderr, stderr_fileno)
            os.close(saved_stderr)
