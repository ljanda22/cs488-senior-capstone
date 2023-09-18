## Psuedo: Random Forest

Input: Training set Dn, number of trees M > 0, an ∈ {1, . . . , n},
         mtry ∈ {1, . . . , p}, nodesize ∈ {1, . . . , an}, and x ∈ X.
Output: Prediction of the random forest at x.
 
- **for** j = 1, . . . , M **do**
-      Select an points, with (or without) replacement, uniformly in Dn. In the following steps, only these an observations are used.
-      Set P = (X ) the list containing the cell associated with the root of the tree.
-      Set Pfinal = ∅ an empty list.
-      **while** P 6= ∅ **do**
-          Let A be the first element of P.
-          **if** A contains less than nodesize points or if all **X**i ∈ A are equal
-          **then**
-               Remove the cell A from the list P.
-               Pfinal ← Concatenate(Pfinal, A).
-          **else**
-               Select uniformly, without replacement, a subset Mtry ⊂ {1, . . . ,
-               p} of cardinality **mtry**.
-               Select the best split in A by optimizing the CART-split criterion
-               along the coordinates in Mtry (see text for details).
-               Cut the cell A according to the best split. Call AL and AR the
-               two resulting cells.
-               Remove the cell A from the list P.
-               P ← Concatenate(P, AL, AR).
-          **end**
-      **end**
-      Compute the predicted value mn(x; Θj, Dn) at x equal to the average of
-      the **Y**i falling in the cell of **x** in partition **P**final.
-  **end**
-  Compute the random forest estimate mM,n(x; Θ1, . . . , ΘM, Dn) at the query
-  point x according to ([1](https://arxiv.org/pdf/1511.05741.pdf)).

