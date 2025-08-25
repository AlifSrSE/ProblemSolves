# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def is_valid_placement(grid, n, m):
    black_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                black_cells.append((i, j))
    
    if not black_cells:
        return 0
    
    rows_with_black = set()
    cols_with_black = set()
    
    for i, j in black_cells:
        rows_with_black.add(i)
        cols_with_black.add(j)
    
    if len(rows_with_black) < n or len(cols_with_black) < m:
        return -1
    
    def can_reach_all_black(start_i, start_j, visited):
        stack = [(start_i, start_j)]
        visited.add((start_i, start_j))
        reached = set([(start_i, start_j)])
        
        while stack:
            i, j = stack.pop()
            for jj in range(m):
                if grid[i][jj] == '#' and (i, jj) not in visited:
                    visited.add((i, jj))
                    reached.add((i, jj))
                    stack.append((i, jj))
            for ii in range(n):
                if grid[ii][j] == '#' and (ii, j) not in visited:
                    visited.add((ii, j))
                    reached.add((ii, j))
                    stack.append((ii, j))
        return reached
    
    visited = set()
    components = []
    
    for i, j in black_cells:
        if (i, j) not in visited:
            reached = can_reach_all_black(i, j, visited)
            for ii in range(n):
                for jj in range(m):
                    if grid[ii][jj] == '.' and (ii, jj) in reached:
                        return -1
            components.append(reached)
    
    def can_place_south_magnets():
        for component in components:
            component_rows = set(i for i, j in component)
            component_cols = set(j for i, j in component)
            if len(component_rows) == n and len(component_cols) == m:
                continue
            else:
                remaining_rows = set(range(n)) - component_rows
                remaining_cols = set(range(m)) - component_cols
                other_black_cells = [(i, j) for i, j in black_cells if (i, j) not in component]
                other_rows = set(i for i, j in other_black_cells)
                other_cols = set(j for i, j in other_black_cells)
                if not (remaining_rows.issubset(other_rows) and remaining_cols.issubset(other_cols)):
                    return False
        return True
    
    if not can_place_south_magnets():
        return -1
    
    return len(components)

def alif():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    return is_valid_placement(grid, n, m)

print(alif())