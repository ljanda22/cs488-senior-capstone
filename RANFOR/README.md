Psuedo: Random Forest

Input: Training set Dn, number of trees M > 0, an ∈ {1, . . . , n},
mtry ∈ {1, . . . , p}, nodesize ∈ {1, . . . , an}, and x ∈ X .
Output: Prediction of the random forest at x.
1 for j = 1, . . . , M do
2 Select an points, with (or without) replacement, uniformly in Dn. In the
following steps, only these an observations are used.
3 Set P = (X ) the list containing the cell associated with the root of the
tree.
4 Set Pfinal = ∅ an empty list.
5 while P 6= ∅ do
6 Let A be the first element of P.
7 if A contains less than nodesize points or if all Xi ∈ A are equal
then
8 Remove the cell A from the list P.
9 Pfinal ← Concatenate(Pfinal, A).
10 else
11 Select uniformly, without replacement, a subset Mtry ⊂ {1, . . . ,
p} of cardinality mtry.
12 Select the best split in A by optimizing the CART-split criterion
along the coordinates in Mtry (see text for details).
13 Cut the cell A according to the best split. Call AL and AR the
two resulting cells.
14 Remove the cell A from the list P.
15 P ← Concatenate(P, AL, AR).
16 end
17 end
18 Compute the predicted value mn(x; Θj
, Dn) at x equal to the average of
the Yi
falling in the cell of x in partition Pfinal.
19 end
20 Compute the random forest estimate mM,n(x; Θ1, . . . , ΘM, Dn) at the query
point x according to (1).
