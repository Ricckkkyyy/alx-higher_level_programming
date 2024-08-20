#!/usr/bin/python3
import sys


def print_solution(solution):
    """Print the board configuration."""
    print([[row, col] for row, col in enumerate(solution)])


def is_safe(solution, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if solution[i] == col or \
           solution[i] - i == col - row or \
           solution[i] + i == col + row:
            return False
    return True


def solve_nqueens(solution, row, n):
    """Solve the N Queens problem using backtracking."""
    if row == n:
        print_solution(solution)
        return

    for col in range(n):
        if is_safe(solution, row, col):
            solution[row] = col
            solve_nqueens(solution, row + 1, n)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solution = [-1] * n
    solve_nqueens(solution, 0, n)


if __name__ == "__main__":
    main()

