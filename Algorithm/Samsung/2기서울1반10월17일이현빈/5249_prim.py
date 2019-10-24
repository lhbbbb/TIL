import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

# todo: 너무 비효율적이게 작성함. 효율적으로 작성해보기
def prim(node):
    cost = 0
    stack = [node]
    visited[node] = True
    rear = -1
    while rear < V - 1:
        rear += 1
        node = stack[rear]
        min_node = 0
        min_val = 1e8
        for ele in stack:
            for next_node, node_cost in enumerate(adj_matrix[ele]):
                if node_cost and not visited[next_node]:
                    if min_val > node_cost:
                        min_val = node_cost
                        min_node = next_node

        visited[min_node] = True
        cost += min_val
        stack.append(min_node)

    return cost


for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_matrix[n1][n2] = w
        adj_matrix[n2][n1] = w

    visited = [0] * (V + 1)

    print('#{} {}'.format(tc, prim(0)))
