package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		StringTokenizer st = new StringTokenizer(s);
		int N = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[N];
		s = br.readLine();
		st = new StringTokenizer(s);
		for(int i=0; i < N ; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int MAX = 1000000;
		Seg tree = new Seg(MAX);
		
		int ans = 0;
		
		for(int i=0; i < N; i++) {
			int cur = tree.query(1, MAX, 1, arr[i]-1, 1);
			if (ans < cur + 1) {
				ans = cur + 1;
			}
			tree.update(1,  MAX,  arr[i], 1, cur+1);
		}
		
		System.out.println(ans);
		
		return ;
	}
}

class Seg {
	int[] tree;
	int[] lazy;
	
	Seg(int n) {
		tree = new int[n*4];
		lazy = new int[n*4];
	}
	int max(int a, int b) {
		if (a < b) {
			return b;
		} else {
			return a;
		}
	}
	void update(int s, int e, int idx, int node, int val) {
		if (idx < s || idx > e) {
			return ;
		}
		tree[node] = max(tree[node], val);
		if (s != e) {
			int mid = (s + e) / 2;
			update(s, mid, idx, node*2, val);
			update(mid+1, e, idx, node*2+1, val);
		}
		
	}
	
	public int query(int s, int e, int left, int right, int node) {
		if (s > right || e < left) {
			return 0;
		}
		if (left <= s && e <= right) {
			return tree[node];
		}
		int mid = (s + e) / 2;  
		return max(query(s, mid, left, right, node*2), query(mid+1, e, left, right, node*2+1));
	}
}
