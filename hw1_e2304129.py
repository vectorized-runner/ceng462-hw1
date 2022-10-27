def manhattan_dist(coord_a, coord_b):
    (ax, ay) = coord_a
    (bx, by) = coord_b
    xdiff = abs(ax - bx)
    ydiff = abs(ay - by)
    return xdiff + ydiff


def parse_file(file_name):
    f = open(file_name, "r")
    d = eval(f.read())
    return d['min'], d['env']


def find_start_customers_final(graph):
    (row_count, column_count) = get_graph_size(graph)
    current_row = 0
    start = (0, 0)
    final = (0, 0)
    customers = []

    while current_row != row_count:
        current_col = 0
        while current_col != column_count:
            coords = (current_row, current_col)
            if is_start(graph, coords):
                start = coords
            elif is_finish(graph, (current_row, current_col)):
                final = coords
            elif is_customer(graph, coords):
                customers.append(coords)
            current_col += 1
        current_row += 1

    return start, customers, final


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


def dfs(min_packages, graph):
    # We set this to -1 so that removing 'start' from the queue should make it 0, then we count customers
    current_package = -1
    stack = []
    path = []
    visited = set()
    (start, customers, final) = find_start_customers_final(graph)
    stack.append(start)

    while len(stack) > 0:
        coords = stack.pop()

        if coords not in visited:
            path.append(coords)
            current_package += 1
            if current_package == min_packages:
                path.append(final)
                return path
            visited.add(coords)

        for customer in customers:
            if customer not in visited:
                stack.append(customer)

    return None


def bfs(min_packages, graph):
    # We set this to -1 so that removing 'start' from the queue should make it 0, then we count customers
    package_count = -1
    queue = []
    path = []
    visited = set()
    (start, customers, final) = find_start_customers_final(graph)
    queue.append(start)
    visited.add(start)

    while len(queue) > 0:
        coords = queue.pop(0)
        path.append(coords)
        package_count += 1
        if package_count == min_packages:
            path.append(final)
            return path

        for customer in customers:
            if customer not in visited:
                visited.add(customer)
                queue.append(customer)

    return None


def get_min_cost(current_cost, customers, current_packages, min_packages, coords, final, path):
    current_packages += 1
    path.append(coords)

    if current_packages >= min_packages:
        path.append(final)
        cost = current_cost + manhattan_dist(coords, final)
        return cost, path

    min_cost = 1_000_000
    min_path = None
    for customer in customers:
        if customer not in path:
            cost = current_cost + manhattan_dist(coords, customer)
            search = get_min_cost(cost, customers, current_packages, min_packages, customer, final, path.copy())
            if search[0] < min_cost:
                min_cost = search[0]
                min_path = search[1]
    return min_cost, min_path


# Using Dijkstra doesn't help in this question, this is a brute-force finding all paths algorithm
def ucs(min_packages, graph):
    (start, customers, final) = find_start_customers_final(graph)

    if len(customers) < min_packages:
        return None

    return get_min_cost(0, customers, -1, min_packages, start, final, [])[1]


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

