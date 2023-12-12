def bitonic7(List):
	if (List[1] < List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[0] > List[2]):
		List[0], List[2] = List[2], List[0]
	if (List[1] > List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[3] < List[4]):
		List[3], List[4] = List[4], List[3]
	if (List[5] > List[6]):
		List[5], List[6] = List[6], List[5]
	if (List[3] < List[5]):
		List[3], List[5] = List[5], List[3]
	if (List[4] < List[6]):
		List[4], List[6] = List[6], List[4]
	if (List[3] < List[4]):
		List[3], List[4] = List[4], List[3]
	if (List[5] < List[6]):
		List[5], List[6] = List[6], List[5]
	if (List[0] > List[4]):
		List[0], List[4] = List[4], List[0]
	if (List[1] > List[5]):
		List[1], List[5] = List[5], List[1]
	if (List[2] > List[6]):
		List[2], List[6] = List[6], List[2]
	if (List[0] > List[2]):
		List[0], List[2] = List[2], List[0]
	if (List[1] > List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[3] > List[5]):
		List[3], List[5] = List[5], List[3]
	if (List[4] > List[6]):
		List[4], List[6] = List[6], List[4]
	if (List[3] > List[4]):
		List[3], List[4] = List[4], List[3]
	if (List[5] > List[6]):
		List[5], List[6] = List[6], List[5]
	return List
