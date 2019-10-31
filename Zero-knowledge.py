from collections import Counter
import pandas as pd

cipher = input().upper()
counter = Counter(cipher)
len_all = len(cipher)

frequency = {}
sum = 0
english_freq = {'E': 12.02, 'T': 9.10, 'A': 8.12,'O': 7.68, 'I':7.31, 'N': 6.95, 'S': 6.28, 'R':6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61,'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P':1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X' : 0.17, 'Q': 0.11, 'J': 0.10, 'Z':0.07 }
english_freq_sorted = {k: english_freq[k] for k in sorted(english_freq)}
for i in counter.keys():
    frequency[i] = (counter[i]/len_all)*100

diff_m = [[0 for j in range(26)] for i in range(len(frequency.keys()))]
index_cipher = 0
index_en = 0
for i in frequency.keys():
    for j in english_freq_sorted.keys():
        diff_m[index_cipher][index_en] = abs(frequency[i] - english_freq_sorted [j])
        index_en += 1
    index_cipher += 1
    index_en = 0

matrix_data =pd.DataFrame(diff_m, columns=english_freq_sorted.keys(), index=counter.keys())

m1 =matrix_data.sort_values(axis=1, ascending=False, by = list(matrix_data.index))
nearest_chars = m1[m1.columns[-5:]]
print(nearest_chars)



