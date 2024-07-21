N = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)
normalized_scores = []

for score in scores:
    normalized_scores.append((score / max_score) * 100)
average_normalized_score = sum(normalized_scores) / N
print(average_normalized_score)