import time, os
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]
reset_color = "\033[0m"
def print_spiral(matrix):
    n, m = len(matrix), len(matrix[0])
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    visited = [[False] * m for op in range(n)]
    def display():
        os.system('cls' if os.name == 'nt' else 'clear')
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                color = colors[(x - 1) % len(colors)]
                if visited[i][j]:
                    print(color + f"{x:2}" + reset_color, end=" ")
                else:
                    print("  ", end=" ")
            print()
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            visited[top][i] = True
            display()
            time.sleep(0.5)
        top += 1
        for i in range(top, bottom + 1):
            visited[i][right] = True
            display()
            time.sleep(0.5)
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                visited[bottom][i] = True
                display()
                time.sleep(0.5)
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                visited[i][left] = True
                display()
                time.sleep(0.5)
            left += 1
print_spiral(matrix)