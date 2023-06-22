popu = int(input())
rank = [1 for i in range(popu)]
table = []
for i in range(popu):
  w, h = map(int, input().split())
  table.append([w,h])

for i in range(popu):
  for j in range(popu):
    if table[i][0] < table[j][0] and table[i][1] < table[j][1]:
      rank[i] += 1

rank_str = list(map(str, rank))
print(' '.join(rank_str))