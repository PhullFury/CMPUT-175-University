def bitonic101(List):
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
	if (List[51] > List[52]):
		List[51], List[52] = List[52], List[51]
	if (List[50] < List[52]):
		List[50], List[52] = List[52], List[50]
	if (List[51] < List[52]):
		List[51], List[52] = List[52], List[51]
	if (List[54] < List[55]):
		List[54], List[55] = List[55], List[54]
	if (List[53] > List[55]):
		List[53], List[55] = List[55], List[53]
	if (List[54] > List[55]):
		List[54], List[55] = List[55], List[54]
	if (List[50] < List[54]):
		List[50], List[54] = List[54], List[50]
	if (List[51] < List[55]):
		List[51], List[55] = List[55], List[51]
	if (List[50] < List[51]):
		List[50], List[51] = List[51], List[50]
	if (List[52] < List[54]):
		List[52], List[54] = List[54], List[52]
	if (List[53] < List[55]):
		List[53], List[55] = List[55], List[53]
	if (List[52] < List[53]):
		List[52], List[53] = List[53], List[52]
	if (List[54] < List[55]):
		List[54], List[55] = List[55], List[54]
	if (List[57] < List[58]):
		List[57], List[58] = List[58], List[57]
	if (List[56] > List[58]):
		List[56], List[58] = List[58], List[56]
	if (List[57] > List[58]):
		List[57], List[58] = List[58], List[57]
	if (List[60] > List[61]):
		List[60], List[61] = List[61], List[60]
	if (List[59] < List[61]):
		List[59], List[61] = List[61], List[59]
	if (List[60] < List[61]):
		List[60], List[61] = List[61], List[60]
	if (List[56] > List[60]):
		List[56], List[60] = List[60], List[56]
	if (List[57] > List[61]):
		List[57], List[61] = List[61], List[57]
	if (List[56] > List[57]):
		List[56], List[57] = List[57], List[56]
	if (List[58] > List[60]):
		List[58], List[60] = List[60], List[58]
	if (List[59] > List[61]):
		List[59], List[61] = List[61], List[59]
	if (List[58] > List[59]):
		List[58], List[59] = List[59], List[58]
	if (List[60] > List[61]):
		List[60], List[61] = List[61], List[60]
	if (List[50] < List[58]):
		List[50], List[58] = List[58], List[50]
	if (List[51] < List[59]):
		List[51], List[59] = List[59], List[51]
	if (List[52] < List[60]):
		List[52], List[60] = List[60], List[52]
	if (List[53] < List[61]):
		List[53], List[61] = List[61], List[53]
	if (List[50] < List[52]):
		List[50], List[52] = List[52], List[50]
	if (List[51] < List[53]):
		List[51], List[53] = List[53], List[51]
	if (List[50] < List[51]):
		List[50], List[51] = List[51], List[50]
	if (List[52] < List[53]):
		List[52], List[53] = List[53], List[52]
	if (List[54] < List[58]):
		List[54], List[58] = List[58], List[54]
	if (List[55] < List[59]):
		List[55], List[59] = List[59], List[55]
	if (List[56] < List[60]):
		List[56], List[60] = List[60], List[56]
	if (List[57] < List[61]):
		List[57], List[61] = List[61], List[57]
	if (List[54] < List[56]):
		List[54], List[56] = List[56], List[54]
	if (List[55] < List[57]):
		List[55], List[57] = List[57], List[55]
	if (List[54] < List[55]):
		List[54], List[55] = List[55], List[54]
	if (List[56] < List[57]):
		List[56], List[57] = List[57], List[56]
	if (List[58] < List[60]):
		List[58], List[60] = List[60], List[58]
	if (List[59] < List[61]):
		List[59], List[61] = List[61], List[59]
	if (List[58] < List[59]):
		List[58], List[59] = List[59], List[58]
	if (List[60] < List[61]):
		List[60], List[61] = List[61], List[60]
	if (List[63] < List[64]):
		List[63], List[64] = List[64], List[63]
	if (List[62] > List[64]):
		List[62], List[64] = List[64], List[62]
	if (List[63] > List[64]):
		List[63], List[64] = List[64], List[63]
	if (List[66] > List[67]):
		List[66], List[67] = List[67], List[66]
	if (List[65] < List[67]):
		List[65], List[67] = List[67], List[65]
	if (List[66] < List[67]):
		List[66], List[67] = List[67], List[66]
	if (List[62] > List[66]):
		List[62], List[66] = List[66], List[62]
	if (List[63] > List[67]):
		List[63], List[67] = List[67], List[63]
	if (List[62] > List[63]):
		List[62], List[63] = List[63], List[62]
	if (List[64] > List[66]):
		List[64], List[66] = List[66], List[64]
	if (List[65] > List[67]):
		List[65], List[67] = List[67], List[65]
	if (List[64] > List[65]):
		List[64], List[65] = List[65], List[64]
	if (List[66] > List[67]):
		List[66], List[67] = List[67], List[66]
	if (List[69] > List[70]):
		List[69], List[70] = List[70], List[69]
	if (List[68] < List[70]):
		List[68], List[70] = List[70], List[68]
	if (List[69] < List[70]):
		List[69], List[70] = List[70], List[69]
	if (List[71] > List[72]):
		List[71], List[72] = List[72], List[71]
	if (List[73] < List[74]):
		List[73], List[74] = List[74], List[73]
	if (List[71] > List[73]):
		List[71], List[73] = List[73], List[71]
	if (List[72] > List[74]):
		List[72], List[74] = List[74], List[72]
	if (List[71] > List[72]):
		List[71], List[72] = List[72], List[71]
	if (List[73] > List[74]):
		List[73], List[74] = List[74], List[73]
	if (List[68] < List[72]):
		List[68], List[72] = List[72], List[68]
	if (List[69] < List[73]):
		List[69], List[73] = List[73], List[69]
	if (List[70] < List[74]):
		List[70], List[74] = List[74], List[70]
	if (List[68] < List[70]):
		List[68], List[70] = List[70], List[68]
	if (List[69] < List[70]):
		List[69], List[70] = List[70], List[69]
	if (List[71] < List[73]):
		List[71], List[73] = List[73], List[71]
	if (List[72] < List[74]):
		List[72], List[74] = List[74], List[72]
	if (List[71] < List[72]):
		List[71], List[72] = List[72], List[71]
	if (List[73] < List[74]):
		List[73], List[74] = List[74], List[73]
	if (List[62] > List[70]):
		List[62], List[70] = List[70], List[62]
	if (List[63] > List[71]):
		List[63], List[71] = List[71], List[63]
	if (List[64] > List[72]):
		List[64], List[72] = List[72], List[64]
	if (List[65] > List[73]):
		List[65], List[73] = List[73], List[65]
	if (List[66] > List[74]):
		List[66], List[74] = List[74], List[66]
	if (List[62] > List[66]):
		List[62], List[66] = List[66], List[62]
	if (List[63] > List[65]):
		List[63], List[65] = List[65], List[63]
	if (List[64] > List[66]):
		List[64], List[66] = List[66], List[64]
	if (List[63] > List[64]):
		List[63], List[64] = List[64], List[63]
	if (List[65] > List[66]):
		List[65], List[66] = List[66], List[65]
	if (List[67] > List[71]):
		List[67], List[71] = List[71], List[67]
	if (List[68] > List[72]):
		List[68], List[72] = List[72], List[68]
	if (List[69] > List[73]):
		List[69], List[73] = List[73], List[69]
	if (List[70] > List[74]):
		List[70], List[74] = List[74], List[70]
	if (List[67] > List[69]):
		List[67], List[69] = List[69], List[67]
	if (List[68] > List[70]):
		List[68], List[70] = List[70], List[68]
	if (List[67] > List[68]):
		List[67], List[68] = List[68], List[67]
	if (List[69] > List[70]):
		List[69], List[70] = List[70], List[69]
	if (List[71] > List[73]):
		List[71], List[73] = List[73], List[71]
	if (List[72] > List[74]):
		List[72], List[74] = List[74], List[72]
	if (List[71] > List[72]):
		List[71], List[72] = List[72], List[71]
	if (List[73] > List[74]):
		List[73], List[74] = List[74], List[73]
	if (List[50] < List[66]):
		List[50], List[66] = List[66], List[50]
	if (List[51] < List[67]):
		List[51], List[67] = List[67], List[51]
	if (List[52] < List[68]):
		List[52], List[68] = List[68], List[52]
	if (List[53] < List[69]):
		List[53], List[69] = List[69], List[53]
	if (List[54] < List[70]):
		List[54], List[70] = List[70], List[54]
	if (List[55] < List[71]):
		List[55], List[71] = List[71], List[55]
	if (List[56] < List[72]):
		List[56], List[72] = List[72], List[56]
	if (List[57] < List[73]):
		List[57], List[73] = List[73], List[57]
	if (List[58] < List[74]):
		List[58], List[74] = List[74], List[58]
	if (List[50] < List[58]):
		List[50], List[58] = List[58], List[50]
	if (List[51] < List[55]):
		List[51], List[55] = List[55], List[51]
	if (List[52] < List[56]):
		List[52], List[56] = List[56], List[52]
	if (List[53] < List[57]):
		List[53], List[57] = List[57], List[53]
	if (List[54] < List[58]):
		List[54], List[58] = List[58], List[54]
	if (List[51] < List[53]):
		List[51], List[53] = List[53], List[51]
	if (List[52] < List[54]):
		List[52], List[54] = List[54], List[52]
	if (List[51] < List[52]):
		List[51], List[52] = List[52], List[51]
	if (List[53] < List[54]):
		List[53], List[54] = List[54], List[53]
	if (List[55] < List[57]):
		List[55], List[57] = List[57], List[55]
	if (List[56] < List[58]):
		List[56], List[58] = List[58], List[56]
	if (List[55] < List[56]):
		List[55], List[56] = List[56], List[55]
	if (List[57] < List[58]):
		List[57], List[58] = List[58], List[57]
	if (List[59] < List[67]):
		List[59], List[67] = List[67], List[59]
	if (List[60] < List[68]):
		List[60], List[68] = List[68], List[60]
	if (List[61] < List[69]):
		List[61], List[69] = List[69], List[61]
	if (List[62] < List[70]):
		List[62], List[70] = List[70], List[62]
	if (List[63] < List[71]):
		List[63], List[71] = List[71], List[63]
	if (List[64] < List[72]):
		List[64], List[72] = List[72], List[64]
	if (List[65] < List[73]):
		List[65], List[73] = List[73], List[65]
	if (List[66] < List[74]):
		List[66], List[74] = List[74], List[66]
	if (List[59] < List[63]):
		List[59], List[63] = List[63], List[59]
	if (List[60] < List[64]):
		List[60], List[64] = List[64], List[60]
	if (List[61] < List[65]):
		List[61], List[65] = List[65], List[61]
	if (List[62] < List[66]):
		List[62], List[66] = List[66], List[62]
	if (List[59] < List[61]):
		List[59], List[61] = List[61], List[59]
	if (List[60] < List[62]):
		List[60], List[62] = List[62], List[60]
	if (List[59] < List[60]):
		List[59], List[60] = List[60], List[59]
	if (List[61] < List[62]):
		List[61], List[62] = List[62], List[61]
	if (List[63] < List[65]):
		List[63], List[65] = List[65], List[63]
	if (List[64] < List[66]):
		List[64], List[66] = List[66], List[64]
	if (List[63] < List[64]):
		List[63], List[64] = List[64], List[63]
	if (List[65] < List[66]):
		List[65], List[66] = List[66], List[65]
	if (List[67] < List[71]):
		List[67], List[71] = List[71], List[67]
	if (List[68] < List[72]):
		List[68], List[72] = List[72], List[68]
	if (List[69] < List[73]):
		List[69], List[73] = List[73], List[69]
	if (List[70] < List[74]):
		List[70], List[74] = List[74], List[70]
	if (List[67] < List[69]):
		List[67], List[69] = List[69], List[67]
	if (List[68] < List[70]):
		List[68], List[70] = List[70], List[68]
	if (List[67] < List[68]):
		List[67], List[68] = List[68], List[67]
	if (List[69] < List[70]):
		List[69], List[70] = List[70], List[69]
	if (List[71] < List[73]):
		List[71], List[73] = List[73], List[71]
	if (List[72] < List[74]):
		List[72], List[74] = List[74], List[72]
	if (List[71] < List[72]):
		List[71], List[72] = List[72], List[71]
	if (List[73] < List[74]):
		List[73], List[74] = List[74], List[73]
	if (List[76] < List[77]):
		List[76], List[77] = List[77], List[76]
	if (List[75] > List[77]):
		List[75], List[77] = List[77], List[75]
	if (List[76] > List[77]):
		List[76], List[77] = List[77], List[76]
	if (List[79] > List[80]):
		List[79], List[80] = List[80], List[79]
	if (List[78] < List[80]):
		List[78], List[80] = List[80], List[78]
	if (List[79] < List[80]):
		List[79], List[80] = List[80], List[79]
	if (List[75] > List[79]):
		List[75], List[79] = List[79], List[75]
	if (List[76] > List[80]):
		List[76], List[80] = List[80], List[76]
	if (List[75] > List[76]):
		List[75], List[76] = List[76], List[75]
	if (List[77] > List[79]):
		List[77], List[79] = List[79], List[77]
	if (List[78] > List[80]):
		List[78], List[80] = List[80], List[78]
	if (List[77] > List[78]):
		List[77], List[78] = List[78], List[77]
	if (List[79] > List[80]):
		List[79], List[80] = List[80], List[79]
	if (List[82] > List[83]):
		List[82], List[83] = List[83], List[82]
	if (List[81] < List[83]):
		List[81], List[83] = List[83], List[81]
	if (List[82] < List[83]):
		List[82], List[83] = List[83], List[82]
	if (List[84] > List[85]):
		List[84], List[85] = List[85], List[84]
	if (List[86] < List[87]):
		List[86], List[87] = List[87], List[86]
	if (List[84] > List[86]):
		List[84], List[86] = List[86], List[84]
	if (List[85] > List[87]):
		List[85], List[87] = List[87], List[85]
	if (List[84] > List[85]):
		List[84], List[85] = List[85], List[84]
	if (List[86] > List[87]):
		List[86], List[87] = List[87], List[86]
	if (List[81] < List[85]):
		List[81], List[85] = List[85], List[81]
	if (List[82] < List[86]):
		List[82], List[86] = List[86], List[82]
	if (List[83] < List[87]):
		List[83], List[87] = List[87], List[83]
	if (List[81] < List[83]):
		List[81], List[83] = List[83], List[81]
	if (List[82] < List[83]):
		List[82], List[83] = List[83], List[82]
	if (List[84] < List[86]):
		List[84], List[86] = List[86], List[84]
	if (List[85] < List[87]):
		List[85], List[87] = List[87], List[85]
	if (List[84] < List[85]):
		List[84], List[85] = List[85], List[84]
	if (List[86] < List[87]):
		List[86], List[87] = List[87], List[86]
	if (List[75] > List[83]):
		List[75], List[83] = List[83], List[75]
	if (List[76] > List[84]):
		List[76], List[84] = List[84], List[76]
	if (List[77] > List[85]):
		List[77], List[85] = List[85], List[77]
	if (List[78] > List[86]):
		List[78], List[86] = List[86], List[78]
	if (List[79] > List[87]):
		List[79], List[87] = List[87], List[79]
	if (List[75] > List[79]):
		List[75], List[79] = List[79], List[75]
	if (List[76] > List[78]):
		List[76], List[78] = List[78], List[76]
	if (List[77] > List[79]):
		List[77], List[79] = List[79], List[77]
	if (List[76] > List[77]):
		List[76], List[77] = List[77], List[76]
	if (List[78] > List[79]):
		List[78], List[79] = List[79], List[78]
	if (List[80] > List[84]):
		List[80], List[84] = List[84], List[80]
	if (List[81] > List[85]):
		List[81], List[85] = List[85], List[81]
	if (List[82] > List[86]):
		List[82], List[86] = List[86], List[82]
	if (List[83] > List[87]):
		List[83], List[87] = List[87], List[83]
	if (List[80] > List[82]):
		List[80], List[82] = List[82], List[80]
	if (List[81] > List[83]):
		List[81], List[83] = List[83], List[81]
	if (List[80] > List[81]):
		List[80], List[81] = List[81], List[80]
	if (List[82] > List[83]):
		List[82], List[83] = List[83], List[82]
	if (List[84] > List[86]):
		List[84], List[86] = List[86], List[84]
	if (List[85] > List[87]):
		List[85], List[87] = List[87], List[85]
	if (List[84] > List[85]):
		List[84], List[85] = List[85], List[84]
	if (List[86] > List[87]):
		List[86], List[87] = List[87], List[86]
	if (List[89] > List[90]):
		List[89], List[90] = List[90], List[89]
	if (List[88] < List[90]):
		List[88], List[90] = List[90], List[88]
	if (List[89] < List[90]):
		List[89], List[90] = List[90], List[89]
	if (List[92] < List[93]):
		List[92], List[93] = List[93], List[92]
	if (List[91] > List[93]):
		List[91], List[93] = List[93], List[91]
	if (List[92] > List[93]):
		List[92], List[93] = List[93], List[92]
	if (List[88] < List[92]):
		List[88], List[92] = List[92], List[88]
	if (List[89] < List[93]):
		List[89], List[93] = List[93], List[89]
	if (List[88] < List[89]):
		List[88], List[89] = List[89], List[88]
	if (List[90] < List[92]):
		List[90], List[92] = List[92], List[90]
	if (List[91] < List[93]):
		List[91], List[93] = List[93], List[91]
	if (List[90] < List[91]):
		List[90], List[91] = List[91], List[90]
	if (List[92] < List[93]):
		List[92], List[93] = List[93], List[92]
	if (List[95] < List[96]):
		List[95], List[96] = List[96], List[95]
	if (List[94] > List[96]):
		List[94], List[96] = List[96], List[94]
	if (List[95] > List[96]):
		List[95], List[96] = List[96], List[95]
	if (List[97] < List[98]):
		List[97], List[98] = List[98], List[97]
	if (List[99] > List[100]):
		List[99], List[100] = List[100], List[99]
	if (List[97] < List[99]):
		List[97], List[99] = List[99], List[97]
	if (List[98] < List[100]):
		List[98], List[100] = List[100], List[98]
	if (List[97] < List[98]):
		List[97], List[98] = List[98], List[97]
	if (List[99] < List[100]):
		List[99], List[100] = List[100], List[99]
	if (List[94] > List[98]):
		List[94], List[98] = List[98], List[94]
	if (List[95] > List[99]):
		List[95], List[99] = List[99], List[95]
	if (List[96] > List[100]):
		List[96], List[100] = List[100], List[96]
	if (List[94] > List[96]):
		List[94], List[96] = List[96], List[94]
	if (List[95] > List[96]):
		List[95], List[96] = List[96], List[95]
	if (List[97] > List[99]):
		List[97], List[99] = List[99], List[97]
	if (List[98] > List[100]):
		List[98], List[100] = List[100], List[98]
	if (List[97] > List[98]):
		List[97], List[98] = List[98], List[97]
	if (List[99] > List[100]):
		List[99], List[100] = List[100], List[99]
	if (List[88] < List[96]):
		List[88], List[96] = List[96], List[88]
	if (List[89] < List[97]):
		List[89], List[97] = List[97], List[89]
	if (List[90] < List[98]):
		List[90], List[98] = List[98], List[90]
	if (List[91] < List[99]):
		List[91], List[99] = List[99], List[91]
	if (List[92] < List[100]):
		List[92], List[100] = List[100], List[92]
	if (List[88] < List[92]):
		List[88], List[92] = List[92], List[88]
	if (List[89] < List[91]):
		List[89], List[91] = List[91], List[89]
	if (List[90] < List[92]):
		List[90], List[92] = List[92], List[90]
	if (List[89] < List[90]):
		List[89], List[90] = List[90], List[89]
	if (List[91] < List[92]):
		List[91], List[92] = List[92], List[91]
	if (List[93] < List[97]):
		List[93], List[97] = List[97], List[93]
	if (List[94] < List[98]):
		List[94], List[98] = List[98], List[94]
	if (List[95] < List[99]):
		List[95], List[99] = List[99], List[95]
	if (List[96] < List[100]):
		List[96], List[100] = List[100], List[96]
	if (List[93] < List[95]):
		List[93], List[95] = List[95], List[93]
	if (List[94] < List[96]):
		List[94], List[96] = List[96], List[94]
	if (List[93] < List[94]):
		List[93], List[94] = List[94], List[93]
	if (List[95] < List[96]):
		List[95], List[96] = List[96], List[95]
	if (List[97] < List[99]):
		List[97], List[99] = List[99], List[97]
	if (List[98] < List[100]):
		List[98], List[100] = List[100], List[98]
	if (List[97] < List[98]):
		List[97], List[98] = List[98], List[97]
	if (List[99] < List[100]):
		List[99], List[100] = List[100], List[99]
	if (List[75] > List[91]):
		List[75], List[91] = List[91], List[75]
	if (List[76] > List[92]):
		List[76], List[92] = List[92], List[76]
	if (List[77] > List[93]):
		List[77], List[93] = List[93], List[77]
	if (List[78] > List[94]):
		List[78], List[94] = List[94], List[78]
	if (List[79] > List[95]):
		List[79], List[95] = List[95], List[79]
	if (List[80] > List[96]):
		List[80], List[96] = List[96], List[80]
	if (List[81] > List[97]):
		List[81], List[97] = List[97], List[81]
	if (List[82] > List[98]):
		List[82], List[98] = List[98], List[82]
	if (List[83] > List[99]):
		List[83], List[99] = List[99], List[83]
	if (List[84] > List[100]):
		List[84], List[100] = List[100], List[84]
	if (List[75] > List[83]):
		List[75], List[83] = List[83], List[75]
	if (List[76] > List[84]):
		List[76], List[84] = List[84], List[76]
	if (List[75] > List[76]):
		List[75], List[76] = List[76], List[75]
	if (List[77] > List[81]):
		List[77], List[81] = List[81], List[77]
	if (List[78] > List[82]):
		List[78], List[82] = List[82], List[78]
	if (List[79] > List[83]):
		List[79], List[83] = List[83], List[79]
	if (List[80] > List[84]):
		List[80], List[84] = List[84], List[80]
	if (List[77] > List[79]):
		List[77], List[79] = List[79], List[77]
	if (List[78] > List[80]):
		List[78], List[80] = List[80], List[78]
	if (List[77] > List[78]):
		List[77], List[78] = List[78], List[77]
	if (List[79] > List[80]):
		List[79], List[80] = List[80], List[79]
	if (List[81] > List[83]):
		List[81], List[83] = List[83], List[81]
	if (List[82] > List[84]):
		List[82], List[84] = List[84], List[82]
	if (List[81] > List[82]):
		List[81], List[82] = List[82], List[81]
	if (List[83] > List[84]):
		List[83], List[84] = List[84], List[83]
	if (List[85] > List[93]):
		List[85], List[93] = List[93], List[85]
	if (List[86] > List[94]):
		List[86], List[94] = List[94], List[86]
	if (List[87] > List[95]):
		List[87], List[95] = List[95], List[87]
	if (List[88] > List[96]):
		List[88], List[96] = List[96], List[88]
	if (List[89] > List[97]):
		List[89], List[97] = List[97], List[89]
	if (List[90] > List[98]):
		List[90], List[98] = List[98], List[90]
	if (List[91] > List[99]):
		List[91], List[99] = List[99], List[91]
	if (List[92] > List[100]):
		List[92], List[100] = List[100], List[92]
	if (List[85] > List[89]):
		List[85], List[89] = List[89], List[85]
	if (List[86] > List[90]):
		List[86], List[90] = List[90], List[86]
	if (List[87] > List[91]):
		List[87], List[91] = List[91], List[87]
	if (List[88] > List[92]):
		List[88], List[92] = List[92], List[88]
	if (List[85] > List[87]):
		List[85], List[87] = List[87], List[85]
	if (List[86] > List[88]):
		List[86], List[88] = List[88], List[86]
	if (List[85] > List[86]):
		List[85], List[86] = List[86], List[85]
	if (List[87] > List[88]):
		List[87], List[88] = List[88], List[87]
	if (List[89] > List[91]):
		List[89], List[91] = List[91], List[89]
	if (List[90] > List[92]):
		List[90], List[92] = List[92], List[90]
	if (List[89] > List[90]):
		List[89], List[90] = List[90], List[89]
	if (List[91] > List[92]):
		List[91], List[92] = List[92], List[91]
	if (List[93] > List[97]):
		List[93], List[97] = List[97], List[93]
	if (List[94] > List[98]):
		List[94], List[98] = List[98], List[94]
	if (List[95] > List[99]):
		List[95], List[99] = List[99], List[95]
	if (List[96] > List[100]):
		List[96], List[100] = List[100], List[96]
	if (List[93] > List[95]):
		List[93], List[95] = List[95], List[93]
	if (List[94] > List[96]):
		List[94], List[96] = List[96], List[94]
	if (List[93] > List[94]):
		List[93], List[94] = List[94], List[93]
	if (List[95] > List[96]):
		List[95], List[96] = List[96], List[95]
	if (List[97] > List[99]):
		List[97], List[99] = List[99], List[97]
	if (List[98] > List[100]):
		List[98], List[100] = List[100], List[98]
	if (List[97] > List[98]):
		List[97], List[98] = List[98], List[97]
	if (List[99] > List[100]):
		List[99], List[100] = List[100], List[99]
	if (List[50] < List[82]):
		List[50], List[82] = List[82], List[50]
	if (List[51] < List[83]):
		List[51], List[83] = List[83], List[51]
	if (List[52] < List[84]):
		List[52], List[84] = List[84], List[52]
	if (List[53] < List[85]):
		List[53], List[85] = List[85], List[53]
	if (List[54] < List[86]):
		List[54], List[86] = List[86], List[54]
	if (List[55] < List[87]):
		List[55], List[87] = List[87], List[55]
	if (List[56] < List[88]):
		List[56], List[88] = List[88], List[56]
	if (List[57] < List[89]):
		List[57], List[89] = List[89], List[57]
	if (List[58] < List[90]):
		List[58], List[90] = List[90], List[58]
	if (List[59] < List[91]):
		List[59], List[91] = List[91], List[59]
	if (List[60] < List[92]):
		List[60], List[92] = List[92], List[60]
	if (List[61] < List[93]):
		List[61], List[93] = List[93], List[61]
	if (List[62] < List[94]):
		List[62], List[94] = List[94], List[62]
	if (List[63] < List[95]):
		List[63], List[95] = List[95], List[63]
	if (List[64] < List[96]):
		List[64], List[96] = List[96], List[64]
	if (List[65] < List[97]):
		List[65], List[97] = List[97], List[65]
	if (List[66] < List[98]):
		List[66], List[98] = List[98], List[66]
	if (List[67] < List[99]):
		List[67], List[99] = List[99], List[67]
	if (List[68] < List[100]):
		List[68], List[100] = List[100], List[68]
	if (List[50] < List[66]):
		List[50], List[66] = List[66], List[50]
	if (List[51] < List[67]):
		List[51], List[67] = List[67], List[51]
	if (List[52] < List[68]):
		List[52], List[68] = List[68], List[52]
	if (List[50] < List[52]):
		List[50], List[52] = List[52], List[50]
	if (List[51] < List[52]):
		List[51], List[52] = List[52], List[51]
	if (List[53] < List[61]):
		List[53], List[61] = List[61], List[53]
	if (List[54] < List[62]):
		List[54], List[62] = List[62], List[54]
	if (List[55] < List[63]):
		List[55], List[63] = List[63], List[55]
	if (List[56] < List[64]):
		List[56], List[64] = List[64], List[56]
	if (List[57] < List[65]):
		List[57], List[65] = List[65], List[57]
	if (List[58] < List[66]):
		List[58], List[66] = List[66], List[58]
	if (List[59] < List[67]):
		List[59], List[67] = List[67], List[59]
	if (List[60] < List[68]):
		List[60], List[68] = List[68], List[60]
	if (List[53] < List[57]):
		List[53], List[57] = List[57], List[53]
	if (List[54] < List[58]):
		List[54], List[58] = List[58], List[54]
	if (List[55] < List[59]):
		List[55], List[59] = List[59], List[55]
	if (List[56] < List[60]):
		List[56], List[60] = List[60], List[56]
	if (List[53] < List[55]):
		List[53], List[55] = List[55], List[53]
	if (List[54] < List[56]):
		List[54], List[56] = List[56], List[54]
	if (List[53] < List[54]):
		List[53], List[54] = List[54], List[53]
	if (List[55] < List[56]):
		List[55], List[56] = List[56], List[55]
	if (List[57] < List[59]):
		List[57], List[59] = List[59], List[57]
	if (List[58] < List[60]):
		List[58], List[60] = List[60], List[58]
	if (List[57] < List[58]):
		List[57], List[58] = List[58], List[57]
	if (List[59] < List[60]):
		List[59], List[60] = List[60], List[59]
	if (List[61] < List[65]):
		List[61], List[65] = List[65], List[61]
	if (List[62] < List[66]):
		List[62], List[66] = List[66], List[62]
	if (List[63] < List[67]):
		List[63], List[67] = List[67], List[63]
	if (List[64] < List[68]):
		List[64], List[68] = List[68], List[64]
	if (List[61] < List[63]):
		List[61], List[63] = List[63], List[61]
	if (List[62] < List[64]):
		List[62], List[64] = List[64], List[62]
	if (List[61] < List[62]):
		List[61], List[62] = List[62], List[61]
	if (List[63] < List[64]):
		List[63], List[64] = List[64], List[63]
	if (List[65] < List[67]):
		List[65], List[67] = List[67], List[65]
	if (List[66] < List[68]):
		List[66], List[68] = List[68], List[66]
	if (List[65] < List[66]):
		List[65], List[66] = List[66], List[65]
	if (List[67] < List[68]):
		List[67], List[68] = List[68], List[67]
	if (List[69] < List[85]):
		List[69], List[85] = List[85], List[69]
	if (List[70] < List[86]):
		List[70], List[86] = List[86], List[70]
	if (List[71] < List[87]):
		List[71], List[87] = List[87], List[71]
	if (List[72] < List[88]):
		List[72], List[88] = List[88], List[72]
	if (List[73] < List[89]):
		List[73], List[89] = List[89], List[73]
	if (List[74] < List[90]):
		List[74], List[90] = List[90], List[74]
	if (List[75] < List[91]):
		List[75], List[91] = List[91], List[75]
	if (List[76] < List[92]):
		List[76], List[92] = List[92], List[76]
	if (List[77] < List[93]):
		List[77], List[93] = List[93], List[77]
	if (List[78] < List[94]):
		List[78], List[94] = List[94], List[78]
	if (List[79] < List[95]):
		List[79], List[95] = List[95], List[79]
	if (List[80] < List[96]):
		List[80], List[96] = List[96], List[80]
	if (List[81] < List[97]):
		List[81], List[97] = List[97], List[81]
	if (List[82] < List[98]):
		List[82], List[98] = List[98], List[82]
	if (List[83] < List[99]):
		List[83], List[99] = List[99], List[83]
	if (List[84] < List[100]):
		List[84], List[100] = List[100], List[84]
	if (List[69] < List[77]):
		List[69], List[77] = List[77], List[69]
	if (List[70] < List[78]):
		List[70], List[78] = List[78], List[70]
	if (List[71] < List[79]):
		List[71], List[79] = List[79], List[71]
	if (List[72] < List[80]):
		List[72], List[80] = List[80], List[72]
	if (List[73] < List[81]):
		List[73], List[81] = List[81], List[73]
	if (List[74] < List[82]):
		List[74], List[82] = List[82], List[74]
	if (List[75] < List[83]):
		List[75], List[83] = List[83], List[75]
	if (List[76] < List[84]):
		List[76], List[84] = List[84], List[76]
	if (List[69] < List[73]):
		List[69], List[73] = List[73], List[69]
	if (List[70] < List[74]):
		List[70], List[74] = List[74], List[70]
	if (List[71] < List[75]):
		List[71], List[75] = List[75], List[71]
	if (List[72] < List[76]):
		List[72], List[76] = List[76], List[72]
	if (List[69] < List[71]):
		List[69], List[71] = List[71], List[69]
	if (List[70] < List[72]):
		List[70], List[72] = List[72], List[70]
	if (List[69] < List[70]):
		List[69], List[70] = List[70], List[69]
	if (List[71] < List[72]):
		List[71], List[72] = List[72], List[71]
	if (List[73] < List[75]):
		List[73], List[75] = List[75], List[73]
	if (List[74] < List[76]):
		List[74], List[76] = List[76], List[74]
	if (List[73] < List[74]):
		List[73], List[74] = List[74], List[73]
	if (List[75] < List[76]):
		List[75], List[76] = List[76], List[75]
	if (List[77] < List[81]):
		List[77], List[81] = List[81], List[77]
	if (List[78] < List[82]):
		List[78], List[82] = List[82], List[78]
	if (List[79] < List[83]):
		List[79], List[83] = List[83], List[79]
	if (List[80] < List[84]):
		List[80], List[84] = List[84], List[80]
	if (List[77] < List[79]):
		List[77], List[79] = List[79], List[77]
	if (List[78] < List[80]):
		List[78], List[80] = List[80], List[78]
	if (List[77] < List[78]):
		List[77], List[78] = List[78], List[77]
	if (List[79] < List[80]):
		List[79], List[80] = List[80], List[79]
	if (List[81] < List[83]):
		List[81], List[83] = List[83], List[81]
	if (List[82] < List[84]):
		List[82], List[84] = List[84], List[82]
	if (List[81] < List[82]):
		List[81], List[82] = List[82], List[81]
	if (List[83] < List[84]):
		List[83], List[84] = List[84], List[83]
	if (List[85] < List[93]):
		List[85], List[93] = List[93], List[85]
	if (List[86] < List[94]):
		List[86], List[94] = List[94], List[86]
	if (List[87] < List[95]):
		List[87], List[95] = List[95], List[87]
	if (List[88] < List[96]):
		List[88], List[96] = List[96], List[88]
	if (List[89] < List[97]):
		List[89], List[97] = List[97], List[89]
	if (List[90] < List[98]):
		List[90], List[98] = List[98], List[90]
	if (List[91] < List[99]):
		List[91], List[99] = List[99], List[91]
	if (List[92] < List[100]):
		List[92], List[100] = List[100], List[92]
	if (List[85] < List[89]):
		List[85], List[89] = List[89], List[85]
	if (List[86] < List[90]):
		List[86], List[90] = List[90], List[86]
	if (List[87] < List[91]):
		List[87], List[91] = List[91], List[87]
	if (List[88] < List[92]):
		List[88], List[92] = List[92], List[88]
	if (List[85] < List[87]):
		List[85], List[87] = List[87], List[85]
	if (List[86] < List[88]):
		List[86], List[88] = List[88], List[86]
	if (List[85] < List[86]):
		List[85], List[86] = List[86], List[85]
	if (List[87] < List[88]):
		List[87], List[88] = List[88], List[87]
	if (List[89] < List[91]):
		List[89], List[91] = List[91], List[89]
	if (List[90] < List[92]):
		List[90], List[92] = List[92], List[90]
	if (List[89] < List[90]):
		List[89], List[90] = List[90], List[89]
	if (List[91] < List[92]):
		List[91], List[92] = List[92], List[91]
	if (List[93] < List[97]):
		List[93], List[97] = List[97], List[93]
	if (List[94] < List[98]):
		List[94], List[98] = List[98], List[94]
	if (List[95] < List[99]):
		List[95], List[99] = List[99], List[95]
	if (List[96] < List[100]):
		List[96], List[100] = List[100], List[96]
	if (List[93] < List[95]):
		List[93], List[95] = List[95], List[93]
	if (List[94] < List[96]):
		List[94], List[96] = List[96], List[94]
	if (List[93] < List[94]):
		List[93], List[94] = List[94], List[93]
	if (List[95] < List[96]):
		List[95], List[96] = List[96], List[95]
	if (List[97] < List[99]):
		List[97], List[99] = List[99], List[97]
	if (List[98] < List[100]):
		List[98], List[100] = List[100], List[98]
	if (List[97] < List[98]):
		List[97], List[98] = List[98], List[97]
	if (List[99] < List[100]):
		List[99], List[100] = List[100], List[99]
	if (List[0] > List[64]):
		List[0], List[64] = List[64], List[0]
	if (List[1] > List[65]):
		List[1], List[65] = List[65], List[1]
	if (List[2] > List[66]):
		List[2], List[66] = List[66], List[2]
	if (List[3] > List[67]):
		List[3], List[67] = List[67], List[3]
	if (List[4] > List[68]):
		List[4], List[68] = List[68], List[4]
	if (List[5] > List[69]):
		List[5], List[69] = List[69], List[5]
	if (List[6] > List[70]):
		List[6], List[70] = List[70], List[6]
	if (List[7] > List[71]):
		List[7], List[71] = List[71], List[7]
	if (List[8] > List[72]):
		List[8], List[72] = List[72], List[8]
	if (List[9] > List[73]):
		List[9], List[73] = List[73], List[9]
	if (List[10] > List[74]):
		List[10], List[74] = List[74], List[10]
	if (List[11] > List[75]):
		List[11], List[75] = List[75], List[11]
	if (List[12] > List[76]):
		List[12], List[76] = List[76], List[12]
	if (List[13] > List[77]):
		List[13], List[77] = List[77], List[13]
	if (List[14] > List[78]):
		List[14], List[78] = List[78], List[14]
	if (List[15] > List[79]):
		List[15], List[79] = List[79], List[15]
	if (List[16] > List[80]):
		List[16], List[80] = List[80], List[16]
	if (List[17] > List[81]):
		List[17], List[81] = List[81], List[17]
	if (List[18] > List[82]):
		List[18], List[82] = List[82], List[18]
	if (List[19] > List[83]):
		List[19], List[83] = List[83], List[19]
	if (List[20] > List[84]):
		List[20], List[84] = List[84], List[20]
	if (List[21] > List[85]):
		List[21], List[85] = List[85], List[21]
	if (List[22] > List[86]):
		List[22], List[86] = List[86], List[22]
	if (List[23] > List[87]):
		List[23], List[87] = List[87], List[23]
	if (List[24] > List[88]):
		List[24], List[88] = List[88], List[24]
	if (List[25] > List[89]):
		List[25], List[89] = List[89], List[25]
	if (List[26] > List[90]):
		List[26], List[90] = List[90], List[26]
	if (List[27] > List[91]):
		List[27], List[91] = List[91], List[27]
	if (List[28] > List[92]):
		List[28], List[92] = List[92], List[28]
	if (List[29] > List[93]):
		List[29], List[93] = List[93], List[29]
	if (List[30] > List[94]):
		List[30], List[94] = List[94], List[30]
	if (List[31] > List[95]):
		List[31], List[95] = List[95], List[31]
	if (List[32] > List[96]):
		List[32], List[96] = List[96], List[32]
	if (List[33] > List[97]):
		List[33], List[97] = List[97], List[33]
	if (List[34] > List[98]):
		List[34], List[98] = List[98], List[34]
	if (List[35] > List[99]):
		List[35], List[99] = List[99], List[35]
	if (List[36] > List[100]):
		List[36], List[100] = List[100], List[36]
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
	if (List[0] > List[4]):
		List[0], List[4] = List[4], List[0]
	if (List[1] > List[3]):
		List[1], List[3] = List[3], List[1]
	if (List[2] > List[4]):
		List[2], List[4] = List[4], List[2]
	if (List[1] > List[2]):
		List[1], List[2] = List[2], List[1]
	if (List[3] > List[4]):
		List[3], List[4] = List[4], List[3]
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
	if (List[16] > List[32]):
		List[16], List[32] = List[32], List[16]
	if (List[17] > List[33]):
		List[17], List[33] = List[33], List[17]
	if (List[18] > List[34]):
		List[18], List[34] = List[34], List[18]
	if (List[19] > List[35]):
		List[19], List[35] = List[35], List[19]
	if (List[20] > List[36]):
		List[20], List[36] = List[36], List[20]
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
	if (List[10] > List[18]):
		List[10], List[18] = List[18], List[10]
	if (List[11] > List[19]):
		List[11], List[19] = List[19], List[11]
	if (List[12] > List[20]):
		List[12], List[20] = List[20], List[12]
	if (List[5] > List[9]):
		List[5], List[9] = List[9], List[5]
	if (List[6] > List[10]):
		List[6], List[10] = List[10], List[6]
	if (List[7] > List[11]):
		List[7], List[11] = List[11], List[7]
	if (List[8] > List[12]):
		List[8], List[12] = List[12], List[8]
	if (List[5] > List[7]):
		List[5], List[7] = List[7], List[5]
	if (List[6] > List[8]):
		List[6], List[8] = List[8], List[6]
	if (List[5] > List[6]):
		List[5], List[6] = List[6], List[5]
	if (List[7] > List[8]):
		List[7], List[8] = List[8], List[7]
	if (List[9] > List[11]):
		List[9], List[11] = List[11], List[9]
	if (List[10] > List[12]):
		List[10], List[12] = List[12], List[10]
	if (List[9] > List[10]):
		List[9], List[10] = List[10], List[9]
	if (List[11] > List[12]):
		List[11], List[12] = List[12], List[11]
	if (List[13] > List[17]):
		List[13], List[17] = List[17], List[13]
	if (List[14] > List[18]):
		List[14], List[18] = List[18], List[14]
	if (List[15] > List[19]):
		List[15], List[19] = List[19], List[15]
	if (List[16] > List[20]):
		List[16], List[20] = List[20], List[16]
	if (List[13] > List[15]):
		List[13], List[15] = List[15], List[13]
	if (List[14] > List[16]):
		List[14], List[16] = List[16], List[14]
	if (List[13] > List[14]):
		List[13], List[14] = List[14], List[13]
	if (List[15] > List[16]):
		List[15], List[16] = List[16], List[15]
	if (List[17] > List[19]):
		List[17], List[19] = List[19], List[17]
	if (List[18] > List[20]):
		List[18], List[20] = List[20], List[18]
	if (List[17] > List[18]):
		List[17], List[18] = List[18], List[17]
	if (List[19] > List[20]):
		List[19], List[20] = List[20], List[19]
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
	if (List[26] > List[34]):
		List[26], List[34] = List[34], List[26]
	if (List[27] > List[35]):
		List[27], List[35] = List[35], List[27]
	if (List[28] > List[36]):
		List[28], List[36] = List[36], List[28]
	if (List[21] > List[25]):
		List[21], List[25] = List[25], List[21]
	if (List[22] > List[26]):
		List[22], List[26] = List[26], List[22]
	if (List[23] > List[27]):
		List[23], List[27] = List[27], List[23]
	if (List[24] > List[28]):
		List[24], List[28] = List[28], List[24]
	if (List[21] > List[23]):
		List[21], List[23] = List[23], List[21]
	if (List[22] > List[24]):
		List[22], List[24] = List[24], List[22]
	if (List[21] > List[22]):
		List[21], List[22] = List[22], List[21]
	if (List[23] > List[24]):
		List[23], List[24] = List[24], List[23]
	if (List[25] > List[27]):
		List[25], List[27] = List[27], List[25]
	if (List[26] > List[28]):
		List[26], List[28] = List[28], List[26]
	if (List[25] > List[26]):
		List[25], List[26] = List[26], List[25]
	if (List[27] > List[28]):
		List[27], List[28] = List[28], List[27]
	if (List[29] > List[33]):
		List[29], List[33] = List[33], List[29]
	if (List[30] > List[34]):
		List[30], List[34] = List[34], List[30]
	if (List[31] > List[35]):
		List[31], List[35] = List[35], List[31]
	if (List[32] > List[36]):
		List[32], List[36] = List[36], List[32]
	if (List[29] > List[31]):
		List[29], List[31] = List[31], List[29]
	if (List[30] > List[32]):
		List[30], List[32] = List[32], List[30]
	if (List[29] > List[30]):
		List[29], List[30] = List[30], List[29]
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
	if (List[37] > List[69]):
		List[37], List[69] = List[69], List[37]
	if (List[38] > List[70]):
		List[38], List[70] = List[70], List[38]
	if (List[39] > List[71]):
		List[39], List[71] = List[71], List[39]
	if (List[40] > List[72]):
		List[40], List[72] = List[72], List[40]
	if (List[41] > List[73]):
		List[41], List[73] = List[73], List[41]
	if (List[42] > List[74]):
		List[42], List[74] = List[74], List[42]
	if (List[43] > List[75]):
		List[43], List[75] = List[75], List[43]
	if (List[44] > List[76]):
		List[44], List[76] = List[76], List[44]
	if (List[45] > List[77]):
		List[45], List[77] = List[77], List[45]
	if (List[46] > List[78]):
		List[46], List[78] = List[78], List[46]
	if (List[47] > List[79]):
		List[47], List[79] = List[79], List[47]
	if (List[48] > List[80]):
		List[48], List[80] = List[80], List[48]
	if (List[49] > List[81]):
		List[49], List[81] = List[81], List[49]
	if (List[50] > List[82]):
		List[50], List[82] = List[82], List[50]
	if (List[51] > List[83]):
		List[51], List[83] = List[83], List[51]
	if (List[52] > List[84]):
		List[52], List[84] = List[84], List[52]
	if (List[53] > List[85]):
		List[53], List[85] = List[85], List[53]
	if (List[54] > List[86]):
		List[54], List[86] = List[86], List[54]
	if (List[55] > List[87]):
		List[55], List[87] = List[87], List[55]
	if (List[56] > List[88]):
		List[56], List[88] = List[88], List[56]
	if (List[57] > List[89]):
		List[57], List[89] = List[89], List[57]
	if (List[58] > List[90]):
		List[58], List[90] = List[90], List[58]
	if (List[59] > List[91]):
		List[59], List[91] = List[91], List[59]
	if (List[60] > List[92]):
		List[60], List[92] = List[92], List[60]
	if (List[61] > List[93]):
		List[61], List[93] = List[93], List[61]
	if (List[62] > List[94]):
		List[62], List[94] = List[94], List[62]
	if (List[63] > List[95]):
		List[63], List[95] = List[95], List[63]
	if (List[64] > List[96]):
		List[64], List[96] = List[96], List[64]
	if (List[65] > List[97]):
		List[65], List[97] = List[97], List[65]
	if (List[66] > List[98]):
		List[66], List[98] = List[98], List[66]
	if (List[67] > List[99]):
		List[67], List[99] = List[99], List[67]
	if (List[68] > List[100]):
		List[68], List[100] = List[100], List[68]
	if (List[37] > List[53]):
		List[37], List[53] = List[53], List[37]
	if (List[38] > List[54]):
		List[38], List[54] = List[54], List[38]
	if (List[39] > List[55]):
		List[39], List[55] = List[55], List[39]
	if (List[40] > List[56]):
		List[40], List[56] = List[56], List[40]
	if (List[41] > List[57]):
		List[41], List[57] = List[57], List[41]
	if (List[42] > List[58]):
		List[42], List[58] = List[58], List[42]
	if (List[43] > List[59]):
		List[43], List[59] = List[59], List[43]
	if (List[44] > List[60]):
		List[44], List[60] = List[60], List[44]
	if (List[45] > List[61]):
		List[45], List[61] = List[61], List[45]
	if (List[46] > List[62]):
		List[46], List[62] = List[62], List[46]
	if (List[47] > List[63]):
		List[47], List[63] = List[63], List[47]
	if (List[48] > List[64]):
		List[48], List[64] = List[64], List[48]
	if (List[49] > List[65]):
		List[49], List[65] = List[65], List[49]
	if (List[50] > List[66]):
		List[50], List[66] = List[66], List[50]
	if (List[51] > List[67]):
		List[51], List[67] = List[67], List[51]
	if (List[52] > List[68]):
		List[52], List[68] = List[68], List[52]
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
	if (List[42] > List[50]):
		List[42], List[50] = List[50], List[42]
	if (List[43] > List[51]):
		List[43], List[51] = List[51], List[43]
	if (List[44] > List[52]):
		List[44], List[52] = List[52], List[44]
	if (List[37] > List[41]):
		List[37], List[41] = List[41], List[37]
	if (List[38] > List[42]):
		List[38], List[42] = List[42], List[38]
	if (List[39] > List[43]):
		List[39], List[43] = List[43], List[39]
	if (List[40] > List[44]):
		List[40], List[44] = List[44], List[40]
	if (List[37] > List[39]):
		List[37], List[39] = List[39], List[37]
	if (List[38] > List[40]):
		List[38], List[40] = List[40], List[38]
	if (List[37] > List[38]):
		List[37], List[38] = List[38], List[37]
	if (List[39] > List[40]):
		List[39], List[40] = List[40], List[39]
	if (List[41] > List[43]):
		List[41], List[43] = List[43], List[41]
	if (List[42] > List[44]):
		List[42], List[44] = List[44], List[42]
	if (List[41] > List[42]):
		List[41], List[42] = List[42], List[41]
	if (List[43] > List[44]):
		List[43], List[44] = List[44], List[43]
	if (List[45] > List[49]):
		List[45], List[49] = List[49], List[45]
	if (List[46] > List[50]):
		List[46], List[50] = List[50], List[46]
	if (List[47] > List[51]):
		List[47], List[51] = List[51], List[47]
	if (List[48] > List[52]):
		List[48], List[52] = List[52], List[48]
	if (List[45] > List[47]):
		List[45], List[47] = List[47], List[45]
	if (List[46] > List[48]):
		List[46], List[48] = List[48], List[46]
	if (List[45] > List[46]):
		List[45], List[46] = List[46], List[45]
	if (List[47] > List[48]):
		List[47], List[48] = List[48], List[47]
	if (List[49] > List[51]):
		List[49], List[51] = List[51], List[49]
	if (List[50] > List[52]):
		List[50], List[52] = List[52], List[50]
	if (List[49] > List[50]):
		List[49], List[50] = List[50], List[49]
	if (List[51] > List[52]):
		List[51], List[52] = List[52], List[51]
	if (List[53] > List[61]):
		List[53], List[61] = List[61], List[53]
	if (List[54] > List[62]):
		List[54], List[62] = List[62], List[54]
	if (List[55] > List[63]):
		List[55], List[63] = List[63], List[55]
	if (List[56] > List[64]):
		List[56], List[64] = List[64], List[56]
	if (List[57] > List[65]):
		List[57], List[65] = List[65], List[57]
	if (List[58] > List[66]):
		List[58], List[66] = List[66], List[58]
	if (List[59] > List[67]):
		List[59], List[67] = List[67], List[59]
	if (List[60] > List[68]):
		List[60], List[68] = List[68], List[60]
	if (List[53] > List[57]):
		List[53], List[57] = List[57], List[53]
	if (List[54] > List[58]):
		List[54], List[58] = List[58], List[54]
	if (List[55] > List[59]):
		List[55], List[59] = List[59], List[55]
	if (List[56] > List[60]):
		List[56], List[60] = List[60], List[56]
	if (List[53] > List[55]):
		List[53], List[55] = List[55], List[53]
	if (List[54] > List[56]):
		List[54], List[56] = List[56], List[54]
	if (List[53] > List[54]):
		List[53], List[54] = List[54], List[53]
	if (List[55] > List[56]):
		List[55], List[56] = List[56], List[55]
	if (List[57] > List[59]):
		List[57], List[59] = List[59], List[57]
	if (List[58] > List[60]):
		List[58], List[60] = List[60], List[58]
	if (List[57] > List[58]):
		List[57], List[58] = List[58], List[57]
	if (List[59] > List[60]):
		List[59], List[60] = List[60], List[59]
	if (List[61] > List[65]):
		List[61], List[65] = List[65], List[61]
	if (List[62] > List[66]):
		List[62], List[66] = List[66], List[62]
	if (List[63] > List[67]):
		List[63], List[67] = List[67], List[63]
	if (List[64] > List[68]):
		List[64], List[68] = List[68], List[64]
	if (List[61] > List[63]):
		List[61], List[63] = List[63], List[61]
	if (List[62] > List[64]):
		List[62], List[64] = List[64], List[62]
	if (List[61] > List[62]):
		List[61], List[62] = List[62], List[61]
	if (List[63] > List[64]):
		List[63], List[64] = List[64], List[63]
	if (List[65] > List[67]):
		List[65], List[67] = List[67], List[65]
	if (List[66] > List[68]):
		List[66], List[68] = List[68], List[66]
	if (List[65] > List[66]):
		List[65], List[66] = List[66], List[65]
	if (List[67] > List[68]):
		List[67], List[68] = List[68], List[67]
	if (List[69] > List[85]):
		List[69], List[85] = List[85], List[69]
	if (List[70] > List[86]):
		List[70], List[86] = List[86], List[70]
	if (List[71] > List[87]):
		List[71], List[87] = List[87], List[71]
	if (List[72] > List[88]):
		List[72], List[88] = List[88], List[72]
	if (List[73] > List[89]):
		List[73], List[89] = List[89], List[73]
	if (List[74] > List[90]):
		List[74], List[90] = List[90], List[74]
	if (List[75] > List[91]):
		List[75], List[91] = List[91], List[75]
	if (List[76] > List[92]):
		List[76], List[92] = List[92], List[76]
	if (List[77] > List[93]):
		List[77], List[93] = List[93], List[77]
	if (List[78] > List[94]):
		List[78], List[94] = List[94], List[78]
	if (List[79] > List[95]):
		List[79], List[95] = List[95], List[79]
	if (List[80] > List[96]):
		List[80], List[96] = List[96], List[80]
	if (List[81] > List[97]):
		List[81], List[97] = List[97], List[81]
	if (List[82] > List[98]):
		List[82], List[98] = List[98], List[82]
	if (List[83] > List[99]):
		List[83], List[99] = List[99], List[83]
	if (List[84] > List[100]):
		List[84], List[100] = List[100], List[84]
	if (List[69] > List[77]):
		List[69], List[77] = List[77], List[69]
	if (List[70] > List[78]):
		List[70], List[78] = List[78], List[70]
	if (List[71] > List[79]):
		List[71], List[79] = List[79], List[71]
	if (List[72] > List[80]):
		List[72], List[80] = List[80], List[72]
	if (List[73] > List[81]):
		List[73], List[81] = List[81], List[73]
	if (List[74] > List[82]):
		List[74], List[82] = List[82], List[74]
	if (List[75] > List[83]):
		List[75], List[83] = List[83], List[75]
	if (List[76] > List[84]):
		List[76], List[84] = List[84], List[76]
	if (List[69] > List[73]):
		List[69], List[73] = List[73], List[69]
	if (List[70] > List[74]):
		List[70], List[74] = List[74], List[70]
	if (List[71] > List[75]):
		List[71], List[75] = List[75], List[71]
	if (List[72] > List[76]):
		List[72], List[76] = List[76], List[72]
	if (List[69] > List[71]):
		List[69], List[71] = List[71], List[69]
	if (List[70] > List[72]):
		List[70], List[72] = List[72], List[70]
	if (List[69] > List[70]):
		List[69], List[70] = List[70], List[69]
	if (List[71] > List[72]):
		List[71], List[72] = List[72], List[71]
	if (List[73] > List[75]):
		List[73], List[75] = List[75], List[73]
	if (List[74] > List[76]):
		List[74], List[76] = List[76], List[74]
	if (List[73] > List[74]):
		List[73], List[74] = List[74], List[73]
	if (List[75] > List[76]):
		List[75], List[76] = List[76], List[75]
	if (List[77] > List[81]):
		List[77], List[81] = List[81], List[77]
	if (List[78] > List[82]):
		List[78], List[82] = List[82], List[78]
	if (List[79] > List[83]):
		List[79], List[83] = List[83], List[79]
	if (List[80] > List[84]):
		List[80], List[84] = List[84], List[80]
	if (List[77] > List[79]):
		List[77], List[79] = List[79], List[77]
	if (List[78] > List[80]):
		List[78], List[80] = List[80], List[78]
	if (List[77] > List[78]):
		List[77], List[78] = List[78], List[77]
	if (List[79] > List[80]):
		List[79], List[80] = List[80], List[79]
	if (List[81] > List[83]):
		List[81], List[83] = List[83], List[81]
	if (List[82] > List[84]):
		List[82], List[84] = List[84], List[82]
	if (List[81] > List[82]):
		List[81], List[82] = List[82], List[81]
	if (List[83] > List[84]):
		List[83], List[84] = List[84], List[83]
	if (List[85] > List[93]):
		List[85], List[93] = List[93], List[85]
	if (List[86] > List[94]):
		List[86], List[94] = List[94], List[86]
	if (List[87] > List[95]):
		List[87], List[95] = List[95], List[87]
	if (List[88] > List[96]):
		List[88], List[96] = List[96], List[88]
	if (List[89] > List[97]):
		List[89], List[97] = List[97], List[89]
	if (List[90] > List[98]):
		List[90], List[98] = List[98], List[90]
	if (List[91] > List[99]):
		List[91], List[99] = List[99], List[91]
	if (List[92] > List[100]):
		List[92], List[100] = List[100], List[92]
	if (List[85] > List[89]):
		List[85], List[89] = List[89], List[85]
	if (List[86] > List[90]):
		List[86], List[90] = List[90], List[86]
	if (List[87] > List[91]):
		List[87], List[91] = List[91], List[87]
	if (List[88] > List[92]):
		List[88], List[92] = List[92], List[88]
	if (List[85] > List[87]):
		List[85], List[87] = List[87], List[85]
	if (List[86] > List[88]):
		List[86], List[88] = List[88], List[86]
	if (List[85] > List[86]):
		List[85], List[86] = List[86], List[85]
	if (List[87] > List[88]):
		List[87], List[88] = List[88], List[87]
	if (List[89] > List[91]):
		List[89], List[91] = List[91], List[89]
	if (List[90] > List[92]):
		List[90], List[92] = List[92], List[90]
	if (List[89] > List[90]):
		List[89], List[90] = List[90], List[89]
	if (List[91] > List[92]):
		List[91], List[92] = List[92], List[91]
	if (List[93] > List[97]):
		List[93], List[97] = List[97], List[93]
	if (List[94] > List[98]):
		List[94], List[98] = List[98], List[94]
	if (List[95] > List[99]):
		List[95], List[99] = List[99], List[95]
	if (List[96] > List[100]):
		List[96], List[100] = List[100], List[96]
	if (List[93] > List[95]):
		List[93], List[95] = List[95], List[93]
	if (List[94] > List[96]):
		List[94], List[96] = List[96], List[94]
	if (List[93] > List[94]):
		List[93], List[94] = List[94], List[93]
	if (List[95] > List[96]):
		List[95], List[96] = List[96], List[95]
	if (List[97] > List[99]):
		List[97], List[99] = List[99], List[97]
	if (List[98] > List[100]):
		List[98], List[100] = List[100], List[98]
	if (List[97] > List[98]):
		List[97], List[98] = List[98], List[97]
	if (List[99] > List[100]):
		List[99], List[100] = List[100], List[99]
	return List
