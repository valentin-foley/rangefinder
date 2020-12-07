def rangefinder(input):
	
	sorted_input = sorted(input)
	maxrange = [sorted_input[0], sorted_input[0]]
	range = [sorted_input[0], sorted_input[0]]
	previous = sorted_input[0]
	
	for current in sorted_input[1:]:
		if (current == previous + 1) or (current == previous):
			range[1] = current
		else:
			if (range[1] - range[0]) > (maxrange[1] - maxrange[0]):
				maxrange = range
			range = [current, current]
		previous = current
	
	if (range[1] - range[0]) > (maxrange[1] - maxrange[0]):
		maxrange = range
	
	return maxrange