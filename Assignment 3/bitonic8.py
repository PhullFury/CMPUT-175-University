def bitonic8(List):
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	if (List[2] < List[3]):
		List[2], List[3] = List[3], List[2]
	if (List[0] > List[2]):
		List[0], List[2] = List[2], List[0]
	if (List[1] > List[3]):
		List[1], List[3] = List[3], List[1]
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	if (List[2] > List[3]):
		List[2], List[3] = List[3], List[2]
	if (List[4] < List[5]):
		List[4], List[5] = List[5], List[4]
	if (List[6] > List[7]):
		List[6], List[7] = List[7], List[6]
	if (List[4] < List[6]):
		List[4], List[6] = List[6], List[4]
	if (List[5] < List[7]):
		List[5], List[7] = List[7], List[5]
	if (List[4] < List[5]):
		List[4], List[5] = List[5], List[4]
	if (List[6] < List[7]):
		List[6], List[7] = List[7], List[6]
	if (List[0] > List[4]):
		List[0], List[4] = List[4], List[0]
	if (List[1] > List[5]):
		List[1], List[5] = List[5], List[1]
	if (List[2] > List[6]):
		List[2], List[6] = List[6], List[2]
	if (List[3] > List[7]):
		List[3], List[7] = List[7], List[3]
	if (List[0] > List[2]):
		List[0], List[2] = List[2], List[0]
	if (List[1] > List[3]):
		List[1], List[3] = List[3], List[1]
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	if (List[2] > List[3]):
		List[2], List[3] = List[3], List[2]
	if (List[4] > List[6]):
		List[4], List[6] = List[6], List[4]
	if (List[5] > List[7]):
		List[5], List[7] = List[7], List[5]
	if (List[4] > List[5]):
		List[4], List[5] = List[5], List[4]
	if (List[6] > List[7]):
		List[6], List[7] = List[7], List[6]
	return List
