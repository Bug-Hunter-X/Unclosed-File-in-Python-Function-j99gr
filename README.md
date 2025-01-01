# Unclosed File Bug in Python

This repository demonstrates a common, yet easily overlooked, bug in Python: failing to close a file after opening it. The `bug.py` file contains a function that opens a file but forgets to close it using `f.close()`. This can lead to resource leaks and, in some cases, data corruption.

The solution, provided in `bugSolution.py`, shows the correct way to handle file operations, using a `with` statement to ensure the file is automatically closed, even if errors occur.  See the `solutionContent` for specifics.  This approach guarantees resource cleanup. 