def bitonic3(List):
	if (List[1] < List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[0] > List[2]):
		List[0], List[2] = List[2], List[0]
	if (List[1] > List[2]):
		List[1], List[2] = List[2], List[1]
	return List
