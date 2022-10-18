def manhattan_dist(coord_a, coord_b):
    xdiff = abs(coord_a[0] - coord_b[0])
    ydiff = abs(coord_a[1] - coord_b[1])
    return xdiff + ydiff


def parse_file(file_name):
    min_packages = 0
    graph = [[]]
    return min_packages, graph


def find_start(graph):
    graph_size = get_graph_size(graph)
    row_count = graph_size[0]
    column_count = graph_size[1]
    current_row = 0

    while current_row != row_count:
        current_col = 0
        while current_col != column_count:
            if is_start(graph, (current_row, current_col)):
                return current_row, current_col
            current_col += 1
        current_row += 1


def get_letter(graph, coords):
    return graph[coords[0]][coords[1]]


def is_customer(graph, coords):
    return get_letter(graph, coords) == 'C'


def is_start(graph, coords):
    return get_letter(graph, coords) == 'S'


def is_finish(graph, coords):
    return get_letter(graph, coords) == 'F'


def get_graph_size(graph):
    return len(graph), len(graph[0])


def graph_contains(graph, coords):
    graph_size = get_graph_size(graph)
    if coords[0] < 0:
        return False
    if coords[1] < 0:
        return False
    if coords[0] >= graph_size[0]:
        return False
    if coords[1] >= graph_size[1]:
        return False
    return True


def get_neighbors(coords):
    result = []
    top_left = (coords[0] - 1, coords[1] - 1)
    top = (coords[0], coords[1] - 1)
    top_right = (coords[0] + 1, coords[1] - 1)
    left = (coords[0] - 1, coords[1])
    right = (coords[0] + 1, coords[1])
    bottom_left = (coords[0] - 1, coords[1] + 1)
    bottom_right = (coords[0] + 1, coords[1] + 1)
    bottom = (coords[0], coords[1] + 1)
    result.append(top_left)
    result.append(top)
    result.append(top_right)
    result.append(left)
    result.append(right)
    result.append(bottom_left)
    result.append(bottom_right)
    result.append(bottom)
    return result


def get_neighbors_in_graph(graph, coords):
    result = []
    neighbors = get_neighbors(coords)
    for neighbor in neighbors:
        if graph_contains(graph, neighbor):
            result.append(neighbor)

    return result


def dfs(min_packages, graph):
    current_package = 0
    stack = []
    path = []
    visited = set()
    start = find_start(graph)
    stack.append(start)
    path.append(start)

    while len(stack) > 0:
        coords = stack.pop()
        assert graph_contains(graph, coords)

        if is_customer(graph, coords):
            path.append(coords)
        elif is_finish(graph, coords):
            path.append(coords)
            return path
            break

        visited.add(coords)
        neighbors = get_neighbors_in_graph(graph, coords)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    # Path failed, DFS couldn't reach finish
    return None


def bfs(min_packages, graph):
    return 0


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
    example_package = 3

    example_graph = [
        "C...C...",
        "........ ",
        "........",
        ".....C.C",
        "........",
        "C.......",
        "......F.",
        "C...S.C."]

    print(dfs(example_package, example_graph))
    print("done")
