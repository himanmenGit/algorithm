# graph = {
#     'start': {
#         'a': 6,
#         'b': 2,
#     },
#     'a': {
#         'fin': 1
#     },
#     'b': {
#         'a': 3,
#         'fin': 5,
#     },
#     'fin': {
#
#     }
# }

# graph = {
#     'S': {
#         'A': 1,
#         'C': 2,
#     },
#     'A': {
#         'B': 6
#     },
#     'B': {
#         'E': 2,
#         'D': 1,
#     },
#     'C': {
#         'A': 4,
#         'D': 3
#     },
#     'D': {
#         'E': 1,
#     },
#     'E': {
#
#     }
# }

# graph = {
#     'A': {
#         'B': 10
#     },
#     'B': {
#         'C': 20
#     },
#     'C': {
#         'D': 20,
#         'E': -1,
#     },
#     'D': {
#         'C': 10
#     },
#     'E': {
#         'B': -20,
#     },
# }

graph = {
    'S': {
        'A': 2,
        'B': 2,
    },
    'A': {
        'B': 2,
    },
    'B': {
        'C': 2,
        'FIN': 2,
    },
    'C': {
        'A': -1,
        'FIN': 2,
    },
    'FIN': {
    }
}

# graph = {
#     'S': {
#         'B': 2
#     },
#     'B': {
#         'A': 1,
#         'FIN': 3
#     },
#     'A': {
#         'B': 1
#     },
#     'FIN': {
#
#     },
# }

costs = {
    # 'a': 6,
    # 'b': 2,
    # 'fin': float('inf'),
}

parents = {
    # 'a': 'start',
    # 'b': 'start',
    # 'fin': None
}

processed = list()

start_node = 'S'
end_node = 'FIN'


def set_node(node):
    costs[node] = 0
    parents[node] = None
    for node_name, node_value in graph[node].items():
        costs[node_name] = node_value
        parents[node_name] = node

    for node_name, nodes in graph.items():
        # 그래프의 노드중 코스트에 없는 노드는 무한대
        if node_name not in costs.keys():
            costs[node_name] = float('inf')
        if node_name not in parents.keys():
            parents[node_name] = None

    for key, value in costs.items():
        print(f'costs : {key} _ {value}')

    for key, value in parents.items():
        print(f'parent : {key} _ {value}')


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:  # 모든 정점을 확인
        cost = costs[node]  # 아직 처리하지 않는 정점 중 더 싼것이 있으면
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


set_node(start_node)
node = find_lowest_cost_node(costs)  # 아직처리하지 않은 가장 싼 정점을 찾는다.
while node is not None:  # 모든 정점을 처리하면 반복문이 종료 된다.
    cost = costs[node]  # 가격을 구한다.
    neighbors = graph[node]  # 이웃을 가져온다.
    for n in neighbors.keys():  # 모든 이웃에 대해 반복
        new_cost = cost + neighbors[n]  # 현재 정점 의 가격 + 이웃중 한명의 가격을 더함.
        print(f'{node}의 cost{cost} + neighbors[이웃]{neighbors[n]} = new_cost{new_cost}')
        if costs[n] > new_cost:  # 만약 이 정점을 지나는 것이 가격이 더 싸다면
            costs[n] = new_cost  # 정점의 가격을 갱신
            parents[n] = node  # 부모를 이 정점으로 새로 설정
    processed.append(node)  # 정점을 처리한 사실을 기록
    node = find_lowest_cost_node(costs)  # 다음으로 처리할 정점을 찾아 반복

result = list()


def find_path(key):
    if parents[key] == start_node:
        result.append(start_node)
        return
    else:
        find_path(parents[key])
        result.append(parents[key])


find_path(end_node)
print('최단 시간 경로: ', ' -> '.join(result), '->', end_node)
print('총 가격:', costs[end_node])
print(costs)
print(processed)