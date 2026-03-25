rider_scores=[0,10,90,20]

for i in range(len(rider_scores)):
    if rider_scores[i] <= 50:
        rider_scores[i] += 20
print(rider_scores)