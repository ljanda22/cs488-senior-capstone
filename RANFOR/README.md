## Psuedo: Random Forest

1. Input: Training set Dn, number of trees M > 0, an ∈ {1, . . . , n},
2.         mtry ∈ {1, . . . , p}, nodesize ∈ {1, . . . , an}, and x ∈ X.
3. Output: Prediction of the random forest at x.
4. 
5. **for** j = 1, . . . , M **do**
6.     Select an points, with (or without) replacement, uniformly in Dn. In the
7.     following steps, only these an observations are used.
8.     Set P = (X ) the list containing the cell associated with the root of the
9.     tree.
10.     Set Pfinal = ∅ an empty list.
11.     **while** P 6= ∅ **do**
12.         Let A be the first element of P.
13.         **if** A contains less than nodesize points or if all **X**i ∈ A are equal
14.         **then**
15.              Remove the cell A from the list P.
16.              Pfinal ← Concatenate(Pfinal, A).
17.         **else**
18.              Select uniformly, without replacement, a subset Mtry ⊂ {1, . . . ,
19.              p} of cardinality **mtry**.
20.              Select the best split in A by optimizing the CART-split criterion
21.              along the coordinates in Mtry (see text for details).
22.              Cut the cell A according to the best split. Call AL and AR the
23.              two resulting cells.
24.              Remove the cell A from the list P.
25.              P ← Concatenate(P, AL, AR).
26.         **end**
27.     **end**
28.     Compute the predicted value mn(x; Θj, Dn) at x equal to the average of
29.     the **Y**i falling in the cell of **x** in partition **P**final.
30. end
31. Compute the random forest estimate mM,n(x; Θ1, . . . , ΘM, Dn) at the query
32. point x according to ([1](https://arxiv.org/pdf/1511.05741.pdf)).
