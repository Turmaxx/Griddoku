# Griddoku
A Simple Sudoku Solver on the terminal written in Python using [Recursive Backtracking][backtracking] that reads from `(9x9)` sudoku grid from a specifed text file as a commandline argument, it then solves the grid and prints grid on the terminal.

## Requirements
- Python must be installed on the system, It can be found [**here**][python.org]
- Please make sure that the text file is in proper format and is in `assests` or mention the path to that files as an argument
- The text file that must be passed a valid Sudoku Board `(9x9)` as a text file.

## Running Tests

```bash
python3 src/sudo.py path_to_file_here
```

## Screenshots
![Sudoku Terminal][pic]

[backtracking]: https://www.geeksforgeeks.org/introduction-to-backtracking-data-structure-and-algorithm-tutorials/
[pic]: imgs/terminaltest.png
[python.org]: https://www.python.org/downloads/