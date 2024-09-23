a = int(input())
pos = []
neg = []
neg_sum = 0
for i in range(a):
    b = int(input())
    if b > 0:
        pos += [b]
    elif b < 0:
        neg += [b]
        neg_sum += b
print(pos)
print(neg)
print(f'Count of positives: {len(pos)}')
print(f'Sum of negatives: {neg_sum}')
