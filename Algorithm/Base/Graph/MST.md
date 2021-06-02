# Minimum Spanning Tree(MST)

## Spanning Tree

* 최소 간선(n-1개)으로 그래프 내의 모든 정점을 연결하는 트리
* 하나의 그래프에서 스패닝 트리는 여러개가 존재할 수 있다

![spanning tree](assets/spanning_trees.jpg)

* 최소 신장 트리



## 프림

### 과정

1. 임의 정점을 하나 선택 시작
2. 선택한 정점과 인접하는 정점들 중 최소 비용의 간선이 존재하는 정점 선택
3. 모든 정점 선택될 때까지 2 반복

```python
def Prim(G, s) # G: 그래프, s: 시작 정점
	# Settings
    edges = [float('inf')] * N # 간선에 해당하는 가중치 값들
    p = [None] * N # 자신과 연결된 부모 노드
    visited = [0] * N # 방문 여부
    edges[s] = 0 # 시작 노드 가중치 0으로 초기화    
    
    # solve 
    for _ in range(N):
        min_val = float('inf')
        min_idx = -1
        # 방문 안한 정점 중 최소 가중치 정점 찾기
        ## dijkstra 알고리즘과 마찬가지로 최소 힙이나, priority queue 구조를 사용하면 불필요한 연산을 줄일 수 있어 빨라진다.
        for i in range(N):
            if not visited[i] and edges[i] < min_val:
                min_idx = i
                min_val = edges[i]
       	visited[min_idx] = 1 # 방문 처리
        # 간선 정보 업데이트, 업데이트 된 간선 정보를 가지는 노드가 다음 후보군이 된다.
        for node, val in G[min_idx]:
            if not visited[node] and val < edges[node]:
                edges[node] = val
                p[node] = min_idx

```

```java
package test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


class Edges implements Comparable<Edges>{
	int v, w;
	
	Edges(int node, int weight) {
		v = node;
		w = weight;
	}
	
	public String toString() {
		return v + " " + w;
	}
	
	@Override
	public int compareTo(Edges e) {
		if (w < e.w) {
			return -1;
		} else {
			return 1;
		}
	}
}

public class Solution {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new FileReader("input.txt"));
		String s = br.readLine();
		
		StringTokenizer st = new StringTokenizer(s);
		
		int T = Integer.parseInt(st.nextToken());
		
		for (int tc=1; tc < T+1; tc++) {
			s = br.readLine();
			st = new StringTokenizer(s);
			
			int N, M;
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			int start, end, cost;
			
			ArrayList<Edges>[] graph = new ArrayList[N+1];
			int[] edges = new int[N+1];
			int[] visited = new int[N+1];
			
			Arrays.fill(edges, Integer.MAX_VALUE);
			edges[1] = 0;
			// init settings
			for (int i=0; i<N+1; i++) {
				graph[i] = new ArrayList<>();
			}
			
			for (int i=0; i < M; i++) {
				s = br.readLine();
				st = new StringTokenizer(s);
				start = Integer.parseInt(st.nextToken());
				end = Integer.parseInt(st.nextToken());
				cost = Integer.parseInt(st.nextToken());
				
				graph[start].add(new Edges(end, cost));
				graph[end].add(new Edges(start, cost));
			}
			
			PriorityQueue<Edges> q = new PriorityQueue<>();
			q.offer(new Edges(1, 0));
			// solve
			Edges vertex;
			while (!q.isEmpty()) {
				vertex = q.poll();
				int min_idx = vertex.v;
				if (visited[min_idx] != 0) {
					continue;
				}
				visited[min_idx] = 1;
				// 간선 가중치 업데이트
				for (Edges nxt: graph[min_idx]) {
					int node = nxt.v;
					int w = nxt.w;
					if (visited[node] == 0 && edges[node] > w) {
						edges[node] = w;
						q.offer(new Edges(node, w));
					}
				}
			}
			System.out.println(Arrays.toString(edges));
		}
	}
}
```



## 크루스칼

### 관련문제

* [다리만들기2](/Algorithm/Baekjoon/다리만들기2/17472.py), [최소신장트리](/Algorithm/Samsung/2기서울1반10월17일이현빈/5249_최소신장트리.py)

### 과정

1. 간선 정렬
2. 정렬된 간선을 돌면서 각 간선에 속한 노드들이 사이클을 형성하는지 확인(Disjoint Set 알고리즘 사용)
   1. 각 간선에 속한 노드들의 부모노드가 같은지 확인(FindSet)
   2. 같으면 사이클 형성된것이므로 pass
   3. 같지 않으면 UnionSet을 사용해서 부모 노드를 가리키게 함

```python
def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])


def unionset(x, y):
    p[findset(y)] = findset(x)


for tc in range(1, T + 1):
    V, E = map(int, input().split())

    info = []
    for _ in range(E):
        info.append(list(map(int, input().split())))

    # sort edges by cost
    info.sort(key=lambda x: x[2])

    # find mst cost
    p = [x for x in range(V + 1)]
    cost = 0
    for ele in info:
        if findset(ele[0]) != findset(ele[1]):
            unionset(ele[0], ele[1])
            # print(p)
            cost += ele[2]

    print("#{} {}".format(tc, cost))
```

### 단점

* 시간복잡도가 간선을 정렬하는 시간에 영향을 받기 때문에 간선 수가 많으면 비효율적