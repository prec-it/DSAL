def fractional_knapsack(val, wt, capacity):
	items = sorted(zip(val, wt), key=lambda x: x[0] / x[1], reverse=True)
	
	total = 0
	
	for value, weight in items:
		if capacity >= weight:
			total += value
			capacity -= weight
		else:
			total += (value / weight) * capacity
			break
			
	return total
	
	
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50

print (fractional_knapsack(val, wt, capacity))

