# Computational Thinking

## 2019.10.07

* 항진명제: 항상 참
* 모순명제: 항상 거짓



## 시간복잡도 계산

$$
\begin{align*}
2^x &= n \\
\Rightarrow x &= log_2n \\
T(n) &= 2T(\frac{n}{2}) + n\\
&= n + 2(\frac{n}{2} + 2T(\frac{n}{4})) \\
&= n + 2(\frac{n}{2} + 2(\frac{n}{4} + 2T(\frac{n}{8})))\\
&= xn + 2^xT(\frac{n}{2^x}) \\
&= nlog_2n + nT(1)\\
&= O(nlog_2n)
\end{align*}
$$



