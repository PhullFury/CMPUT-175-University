def bitonic16(List):
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
	if (List[8] < List[9]):
		List[8], List[9] = List[9], List[8]
	if (List[10] > List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[8] < List[10]):
		List[8], List[10] = List[10], List[8]
	if (List[9] < List[11]):
		List[9], List[11] = List[11], List[9]
	if (List[8] < List[9]):
		List[8], List[9] = List[9], List[8]
	if (List[10] < List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[12] > List[13]):
		List[12], List[13] = List[13], List[12]
	if (List[14] < List[15]):
		List[14], List[15] = List[15], List[14]
	if (List[12] > List[14]):
		List[12], List[14] = List[14], List[12]
	if (List[13] > List[15]):
		List[13], List[15] = List[15], List[13]
	if (List[12] > List[13]):
		List[12], List[13] = List[13], List[12]
	if (List[14] > List[15]):
		List[14], List[15] = List[15], List[14]
	if (List[8] < List[12]):
		List[8], List[12] = List[12], List[8]
	if (List[9] < List[13]):
		List[9], List[13] = List[13], List[9]
	if (List[10] < List[14]):
		List[10], List[14] = List[14], List[10]
	if (List[11] < List[15]):
		List[11], List[15] = List[15], List[11]
	if (List[8] < List[10]):
		List[8], List[10] = List[10], List[8]
	if (List[9] < List[11]):
		List[9], List[11] = List[11], List[9]
	if (List[8] < List[9]):
		List[8], List[9] = List[9], List[8]
	if (List[10] < List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[12] < List[14]):
		List[12], List[14] = List[14], List[12]
	if (List[13] < List[15]):
		List[13], List[15] = List[15], List[13]
	if (List[12] < List[13]):
		List[12], List[13] = List[13], List[12]
	if (List[14] < List[15]):
		List[14], List[15] = List[15], List[14]
	if (List[0] > List[8]):
		List[0], List[8] = List[8], List[0]
	if (List[1] > List[9]):
		List[1], List[9] = List[9], List[1]
	if (List[2] > List[10]):
		List[2], List[10] = List[10], List[2]
	if (List[3] > List[11]):
		List[3], List[11] = List[11], List[3]
	if (List[4] > List[12]):
		List[4], List[12] = List[12], List[4]
	if (List[5] > List[13]):
		List[5], List[13] = List[13], List[5]
	if (List[6] > List[14]):
		List[6], List[14] = List[14], List[6]
	if (List[7] > List[15]):
		List[7], List[15] = List[15], List[7]
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
	if (List[8] > List[12]):
		List[8], List[12] = List[12], List[8]
	if (List[9] > List[13]):
		List[9], List[13] = List[13], List[9]
	if (List[10] > List[14]):
		List[10], List[14] = List[14], List[10]
	if (List[11] > List[15]):
		List[11], List[15] = List[15], List[11]
	if (List[8] > List[10]):
		List[8], List[10] = List[10], List[8]
	if (List[9] > List[11]):
		List[9], List[11] = List[11], List[9]
	if (List[8] > List[9]):
		List[8], List[9] = List[9], List[8]
	if (List[10] > List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[12] > List[14]):
		List[12], List[14] = List[14], List[12]
	if (List[13] > List[15]):
		List[13], List[15] = List[15], List[13]
	if (List[12] > List[13]):
		List[12], List[13] = List[13], List[12]
	if (List[14] > List[15]):
		List[14], List[15] = List[15], List[14]
	return List
