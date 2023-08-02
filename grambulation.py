import numpy as np

def num_spiral(n):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    spiral = np.zeros((n, n), int)
    positions = np.zeros((n * n, 2), int)
    x, y = n // 2, n // 2
    spiral[x, y] = 1
    positions[0] = (x, y)
    direction = 0

    for i in range(2, n * n + 1):
        dx, dy = directions[direction]
        nx, ny = directions[(direction + 1) % 4]
        # check if the cell in the next direction is unfilled.
        if spiral[x + nx, y + ny] == 0:
            direction = (direction + 1) % 4  # change direction
            dx, dy = directions[direction]
        x += dx
        y += dy
        spiral[x, y] = i
        positions[i - 1] = (x, y)

    return spiral, positions

def grambulate(a, b, n=1000):
    n = max(n, int(np.sqrt(max(a, b))) + 3)
    _, positions = num_spiral(n)
    x_a, y_a = positions[a-1]
    x_b, y_b = positions[b-1]
    dx, dy = x_b - x_a, y_b - y_a
    x_c, y_c = x_b + dx, y_b + dy
    if 0 <= x_c < n and 0 <= y_c < n:
        result_positions = np.where((positions == (x_c, y_c)).all(axis=1))
        if result_positions[0].size != 0:
            return result_positions[0][0] + 1
    return None

def u_input():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    return a, b

def main():
    a, b = u_input()
    result = grambulate(a, b)
    if result is not None:
        print(f"Would you look at that, {a}♢{b} is {result}.")
    else:
        print(f"{a}♢{b} falls outside the spiral grid.")

if __name__ == "__main__":
    main()
