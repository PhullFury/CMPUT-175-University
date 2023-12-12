def bitonic32(List):
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
	if (List[16] < List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[18] > List[19]):
		List[18], List[19] = List[19], List[18]
	if (List[16] < List[18]):
		List[16], List[18] = List[18], List[16]
	if (List[17] < List[19]):
		List[17], List[19] = List[19], List[17]
	if (List[16] < List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[18] < List[19]):
		List[18], List[19] = List[19], List[18]
	if (List[20] > List[21]):
		List[20], List[21] = List[21], List[20]
	if (List[22] < List[23]):
		List[22], List[23] = List[23], List[22]
	if (List[20] > List[22]):
		List[20], List[22] = List[22], List[20]
	if (List[21] > List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[20] > List[21]):
		List[20], List[21] = List[21], List[20]
	if (List[22] > List[23]):
		List[22], List[23] = List[23], List[22]
	if (List[16] < List[20]):
		List[16], List[20] = List[20], List[16]
	if (List[17] < List[21]):
		List[17], List[21] = List[21], List[17]
	if (List[18] < List[22]):
		List[18], List[22] = List[22], List[18]
	if (List[19] < List[23]):
		List[19], List[23] = List[23], List[19]
	if (List[16] < List[18]):
		List[16], List[18] = List[18], List[16]
	if (List[17] < List[19]):
		List[17], List[19] = List[19], List[17]
	if (List[16] < List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[18] < List[19]):
		List[18], List[19] = List[19], List[18]
	if (List[20] < List[22]):
		List[20], List[22] = List[22], List[20]
	if (List[21] < List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[20] < List[21]):
		List[20], List[21] = List[21], List[20]
	if (List[22] < List[23]):
		List[22], List[23] = List[23], List[22]
	if (List[24] > List[25]):
		List[24], List[25] = List[25], List[24]
	if (List[26] < List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[24] > List[26]):
		List[24], List[26] = List[26], List[24]
	if (List[25] > List[27]):
		List[25], List[27] = List[27], List[25]
	if (List[24] > List[25]):
		List[24], List[25] = List[25], List[24]
	if (List[26] > List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[28] < List[29]):
		List[28], List[29] = List[29], List[28]
	if (List[30] > List[31]):
		List[30], List[31] = List[31], List[30]
	if (List[28] < List[30]):
		List[28], List[30] = List[30], List[28]
	if (List[29] < List[31]):
		List[29], List[31] = List[31], List[29]
	if (List[28] < List[29]):
		List[28], List[29] = List[29], List[28]
	if (List[30] < List[31]):
		List[30], List[31] = List[31], List[30]
	if (List[24] > List[28]):
		List[24], List[28] = List[28], List[24]
	if (List[25] > List[29]):
		List[25], List[29] = List[29], List[25]
	if (List[26] > List[30]):
		List[26], List[30] = List[30], List[26]
	if (List[27] > List[31]):
		List[27], List[31] = List[31], List[27]
	if (List[24] > List[26]):
		List[24], List[26] = List[26], List[24]
	if (List[25] > List[27]):
		List[25], List[27] = List[27], List[25]
	if (List[24] > List[25]):
		List[24], List[25] = List[25], List[24]
	if (List[26] > List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[28] > List[30]):
		List[28], List[30] = List[30], List[28]
	if (List[29] > List[31]):
		List[29], List[31] = List[31], List[29]
	if (List[28] > List[29]):
		List[28], List[29] = List[29], List[28]
	if (List[30] > List[31]):
		List[30], List[31] = List[31], List[30]
	if (List[16] < List[24]):
		List[16], List[24] = List[24], List[16]
	if (List[17] < List[25]):
		List[17], List[25] = List[25], List[17]
	if (List[18] < List[26]):
		List[18], List[26] = List[26], List[18]
	if (List[19] < List[27]):
		List[19], List[27] = List[27], List[19]
	if (List[20] < List[28]):
		List[20], List[28] = List[28], List[20]
	if (List[21] < List[29]):
		List[21], List[29] = List[29], List[21]
	if (List[22] < List[30]):
		List[22], List[30] = List[30], List[22]
	if (List[23] < List[31]):
		List[23], List[31] = List[31], List[23]
	if (List[16] < List[20]):
		List[16], List[20] = List[20], List[16]
	if (List[17] < List[21]):
		List[17], List[21] = List[21], List[17]
	if (List[18] < List[22]):
		List[18], List[22] = List[22], List[18]
	if (List[19] < List[23]):
		List[19], List[23] = List[23], List[19]
	if (List[16] < List[18]):
		List[16], List[18] = List[18], List[16]
	if (List[17] < List[19]):
		List[17], List[19] = List[19], List[17]
	if (List[16] < List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[18] < List[19]):
		List[18], List[19] = List[19], List[18]
	if (List[20] < List[22]):
		List[20], List[22] = List[22], List[20]
	if (List[21] < List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[20] < List[21]):
		List[20], List[21] = List[21], List[20]
	if (List[22] < List[23]):
		List[22], List[23] = List[23], List[22]
	if (List[24] < List[28]):
		List[24], List[28] = List[28], List[24]
	if (List[25] < List[29]):
		List[25], List[29] = List[29], List[25]
	if (List[26] < List[30]):
		List[26], List[30] = List[30], List[26]
	if (List[27] < List[31]):
		List[27], List[31] = List[31], List[27]
	if (List[24] < List[26]):
		List[24], List[26] = List[26], List[24]
	if (List[25] < List[27]):
		List[25], List[27] = List[27], List[25]
	if (List[24] < List[25]):
		List[24], List[25] = List[25], List[24]
	if (List[26] < List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[28] < List[30]):
		List[28], List[30] = List[30], List[28]
	if (List[29] < List[31]):
		List[29], List[31] = List[31], List[29]
	if (List[28] < List[29]):
		List[28], List[29] = List[29], List[28]
	if (List[30] < List[31]):
		List[30], List[31] = List[31], List[30]
	if (List[0] > List[16]):
		List[0], List[16] = List[16], List[0]
	if (List[1] > List[17]):
		List[1], List[17] = List[17], List[1]
	if (List[2] > List[18]):
		List[2], List[18] = List[18], List[2]
	if (List[3] > List[19]):
		List[3], List[19] = List[19], List[3]
	if (List[4] > List[20]):
		List[4], List[20] = List[20], List[4]
	if (List[5] > List[21]):
		List[5], List[21] = List[21], List[5]
	if (List[6] > List[22]):
		List[6], List[22] = List[22], List[6]
	if (List[7] > List[23]):
		List[7], List[23] = List[23], List[7]
	if (List[8] > List[24]):
		List[8], List[24] = List[24], List[8]
	if (List[9] > List[25]):
		List[9], List[25] = List[25], List[9]
	if (List[10] > List[26]):
		List[10], List[26] = List[26], List[10]
	if (List[11] > List[27]):
		List[11], List[27] = List[27], List[11]
	if (List[12] > List[28]):
		List[12], List[28] = List[28], List[12]
	if (List[13] > List[29]):
		List[13], List[29] = List[29], List[13]
	if (List[14] > List[30]):
		List[14], List[30] = List[30], List[14]
	if (List[15] > List[31]):
		List[15], List[31] = List[31], List[15]
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
	if (List[16] > List[24]):
		List[16], List[24] = List[24], List[16]
	if (List[17] > List[25]):
		List[17], List[25] = List[25], List[17]
	if (List[18] > List[26]):
		List[18], List[26] = List[26], List[18]
	if (List[19] > List[27]):
		List[19], List[27] = List[27], List[19]
	if (List[20] > List[28]):
		List[20], List[28] = List[28], List[20]
	if (List[21] > List[29]):
		List[21], List[29] = List[29], List[21]
	if (List[22] > List[30]):
		List[22], List[30] = List[30], List[22]
	if (List[23] > List[31]):
		List[23], List[31] = List[31], List[23]
	if (List[16] > List[20]):
		List[16], List[20] = List[20], List[16]
	if (List[17] > List[21]):
		List[17], List[21] = List[21], List[17]
	if (List[18] > List[22]):
		List[18], List[22] = List[22], List[18]
	if (List[19] > List[23]):
		List[19], List[23] = List[23], List[19]
	if (List[16] > List[18]):
		List[16], List[18] = List[18], List[16]
	if (List[17] > List[19]):
		List[17], List[19] = List[19], List[17]
	if (List[16] > List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[18] > List[19]):
		List[18], List[19] = List[19], List[18]
	if (List[20] > List[22]):
		List[20], List[22] = List[22], List[20]
	if (List[21] > List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[20] > List[21]):
		List[20], List[21] = List[21], List[20]
	if (List[22] > List[23]):
		List[22], List[23] = List[23], List[22]
	if (List[24] > List[28]):
		List[24], List[28] = List[28], List[24]
	if (List[25] > List[29]):
		List[25], List[29] = List[29], List[25]
	if (List[26] > List[30]):
		List[26], List[30] = List[30], List[26]
	if (List[27] > List[31]):
		List[27], List[31] = List[31], List[27]
	if (List[24] > List[26]):
		List[24], List[26] = List[26], List[24]
	if (List[25] > List[27]):
		List[25], List[27] = List[27], List[25]
	if (List[24] > List[25]):
		List[24], List[25] = List[25], List[24]
	if (List[26] > List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[28] > List[30]):
		List[28], List[30] = List[30], List[28]
	if (List[29] > List[31]):
		List[29], List[31] = List[31], List[29]
	if (List[28] > List[29]):
		List[28], List[29] = List[29], List[28]
	if (List[30] > List[31]):
		List[30], List[31] = List[31], List[30]
	return List
