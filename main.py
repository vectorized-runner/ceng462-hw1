def manhattan_dist(coord_a, coord_b):
    xdiff = abs(coord_a[0] - coord_b[0])
    ydiff = abs(coord_a[1] - coord_b[1])
    return xdiff + ydiff


def parse_file(file_name):
    min_packages = 0
    graph = [[]]
    return min_packages, graph


def find_start(graph):
    row_count = len(graph)
    column_count = len(graph[0])
    current_row = 0

    while current_row != row_count:
        current_col = 0
        while current_col != column_count:
            print(graph[current_row][current_col])
            if graph[current_row][current_col] == 'S':
                return current_row, current_col
            current_col += 1
        current_row += 1


def dfs(min_packages, graph):
    current_package = 0
    stack = []
    visited = {}
    start = find_start(graph)
    

    return 0


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
    queue = []
    queue.append((1, 1))
    queue.append((2, 2))
    print(queue.pop())
    print(queue.pop())

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

    start = find_start(example_graph)

    print(start)
