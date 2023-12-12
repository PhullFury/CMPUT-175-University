def bubble4(List):
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	if (List[1] > List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[2] > List[3]):
		List[2], List[3] = List[3], List[2]
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	if (List[1] > List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	return List
