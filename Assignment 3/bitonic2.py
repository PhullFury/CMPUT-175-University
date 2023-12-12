def bitonic2(List):
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	return List
