Pseudo: HNNU

1: n1 ←− number of samples of the minority class
2: n2 ←− number of samples of the majority class
3: m ←− number of attributes
4: majSamples[1 . . . n2] ←− Samples of the Majority class
5: minSamples[1 . . . n1] ←− Samples of the Minority class
6: if m > threshold then
7: model ←− autoencoder.train(minSamples[1 . . . n1])
8: else
9: model ←− simpleANN.train(minSamples[1 . . . n1])
10: end if
11: distArray ←− {}
12: for each x ∈ n2 do
13: x
0 ←− model.predict(x)
14: d ←− ||x − x
0
||2
2
15: index ←− x.index
16: distArray ←− distArray ∪ {d, index}
17: end for
18: sortedList ←− sort(majSamples[1 . . . n2], distArray)
. Sort the indices of n2 samples according to descending
order of distance
19: selectedIndices ←− sortedList[1..n1] . select first n1
number of indices from the sortedList
20: X1 = {}
21: for each index ∈ selectedIndices do
22: X1 = X1 ∪ majSamples[index]
23: end for
24: f inalData = X1 ∪ minSamples[1 . . . n1])
