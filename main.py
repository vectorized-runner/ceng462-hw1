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


# x is ROW, y is COLUMN
def get_neighbors_in_graph(graph, coords):
    result = []
    top = (coords[0] - 1, coords[1])
    left = (coords[0], coords[1] - 1)
    bottom = (coords[0] + 1, coords[1])
    right = (coords[0], coords[1] + 1)
    if graph_contains(graph, left):
        result.append(left)
    if graph_contains(graph, top):
        result.append(top)
    if graph_contains(graph, bottom):
        result.append(bottom)
    if graph_contains(graph, right):
        result.append(right)

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
        print(stack)
        coords = stack.pop()
        print(coords)

        if coords not in visited:
            if is_customer(graph, coords):
                path.append(coords)
            elif is_finish(graph, coords):
                path.append(coords)
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
    start = find_start(graph)
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
                # Append the final to result
                return path
        # elif is_finish(graph, coords):
        # We don't finish the path, still packages left
        # continue
        # path.append(coords)
        # return path

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

    print("Size:")
    print(get_graph_size(example_graph))
    print("Start:")
    print(find_start(example_graph))
    print("Bfs:")
    print(bfs(example_package, example_graph))
    print("done")
