Psuedocode: SMOTE

Algorithm SMOTE(T, N, k)
Input: Number of minority class samples T; Amount of SMOTE N%; Number of nearest
neighbors k
Output: (N/100) * T synthetic minority class samples
1. (∗ If N is less than 100%, randomize the minority class samples as only a random
percent of them will be SMOTEd. ∗)
2. if N < 100
3. then Randomize the T minority class samples
4. T = (N/100) ∗ T
5. N = 100
6. endif
7. N = (int)(N/100) (∗ The amount of SMOTE is assumed to be in integral multiples of
100. ∗)
8. k = Number of nearest neighbors
9. numattrs = Number of attributes
10. Sample[ ][ ]: array for original minority class samples
11. newindex: keeps a count of number of synthetic samples generated, initialized to 0
12. Synthetic[ ][ ]: array for synthetic samples
(∗ Compute k nearest neighbors for each minority class sample only. ∗)
13. for i ← 1 to T
14. Compute k nearest neighbors for i, and save the indices in the nnarray
15. Populate(N, i, nnarray)
16. endfor
Populate(N, i, nnarray) (∗ Function to generate the synthetic samples. ∗)
17. while N 6= 0
18. Choose a random number between 1 and k, call it nn. This step chooses one of
the k nearest neighbors of i.
19. for attr ← 1 to numattrs
20. Compute: dif = Sample[nnarray[nn]][attr] − Sample[i][attr]
21. Compute: gap = random number between 0 and 1
22. Synthetic[newindex][attr] = Sample[i][attr] + gap ∗ dif
23. endfor
24. newindex++
25. N = N − 1
26. endwhile
27. return (∗ End of Populate. ∗)
End of Pseudo-Code.

