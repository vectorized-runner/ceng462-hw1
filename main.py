def manhattan_dist(coord_a, coord_b):
    (ax, ay) = coord_a
    (bx, by) = coord_b
    xdiff = abs(ax - bx)
    ydiff = abs(ay - by)
    return xdiff + ydiff


def parse_file(file_name):
    min_packages = 0
    graph = [[]]
    return min_packages, graph


def find_start_and_final(graph):
    (row_count, column_count) = get_graph_size(graph)
    current_row = 0
    start = (0, 0)
    final = (0, 0)
    found = 0

    while current_row != row_count:
        current_col = 0
        while current_col != column_count:
            if is_start(graph, (current_row, current_col)):
                start = (current_row, current_col)
                found += 1
            elif is_finish(graph, (current_row, current_col)):
                final = (current_row, current_col)
                found += 1

            if found == 2:
                return start, final
            current_col += 1
        current_row += 1


def get_letter(graph, coords):
    (x, y) = coords
    return graph[x][y]


def is_customer(graph, coords):
    return get_letter(graph, coords) == 'C'


def is_start(graph, coords):
    return get_letter(graph, coords) == 'S'


def is_finish(graph, coords):
    return get_letter(graph, coords) == 'F'


def get_graph_size(graph):
    return len(graph), len(graph[0])


def graph_contains(graph, coords):
    (x, y) = coords
    (sizeX, sizeY) = get_graph_size(graph)
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= sizeX:
        return False
    if y >= sizeY:
        return False
    return True


# x is ROW, y is COLUMN
# going right -> increase y [Column], going up -> decrease x [Row]
def get_neighbors_in_graph(graph, coords):
    result = []
    (x, y) = coords
    top = (x - 1, y)
    bottom = (x + 1, y)
    left = (x, y - 1)
    right = (x, y + 1)

    # TODO: Ensure add order is correct
    if graph_contains(graph, right):
        result.append(right)
    if graph_contains(graph, left):
        result.append(left)
    if graph_contains(graph, top):
        result.append(top)
    if graph_contains(graph, bottom):
        result.append(bottom)

    return result


def dfs(min_packages, graph):
    current_package = 0
    stack = []
    path = []
    visited = set()
    (start, final) = find_start_and_final(graph)
    stack.append(start)
    path.append(start)

    while len(stack) > 0:
        print(stack)
        coords = stack.pop()
        print(coords)

        if coords not in visited:
            if is_customer(graph, coords):
                path.append(coords)
                # after enough customers are met append the final and return
                current_package += 1
                if current_package == min_packages:
                    path.append(final)
                    return path
            visited.add(coords)

        neighbors = get_neighbors_in_graph(graph, coords)
        for neighbor in neighbors:
            # Stack might contain duplicates
            if neighbor not in visited:
                stack.append(neighbor)

    # Path failed, DFS couldn't reach finish
    return None


def bfs(min_packages, graph):
    package_count = 0
    queue = []
    path = []
    visited = set()
    (start, final) = find_start_and_final(graph)
    queue.append(start)
    path.append(start)
    visited.add(start)

    while len(queue) > 0:
        print(queue)
        coords = queue.pop(0)
        print(coords)
        assert (coords in visited)

        if is_customer(graph, coords):
            path.append(coords)
            package_count += 1
            if package_count == min_packages:
                path.append(final)
                return path

        neighbors = get_neighbors_in_graph(graph, coords)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return None


def ucs(min_packages, graph):
    return 0


def UnInformedSearch(method_name, problem_file_name):
    parse_result = parse_file(problem_file_name)
    if method_name == 'DFS':
        return dfs(parse_result[0], parse_result[1])
    elif method_name == 'BFS':
        return bfs(parse_result[0], parse_result[1])
    elif method_name == 'UCS':
        return ucs(parse_result[0], parse_result[1])
    else:
        print("Unexpected method name: " + method_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    min_3 = 7
    example_graph_3 = ['....C...',
                       '.F......',
                       '.....C..',
                       '.......C',
                       '........',
                       'C.......',
                       '.C......',
                       'C...S.C.']

    min_2 = 8
    example_graph_2 = ['....C...',
                       '.F......',
                       '.....C..',
                       '.......C',
                       '........',
                       'C.......',
                       '.C......',
                       'C...S.C.']

    min_1 = 2
    example_graph_1 = ['....C...',
                       '.F......',
                       '.....C..',
                       '.......C',
                       '........',
                       'C.......',
                       '.C......',
                       'C...S.C.']

    print(dfs(example_graph_1, min_1))
    print("done")
