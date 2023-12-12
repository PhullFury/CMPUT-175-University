def bitonic50(List):
	if (List[1] < List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[0] > List[2]):
		List[0], List[2] = List[2], List[0]
	if (List[1] > List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[4] > List[5]):
		List[4], List[5] = List[5], List[4]
	if (List[3] < List[5]):
		List[3], List[5] = List[5], List[3]
	if (List[4] < List[5]):
		List[4], List[5] = List[5], List[4]
	if (List[0] > List[4]):
		List[0], List[4] = List[4], List[0]
	if (List[1] > List[5]):
		List[1], List[5] = List[5], List[1]
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	if (List[2] > List[4]):
		List[2], List[4] = List[4], List[2]
	if (List[3] > List[5]):
		List[3], List[5] = List[5], List[3]
	if (List[2] > List[3]):
		List[2], List[3] = List[3], List[2]
	if (List[4] > List[5]):
		List[4], List[5] = List[5], List[4]
	if (List[7] > List[8]):
		List[7], List[8] = List[8], List[7]
	if (List[6] < List[8]):
		List[6], List[8] = List[8], List[6]
	if (List[7] < List[8]):
		List[7], List[8] = List[8], List[7]
	if (List[10] < List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[9] > List[11]):
		List[9], List[11] = List[11], List[9]
	if (List[10] > List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[6] < List[10]):
		List[6], List[10] = List[10], List[6]
	if (List[7] < List[11]):
		List[7], List[11] = List[11], List[7]
	if (List[6] < List[7]):
		List[6], List[7] = List[7], List[6]
	if (List[8] < List[10]):
		List[8], List[10] = List[10], List[8]
	if (List[9] < List[11]):
		List[9], List[11] = List[11], List[9]
	if (List[8] < List[9]):
		List[8], List[9] = List[9], List[8]
	if (List[10] < List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[0] > List[8]):
		List[0], List[8] = List[8], List[0]
	if (List[1] > List[9]):
		List[1], List[9] = List[9], List[1]
	if (List[2] > List[10]):
		List[2], List[10] = List[10], List[2]
	if (List[3] > List[11]):
		List[3], List[11] = List[11], List[3]
	if (List[0] > List[2]):
		List[0], List[2] = List[2], List[0]
	if (List[1] > List[3]):
		List[1], List[3] = List[3], List[1]
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
	if (List[2] > List[3]):
		List[2], List[3] = List[3], List[2]
	if (List[4] > List[8]):
		List[4], List[8] = List[8], List[4]
	if (List[5] > List[9]):
		List[5], List[9] = List[9], List[5]
	if (List[6] > List[10]):
		List[6], List[10] = List[10], List[6]
	if (List[7] > List[11]):
		List[7], List[11] = List[11], List[7]
	if (List[4] > List[6]):
		List[4], List[6] = List[6], List[4]
	if (List[5] > List[7]):
		List[5], List[7] = List[7], List[5]
	if (List[4] > List[5]):
		List[4], List[5] = List[5], List[4]
	if (List[6] > List[7]):
		List[6], List[7] = List[7], List[6]
	if (List[8] > List[10]):
		List[8], List[10] = List[10], List[8]
	if (List[9] > List[11]):
		List[9], List[11] = List[11], List[9]
	if (List[8] > List[9]):
		List[8], List[9] = List[9], List[8]
	if (List[10] > List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[13] > List[14]):
		List[13], List[14] = List[14], List[13]
	if (List[12] < List[14]):
		List[12], List[14] = List[14], List[12]
	if (List[13] < List[14]):
		List[13], List[14] = List[14], List[13]
	if (List[16] < List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[15] > List[17]):
		List[15], List[17] = List[17], List[15]
	if (List[16] > List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[12] < List[16]):
		List[12], List[16] = List[16], List[12]
	if (List[13] < List[17]):
		List[13], List[17] = List[17], List[13]
	if (List[12] < List[13]):
		List[12], List[13] = List[13], List[12]
	if (List[14] < List[16]):
		List[14], List[16] = List[16], List[14]
	if (List[15] < List[17]):
		List[15], List[17] = List[17], List[15]
	if (List[14] < List[15]):
		List[14], List[15] = List[15], List[14]
	if (List[16] < List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[19] < List[20]):
		List[19], List[20] = List[20], List[19]
	if (List[18] > List[20]):
		List[18], List[20] = List[20], List[18]
	if (List[19] > List[20]):
		List[19], List[20] = List[20], List[19]
	if (List[21] < List[22]):
		List[21], List[22] = List[22], List[21]
	if (List[23] > List[24]):
		List[23], List[24] = List[24], List[23]
	if (List[21] < List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[22] < List[24]):
		List[22], List[24] = List[24], List[22]
	if (List[21] < List[22]):
		List[21], List[22] = List[22], List[21]
	if (List[23] < List[24]):
		List[23], List[24] = List[24], List[23]
	if (List[18] > List[22]):
		List[18], List[22] = List[22], List[18]
	if (List[19] > List[23]):
		List[19], List[23] = List[23], List[19]
	if (List[20] > List[24]):
		List[20], List[24] = List[24], List[20]
	if (List[18] > List[20]):
		List[18], List[20] = List[20], List[18]
	if (List[19] > List[20]):
		List[19], List[20] = List[20], List[19]
	if (List[21] > List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[22] > List[24]):
		List[22], List[24] = List[24], List[22]
	if (List[21] > List[22]):
		List[21], List[22] = List[22], List[21]
	if (List[23] > List[24]):
		List[23], List[24] = List[24], List[23]
	if (List[12] < List[20]):
		List[12], List[20] = List[20], List[12]
	if (List[13] < List[21]):
		List[13], List[21] = List[21], List[13]
	if (List[14] < List[22]):
		List[14], List[22] = List[22], List[14]
	if (List[15] < List[23]):
		List[15], List[23] = List[23], List[15]
	if (List[16] < List[24]):
		List[16], List[24] = List[24], List[16]
	if (List[12] < List[16]):
		List[12], List[16] = List[16], List[12]
	if (List[13] < List[15]):
		List[13], List[15] = List[15], List[13]
	if (List[14] < List[16]):
		List[14], List[16] = List[16], List[14]
	if (List[13] < List[14]):
		List[13], List[14] = List[14], List[13]
	if (List[15] < List[16]):
		List[15], List[16] = List[16], List[15]
	if (List[17] < List[21]):
		List[17], List[21] = List[21], List[17]
	if (List[18] < List[22]):
		List[18], List[22] = List[22], List[18]
	if (List[19] < List[23]):
		List[19], List[23] = List[23], List[19]
	if (List[20] < List[24]):
		List[20], List[24] = List[24], List[20]
	if (List[17] < List[19]):
		List[17], List[19] = List[19], List[17]
	if (List[18] < List[20]):
		List[18], List[20] = List[20], List[18]
	if (List[17] < List[18]):
		List[17], List[18] = List[18], List[17]
	if (List[19] < List[20]):
		List[19], List[20] = List[20], List[19]
	if (List[21] < List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[22] < List[24]):
		List[22], List[24] = List[24], List[22]
	if (List[21] < List[22]):
		List[21], List[22] = List[22], List[21]
	if (List[23] < List[24]):
		List[23], List[24] = List[24], List[23]
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
	if (List[0] > List[8]):
		List[0], List[8] = List[8], List[0]
	if (List[1] > List[5]):
		List[1], List[5] = List[5], List[1]
	if (List[2] > List[6]):
		List[2], List[6] = List[6], List[2]
	if (List[3] > List[7]):
		List[3], List[7] = List[7], List[3]
	if (List[4] > List[8]):
		List[4], List[8] = List[8], List[4]
	if (List[1] > List[3]):
		List[1], List[3] = List[3], List[1]
	if (List[2] > List[4]):
		List[2], List[4] = List[4], List[2]
	if (List[1] > List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[3] > List[4]):
		List[3], List[4] = List[4], List[3]
	if (List[5] > List[7]):
		List[5], List[7] = List[7], List[5]
	if (List[6] > List[8]):
		List[6], List[8] = List[8], List[6]
	if (List[5] > List[6]):
		List[5], List[6] = List[6], List[5]
	if (List[7] > List[8]):
		List[7], List[8] = List[8], List[7]
	if (List[9] > List[17]):
		List[9], List[17] = List[17], List[9]
	if (List[10] > List[18]):
		List[10], List[18] = List[18], List[10]
	if (List[11] > List[19]):
		List[11], List[19] = List[19], List[11]
	if (List[12] > List[20]):
		List[12], List[20] = List[20], List[12]
	if (List[13] > List[21]):
		List[13], List[21] = List[21], List[13]
	if (List[14] > List[22]):
		List[14], List[22] = List[22], List[14]
	if (List[15] > List[23]):
		List[15], List[23] = List[23], List[15]
	if (List[16] > List[24]):
		List[16], List[24] = List[24], List[16]
	if (List[9] > List[13]):
		List[9], List[13] = List[13], List[9]
	if (List[10] > List[14]):
		List[10], List[14] = List[14], List[10]
	if (List[11] > List[15]):
		List[11], List[15] = List[15], List[11]
	if (List[12] > List[16]):
		List[12], List[16] = List[16], List[12]
	if (List[9] > List[11]):
		List[9], List[11] = List[11], List[9]
	if (List[10] > List[12]):
		List[10], List[12] = List[12], List[10]
	if (List[9] > List[10]):
		List[9], List[10] = List[10], List[9]
	if (List[11] > List[12]):
		List[11], List[12] = List[12], List[11]
	if (List[13] > List[15]):
		List[13], List[15] = List[15], List[13]
	if (List[14] > List[16]):
		List[14], List[16] = List[16], List[14]
	if (List[13] > List[14]):
		List[13], List[14] = List[14], List[13]
	if (List[15] > List[16]):
		List[15], List[16] = List[16], List[15]
	if (List[17] > List[21]):
		List[17], List[21] = List[21], List[17]
	if (List[18] > List[22]):
		List[18], List[22] = List[22], List[18]
	if (List[19] > List[23]):
		List[19], List[23] = List[23], List[19]
	if (List[20] > List[24]):
		List[20], List[24] = List[24], List[20]
	if (List[17] > List[19]):
		List[17], List[19] = List[19], List[17]
	if (List[18] > List[20]):
		List[18], List[20] = List[20], List[18]
	if (List[17] > List[18]):
		List[17], List[18] = List[18], List[17]
	if (List[19] > List[20]):
		List[19], List[20] = List[20], List[19]
	if (List[21] > List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[22] > List[24]):
		List[22], List[24] = List[24], List[22]
	if (List[21] > List[22]):
		List[21], List[22] = List[22], List[21]
	if (List[23] > List[24]):
		List[23], List[24] = List[24], List[23]
	if (List[26] > List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[25] < List[27]):
		List[25], List[27] = List[27], List[25]
	if (List[26] < List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[29] < List[30]):
		List[29], List[30] = List[30], List[29]
	if (List[28] > List[30]):
		List[28], List[30] = List[30], List[28]
	if (List[29] > List[30]):
		List[29], List[30] = List[30], List[29]
	if (List[25] < List[29]):
		List[25], List[29] = List[29], List[25]
	if (List[26] < List[30]):
		List[26], List[30] = List[30], List[26]
	if (List[25] < List[26]):
		List[25], List[26] = List[26], List[25]
	if (List[27] < List[29]):
		List[27], List[29] = List[29], List[27]
	if (List[28] < List[30]):
		List[28], List[30] = List[30], List[28]
	if (List[27] < List[28]):
		List[27], List[28] = List[28], List[27]
	if (List[29] < List[30]):
		List[29], List[30] = List[30], List[29]
	if (List[32] < List[33]):
		List[32], List[33] = List[33], List[32]
	if (List[31] > List[33]):
		List[31], List[33] = List[33], List[31]
	if (List[32] > List[33]):
		List[32], List[33] = List[33], List[32]
	if (List[35] > List[36]):
		List[35], List[36] = List[36], List[35]
	if (List[34] < List[36]):
		List[34], List[36] = List[36], List[34]
	if (List[35] < List[36]):
		List[35], List[36] = List[36], List[35]
	if (List[31] > List[35]):
		List[31], List[35] = List[35], List[31]
	if (List[32] > List[36]):
		List[32], List[36] = List[36], List[32]
	if (List[31] > List[32]):
		List[31], List[32] = List[32], List[31]
	if (List[33] > List[35]):
		List[33], List[35] = List[35], List[33]
	if (List[34] > List[36]):
		List[34], List[36] = List[36], List[34]
	if (List[33] > List[34]):
		List[33], List[34] = List[34], List[33]
	if (List[35] > List[36]):
		List[35], List[36] = List[36], List[35]
	if (List[25] < List[33]):
		List[25], List[33] = List[33], List[25]
	if (List[26] < List[34]):
		List[26], List[34] = List[34], List[26]
	if (List[27] < List[35]):
		List[27], List[35] = List[35], List[27]
	if (List[28] < List[36]):
		List[28], List[36] = List[36], List[28]
	if (List[25] < List[27]):
		List[25], List[27] = List[27], List[25]
	if (List[26] < List[28]):
		List[26], List[28] = List[28], List[26]
	if (List[25] < List[26]):
		List[25], List[26] = List[26], List[25]
	if (List[27] < List[28]):
		List[27], List[28] = List[28], List[27]
	if (List[29] < List[33]):
		List[29], List[33] = List[33], List[29]
	if (List[30] < List[34]):
		List[30], List[34] = List[34], List[30]
	if (List[31] < List[35]):
		List[31], List[35] = List[35], List[31]
	if (List[32] < List[36]):
		List[32], List[36] = List[36], List[32]
	if (List[29] < List[31]):
		List[29], List[31] = List[31], List[29]
	if (List[30] < List[32]):
		List[30], List[32] = List[32], List[30]
	if (List[29] < List[30]):
		List[29], List[30] = List[30], List[29]
	if (List[31] < List[32]):
		List[31], List[32] = List[32], List[31]
	if (List[33] < List[35]):
		List[33], List[35] = List[35], List[33]
	if (List[34] < List[36]):
		List[34], List[36] = List[36], List[34]
	if (List[33] < List[34]):
		List[33], List[34] = List[34], List[33]
	if (List[35] < List[36]):
		List[35], List[36] = List[36], List[35]
	if (List[38] < List[39]):
		List[38], List[39] = List[39], List[38]
	if (List[37] > List[39]):
		List[37], List[39] = List[39], List[37]
	if (List[38] > List[39]):
		List[38], List[39] = List[39], List[38]
	if (List[41] > List[42]):
		List[41], List[42] = List[42], List[41]
	if (List[40] < List[42]):
		List[40], List[42] = List[42], List[40]
	if (List[41] < List[42]):
		List[41], List[42] = List[42], List[41]
	if (List[37] > List[41]):
		List[37], List[41] = List[41], List[37]
	if (List[38] > List[42]):
		List[38], List[42] = List[42], List[38]
	if (List[37] > List[38]):
		List[37], List[38] = List[38], List[37]
	if (List[39] > List[41]):
		List[39], List[41] = List[41], List[39]
	if (List[40] > List[42]):
		List[40], List[42] = List[42], List[40]
	if (List[39] > List[40]):
		List[39], List[40] = List[40], List[39]
	if (List[41] > List[42]):
		List[41], List[42] = List[42], List[41]
	if (List[44] > List[45]):
		List[44], List[45] = List[45], List[44]
	if (List[43] < List[45]):
		List[43], List[45] = List[45], List[43]
	if (List[44] < List[45]):
		List[44], List[45] = List[45], List[44]
	if (List[46] > List[47]):
		List[46], List[47] = List[47], List[46]
	if (List[48] < List[49]):
		List[48], List[49] = List[49], List[48]
	if (List[46] > List[48]):
		List[46], List[48] = List[48], List[46]
	if (List[47] > List[49]):
		List[47], List[49] = List[49], List[47]
	if (List[46] > List[47]):
		List[46], List[47] = List[47], List[46]
	if (List[48] > List[49]):
		List[48], List[49] = List[49], List[48]
	if (List[43] < List[47]):
		List[43], List[47] = List[47], List[43]
	if (List[44] < List[48]):
		List[44], List[48] = List[48], List[44]
	if (List[45] < List[49]):
		List[45], List[49] = List[49], List[45]
	if (List[43] < List[45]):
		List[43], List[45] = List[45], List[43]
	if (List[44] < List[45]):
		List[44], List[45] = List[45], List[44]
	if (List[46] < List[48]):
		List[46], List[48] = List[48], List[46]
	if (List[47] < List[49]):
		List[47], List[49] = List[49], List[47]
	if (List[46] < List[47]):
		List[46], List[47] = List[47], List[46]
	if (List[48] < List[49]):
		List[48], List[49] = List[49], List[48]
	if (List[37] > List[45]):
		List[37], List[45] = List[45], List[37]
	if (List[38] > List[46]):
		List[38], List[46] = List[46], List[38]
	if (List[39] > List[47]):
		List[39], List[47] = List[47], List[39]
	if (List[40] > List[48]):
		List[40], List[48] = List[48], List[40]
	if (List[41] > List[49]):
		List[41], List[49] = List[49], List[41]
	if (List[37] > List[41]):
		List[37], List[41] = List[41], List[37]
	if (List[38] > List[40]):
		List[38], List[40] = List[40], List[38]
	if (List[39] > List[41]):
		List[39], List[41] = List[41], List[39]
	if (List[38] > List[39]):
		List[38], List[39] = List[39], List[38]
	if (List[40] > List[41]):
		List[40], List[41] = List[41], List[40]
	if (List[42] > List[46]):
		List[42], List[46] = List[46], List[42]
	if (List[43] > List[47]):
		List[43], List[47] = List[47], List[43]
	if (List[44] > List[48]):
		List[44], List[48] = List[48], List[44]
	if (List[45] > List[49]):
		List[45], List[49] = List[49], List[45]
	if (List[42] > List[44]):
		List[42], List[44] = List[44], List[42]
	if (List[43] > List[45]):
		List[43], List[45] = List[45], List[43]
	if (List[42] > List[43]):
		List[42], List[43] = List[43], List[42]
	if (List[44] > List[45]):
		List[44], List[45] = List[45], List[44]
	if (List[46] > List[48]):
		List[46], List[48] = List[48], List[46]
	if (List[47] > List[49]):
		List[47], List[49] = List[49], List[47]
	if (List[46] > List[47]):
		List[46], List[47] = List[47], List[46]
	if (List[48] > List[49]):
		List[48], List[49] = List[49], List[48]
	if (List[25] < List[41]):
		List[25], List[41] = List[41], List[25]
	if (List[26] < List[42]):
		List[26], List[42] = List[42], List[26]
	if (List[27] < List[43]):
		List[27], List[43] = List[43], List[27]
	if (List[28] < List[44]):
		List[28], List[44] = List[44], List[28]
	if (List[29] < List[45]):
		List[29], List[45] = List[45], List[29]
	if (List[30] < List[46]):
		List[30], List[46] = List[46], List[30]
	if (List[31] < List[47]):
		List[31], List[47] = List[47], List[31]
	if (List[32] < List[48]):
		List[32], List[48] = List[48], List[32]
	if (List[33] < List[49]):
		List[33], List[49] = List[49], List[33]
	if (List[25] < List[33]):
		List[25], List[33] = List[33], List[25]
	if (List[26] < List[30]):
		List[26], List[30] = List[30], List[26]
	if (List[27] < List[31]):
		List[27], List[31] = List[31], List[27]
	if (List[28] < List[32]):
		List[28], List[32] = List[32], List[28]
	if (List[29] < List[33]):
		List[29], List[33] = List[33], List[29]
	if (List[26] < List[28]):
		List[26], List[28] = List[28], List[26]
	if (List[27] < List[29]):
		List[27], List[29] = List[29], List[27]
	if (List[26] < List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[28] < List[29]):
		List[28], List[29] = List[29], List[28]
	if (List[30] < List[32]):
		List[30], List[32] = List[32], List[30]
	if (List[31] < List[33]):
		List[31], List[33] = List[33], List[31]
	if (List[30] < List[31]):
		List[30], List[31] = List[31], List[30]
	if (List[32] < List[33]):
		List[32], List[33] = List[33], List[32]
	if (List[34] < List[42]):
		List[34], List[42] = List[42], List[34]
	if (List[35] < List[43]):
		List[35], List[43] = List[43], List[35]
	if (List[36] < List[44]):
		List[36], List[44] = List[44], List[36]
	if (List[37] < List[45]):
		List[37], List[45] = List[45], List[37]
	if (List[38] < List[46]):
		List[38], List[46] = List[46], List[38]
	if (List[39] < List[47]):
		List[39], List[47] = List[47], List[39]
	if (List[40] < List[48]):
		List[40], List[48] = List[48], List[40]
	if (List[41] < List[49]):
		List[41], List[49] = List[49], List[41]
	if (List[34] < List[38]):
		List[34], List[38] = List[38], List[34]
	if (List[35] < List[39]):
		List[35], List[39] = List[39], List[35]
	if (List[36] < List[40]):
		List[36], List[40] = List[40], List[36]
	if (List[37] < List[41]):
		List[37], List[41] = List[41], List[37]
	if (List[34] < List[36]):
		List[34], List[36] = List[36], List[34]
	if (List[35] < List[37]):
		List[35], List[37] = List[37], List[35]
	if (List[34] < List[35]):
		List[34], List[35] = List[35], List[34]
	if (List[36] < List[37]):
		List[36], List[37] = List[37], List[36]
	if (List[38] < List[40]):
		List[38], List[40] = List[40], List[38]
	if (List[39] < List[41]):
		List[39], List[41] = List[41], List[39]
	if (List[38] < List[39]):
		List[38], List[39] = List[39], List[38]
	if (List[40] < List[41]):
		List[40], List[41] = List[41], List[40]
	if (List[42] < List[46]):
		List[42], List[46] = List[46], List[42]
	if (List[43] < List[47]):
		List[43], List[47] = List[47], List[43]
	if (List[44] < List[48]):
		List[44], List[48] = List[48], List[44]
	if (List[45] < List[49]):
		List[45], List[49] = List[49], List[45]
	if (List[42] < List[44]):
		List[42], List[44] = List[44], List[42]
	if (List[43] < List[45]):
		List[43], List[45] = List[45], List[43]
	if (List[42] < List[43]):
		List[42], List[43] = List[43], List[42]
	if (List[44] < List[45]):
		List[44], List[45] = List[45], List[44]
	if (List[46] < List[48]):
		List[46], List[48] = List[48], List[46]
	if (List[47] < List[49]):
		List[47], List[49] = List[49], List[47]
	if (List[46] < List[47]):
		List[46], List[47] = List[47], List[46]
	if (List[48] < List[49]):
		List[48], List[49] = List[49], List[48]
	if (List[0] > List[32]):
		List[0], List[32] = List[32], List[0]
	if (List[1] > List[33]):
		List[1], List[33] = List[33], List[1]
	if (List[2] > List[34]):
		List[2], List[34] = List[34], List[2]
	if (List[3] > List[35]):
		List[3], List[35] = List[35], List[3]
	if (List[4] > List[36]):
		List[4], List[36] = List[36], List[4]
	if (List[5] > List[37]):
		List[5], List[37] = List[37], List[5]
	if (List[6] > List[38]):
		List[6], List[38] = List[38], List[6]
	if (List[7] > List[39]):
		List[7], List[39] = List[39], List[7]
	if (List[8] > List[40]):
		List[8], List[40] = List[40], List[8]
	if (List[9] > List[41]):
		List[9], List[41] = List[41], List[9]
	if (List[10] > List[42]):
		List[10], List[42] = List[42], List[10]
	if (List[11] > List[43]):
		List[11], List[43] = List[43], List[11]
	if (List[12] > List[44]):
		List[12], List[44] = List[44], List[12]
	if (List[13] > List[45]):
		List[13], List[45] = List[45], List[13]
	if (List[14] > List[46]):
		List[14], List[46] = List[46], List[14]
	if (List[15] > List[47]):
		List[15], List[47] = List[47], List[15]
	if (List[16] > List[48]):
		List[16], List[48] = List[48], List[16]
	if (List[17] > List[49]):
		List[17], List[49] = List[49], List[17]
	if (List[0] > List[16]):
		List[0], List[16] = List[16], List[0]
	if (List[1] > List[17]):
		List[1], List[17] = List[17], List[1]
	if (List[0] > List[1]):
		List[0], List[1] = List[1], List[0]
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
	if (List[8] > List[16]):
		List[8], List[16] = List[16], List[8]
	if (List[9] > List[17]):
		List[9], List[17] = List[17], List[9]
	if (List[2] > List[6]):
		List[2], List[6] = List[6], List[2]
	if (List[3] > List[7]):
		List[3], List[7] = List[7], List[3]
	if (List[4] > List[8]):
		List[4], List[8] = List[8], List[4]
	if (List[5] > List[9]):
		List[5], List[9] = List[9], List[5]
	if (List[2] > List[4]):
		List[2], List[4] = List[4], List[2]
	if (List[3] > List[5]):
		List[3], List[5] = List[5], List[3]
	if (List[2] > List[3]):
		List[2], List[3] = List[3], List[2]
	if (List[4] > List[5]):
		List[4], List[5] = List[5], List[4]
	if (List[6] > List[8]):
		List[6], List[8] = List[8], List[6]
	if (List[7] > List[9]):
		List[7], List[9] = List[9], List[7]
	if (List[6] > List[7]):
		List[6], List[7] = List[7], List[6]
	if (List[8] > List[9]):
		List[8], List[9] = List[9], List[8]
	if (List[10] > List[14]):
		List[10], List[14] = List[14], List[10]
	if (List[11] > List[15]):
		List[11], List[15] = List[15], List[11]
	if (List[12] > List[16]):
		List[12], List[16] = List[16], List[12]
	if (List[13] > List[17]):
		List[13], List[17] = List[17], List[13]
	if (List[10] > List[12]):
		List[10], List[12] = List[12], List[10]
	if (List[11] > List[13]):
		List[11], List[13] = List[13], List[11]
	if (List[10] > List[11]):
		List[10], List[11] = List[11], List[10]
	if (List[12] > List[13]):
		List[12], List[13] = List[13], List[12]
	if (List[14] > List[16]):
		List[14], List[16] = List[16], List[14]
	if (List[15] > List[17]):
		List[15], List[17] = List[17], List[15]
	if (List[14] > List[15]):
		List[14], List[15] = List[15], List[14]
	if (List[16] > List[17]):
		List[16], List[17] = List[17], List[16]
	if (List[18] > List[34]):
		List[18], List[34] = List[34], List[18]
	if (List[19] > List[35]):
		List[19], List[35] = List[35], List[19]
	if (List[20] > List[36]):
		List[20], List[36] = List[36], List[20]
	if (List[21] > List[37]):
		List[21], List[37] = List[37], List[21]
	if (List[22] > List[38]):
		List[22], List[38] = List[38], List[22]
	if (List[23] > List[39]):
		List[23], List[39] = List[39], List[23]
	if (List[24] > List[40]):
		List[24], List[40] = List[40], List[24]
	if (List[25] > List[41]):
		List[25], List[41] = List[41], List[25]
	if (List[26] > List[42]):
		List[26], List[42] = List[42], List[26]
	if (List[27] > List[43]):
		List[27], List[43] = List[43], List[27]
	if (List[28] > List[44]):
		List[28], List[44] = List[44], List[28]
	if (List[29] > List[45]):
		List[29], List[45] = List[45], List[29]
	if (List[30] > List[46]):
		List[30], List[46] = List[46], List[30]
	if (List[31] > List[47]):
		List[31], List[47] = List[47], List[31]
	if (List[32] > List[48]):
		List[32], List[48] = List[48], List[32]
	if (List[33] > List[49]):
		List[33], List[49] = List[49], List[33]
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
	if (List[24] > List[32]):
		List[24], List[32] = List[32], List[24]
	if (List[25] > List[33]):
		List[25], List[33] = List[33], List[25]
	if (List[18] > List[22]):
		List[18], List[22] = List[22], List[18]
	if (List[19] > List[23]):
		List[19], List[23] = List[23], List[19]
	if (List[20] > List[24]):
		List[20], List[24] = List[24], List[20]
	if (List[21] > List[25]):
		List[21], List[25] = List[25], List[21]
	if (List[18] > List[20]):
		List[18], List[20] = List[20], List[18]
	if (List[19] > List[21]):
		List[19], List[21] = List[21], List[19]
	if (List[18] > List[19]):
		List[18], List[19] = List[19], List[18]
	if (List[20] > List[21]):
		List[20], List[21] = List[21], List[20]
	if (List[22] > List[24]):
		List[22], List[24] = List[24], List[22]
	if (List[23] > List[25]):
		List[23], List[25] = List[25], List[23]
	if (List[22] > List[23]):
		List[22], List[23] = List[23], List[22]
	if (List[24] > List[25]):
		List[24], List[25] = List[25], List[24]
	if (List[26] > List[30]):
		List[26], List[30] = List[30], List[26]
	if (List[27] > List[31]):
		List[27], List[31] = List[31], List[27]
	if (List[28] > List[32]):
		List[28], List[32] = List[32], List[28]
	if (List[29] > List[33]):
		List[29], List[33] = List[33], List[29]
	if (List[26] > List[28]):
		List[26], List[28] = List[28], List[26]
	if (List[27] > List[29]):
		List[27], List[29] = List[29], List[27]
	if (List[26] > List[27]):
		List[26], List[27] = List[27], List[26]
	if (List[28] > List[29]):
		List[28], List[29] = List[29], List[28]
	if (List[30] > List[32]):
		List[30], List[32] = List[32], List[30]
	if (List[31] > List[33]):
		List[31], List[33] = List[33], List[31]
	if (List[30] > List[31]):
		List[30], List[31] = List[31], List[30]
	if (List[32] > List[33]):
		List[32], List[33] = List[33], List[32]
	if (List[34] > List[42]):
		List[34], List[42] = List[42], List[34]
	if (List[35] > List[43]):
		List[35], List[43] = List[43], List[35]
	if (List[36] > List[44]):
		List[36], List[44] = List[44], List[36]
	if (List[37] > List[45]):
		List[37], List[45] = List[45], List[37]
	if (List[38] > List[46]):
		List[38], List[46] = List[46], List[38]
	if (List[39] > List[47]):
		List[39], List[47] = List[47], List[39]
	if (List[40] > List[48]):
		List[40], List[48] = List[48], List[40]
	if (List[41] > List[49]):
		List[41], List[49] = List[49], List[41]
	if (List[34] > List[38]):
		List[34], List[38] = List[38], List[34]
	if (List[35] > List[39]):
		List[35], List[39] = List[39], List[35]
	if (List[36] > List[40]):
		List[36], List[40] = List[40], List[36]
	if (List[37] > List[41]):
		List[37], List[41] = List[41], List[37]
	if (List[34] > List[36]):
		List[34], List[36] = List[36], List[34]
	if (List[35] > List[37]):
		List[35], List[37] = List[37], List[35]
	if (List[34] > List[35]):
		List[34], List[35] = List[35], List[34]
	if (List[36] > List[37]):
		List[36], List[37] = List[37], List[36]
	if (List[38] > List[40]):
		List[38], List[40] = List[40], List[38]
	if (List[39] > List[41]):
		List[39], List[41] = List[41], List[39]
	if (List[38] > List[39]):
		List[38], List[39] = List[39], List[38]
	if (List[40] > List[41]):
		List[40], List[41] = List[41], List[40]
	if (List[42] > List[46]):
		List[42], List[46] = List[46], List[42]
	if (List[43] > List[47]):
		List[43], List[47] = List[47], List[43]
	if (List[44] > List[48]):
		List[44], List[48] = List[48], List[44]
	if (List[45] > List[49]):
		List[45], List[49] = List[49], List[45]
	if (List[42] > List[44]):
		List[42], List[44] = List[44], List[42]
	if (List[43] > List[45]):
		List[43], List[45] = List[45], List[43]
	if (List[42] > List[43]):
		List[42], List[43] = List[43], List[42]
	if (List[44] > List[45]):
		List[44], List[45] = List[45], List[44]
	if (List[46] > List[48]):
		List[46], List[48] = List[48], List[46]
	if (List[47] > List[49]):
		List[47], List[49] = List[49], List[47]
	if (List[46] > List[47]):
		List[46], List[47] = List[47], List[46]
	if (List[48] > List[49]):
		List[48], List[49] = List[49], List[48]
	return List
