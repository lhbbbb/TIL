# Segment Tree

구간의 빈번한 연산(최소, 최대, 합 등)이 있을 때 사용한다.

시간복잡도 $O(logN)$

segment tree 문제를 풀 때 가장 중요한 점은 $tree[i]$를 어떻게 정의할 것인지이다.

문제 유형에는 segment tree + vector, segment tree + tree 등이 있다.

## Lazy Propagation

구간의 각 요소들을 같은 값으로 한번에 업데이트 할 때 $O(NlogN)$의 연산이 발생하게 된다.

lazy propagation을 사용하면 이를 $O(logN)$만에 처리할 수 있다.

```java
package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class practice {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		StringTokenizer st = new StringTokenizer(s);
		int n, m;
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		s = br.readLine();
		st = new StringTokenizer(s);
		for(int i=0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		System.out.println(Arrays.toString(arr));
		Segment tree = new Segment(arr, arr.length);
		System.out.println(Arrays.toString(tree.tree));
//		tree.update(0, arr.length-1, 2, 1, 2);
//		System.out.println(Arrays.toString(tree.tree));
		System.out.println(tree.query(0, arr.length-1, 0, 2, 1));
		tree.update_range(0, arr.length-1, 0, 2, 1, 2);
		System.out.println(Arrays.toString(tree.tree));
	}
}

class Segment {
	int[] tree;
	int[] lazy;
	
	Segment(int[] arr, int n) {
		tree = new int[n*4];
		lazy = new int[n*4];
		
		init(arr, 0, n-1, 1);
	}
	
	int init(int[] arr, int s, int e, int node) {
		if (s == e) {
			return tree[node] = arr[s];
		}
		int mid = (s+e) / 2;
		return tree[node] = init(arr, s, mid, node*2) + init(arr, mid+1, e, node*2+1);
	}
	
	public void update(int s, int e, int idx, int node, int diff) {
		if (idx < s || idx > e) {
			return ;
		}
		tree[node] += diff;
		if (s != e) {
			int mid = (s+e) / 2;
			update(s, mid, idx, node*2, diff);
			update(mid+1, e, idx, node*2+1, diff);
		}
	}
	public int query(int s, int e, int left, int right, int node) {
		if (s > right || e < left) {
			return 0;
		}
		
		if (left <= s && e <= right) {
			return tree[node];
		}
		int mid = (s+e) / 2;
		return query(s, mid, left, right, node*2) + query(mid+1, e, left, right, node*2+1);
	}
	void update_lazy(int s, int e, int node) {
		if (lazy[node] != 0) {
			tree[node] += (e-s+1) * lazy[node];
			if (s != e) {
				lazy[node*2] += lazy[node];
				lazy[node*2+1] += lazy[node];
			}
			lazy[node] = 0;
		}
	}
	public void update_range(int s, int e, int left, int right, int node, int diff) {
		update_lazy(s, e, node);
		if (s > right || e < left) {
			return ;
		}
		
		if (left <= s && e <= right) {
			tree[node] += (e-s+1) * diff;
			if (s != e) {
				lazy[node*2] += diff;
				lazy[node*2+1] += diff;
			}
			return ;
		}
		
		int mid = (s+e) / 2;
		update_range(s, mid, left, right, node*2, diff);
		update_range(mid+1, e, left, right, node*2+1, diff);
		tree[node] = tree[node*2] + tree[node*2+1];
	}
}
```