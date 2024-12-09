from collections import defaultdict, deque

def resolve_dependencies_order(dependencies):
    # Build the graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for item, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(item)
            in_degree[item] += 1
        if item not in in_degree:
            in_degree[item] = 0

    # Ensure all nodes are in the in_degree, even if they have no dependencies
    for node in graph:
        if node not in in_degree:
            in_degree[node] = 0

    # Collect nodes with no dependencies
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == len(in_degree):
        return order  # Valid build order
    else:
        raise ValueError("Cyclic dependency detected!")
