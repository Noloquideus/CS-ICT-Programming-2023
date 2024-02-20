from typing import List, Tuple, Optional, Set
import random
import pathlib

T = List[List[str]]


def read_sudoku(path: str) -> T:
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> T:
    digits = [c for c in puzzle if c in "123456789."]
    return group(digits, 9)


def display(grid: T) -> None:
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print("".join(grid[row][col].center(width) + ("|" if col % 3 == 2 and col < 8 else "") for col in range(9)))
        if row % 3 == 2 and row < 8:
            print(line)
    print()


def group(values: List[T], n: int) -> List[List[T]]:
    return [values[i:i + n] for i in range(0, len(values), n)]


def get_row(grid: T, pos: Tuple[int, int]) -> List[str]:
    return grid[pos[0]]


def get_col(grid: T, pos: Tuple[int, int]) -> List[str]:
    return [grid[row][pos[1]] for row in range(9)]


def get_block(grid: T, pos: Tuple[int, int]) -> List[str]:
    start_row, start_col = pos[0] // 3 * 3, pos[1] // 3 * 3
    return [
        grid[row][col]
        for row in range(start_row, start_row + 3)
        for col in range(start_col, start_col + 3)
    ]


def find_empty_positions(grid: T) -> Optional[Tuple[int, int]]:
    for row in range(9):
        for col in range(9):
            if grid[row][col] == '.':
                return row, col
    return None


def find_possible_values(grid: T, pos: Tuple[int, int]) -> Set[str]:
    row_values = set(get_row(grid, pos))
    col_values = set(get_col(grid, pos))
    block_values = set(get_block(grid, pos))
    return set(str(i) for i in range(1, 10)) - row_values - col_values - block_values


def solve(grid: T) -> Optional[T]:
    empty_position = find_empty_positions(grid)
    if not empty_position:
        return grid

    row, col = empty_position
    possible_values = find_possible_values(grid, (row, col))

    for value in possible_values:
        grid[row][col] = value
        if solve(grid):
            return grid
        grid[row][col] = '.'

    return None


def check_solution(solution: T) -> bool:
    for row in solution:
        if len(set(row)) != 9 or '.' in row:
            return False

    for col in range(9):
        if len(set(get_col(solution, (0, col)))) != 9:
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if len(set(get_block(solution, (row, col)))) != 9:
                return False

    return True


def generate_sudoku(N: int) -> T:
    grid = [['.' for _ in range(9)] for _ in range(9)]
    solution = solve(grid)
    if solution is None:
        return grid

    indices = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(indices)

    for i, j in indices[:N]:
        grid[i][j] = '.'

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
