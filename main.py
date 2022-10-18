
def manhattan_dist(coord_a, coord_b):
    xdiff = abs(coord_a[0] - coord_b[0])
    ydiff = abs(coord_a[1] - coord_b[1])
    return xdiff + ydiff


def parse_file(file_name):
    min_packages = 0
    graph = [[]]
    return min_packages, graph


def dfs(min_packages, graph):
    return 0

def bfs(min_packages, graph):
    return 0

def ucs(min_packages, graph):
    return 0

def AAA():
    return 0

def UnInformedSearch(method_name , problem_file_name):
    parse_result = parse_file(problem_file_name)
    if method_name == 'DFS':
        return dfs(parse_result[0], parse_result[1])
    elif method_name == 'BFS':
        return bfs(parse_result[0], parse_result[1])
    else
        return ucs(parse_result[0], parse_result[1])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(manhattan_dist((-1, -1), (3, 5)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
