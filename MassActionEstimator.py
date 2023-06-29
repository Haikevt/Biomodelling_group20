import numpy as np

KMvalues = {
	"GLUT1 (glucose)": 	5,
	"GLUT4 (glucose)": 	5,
	"HK1 (D-glucose)": 		0.101,
	"GPI (G6P)": 		0.445,
	"GPI (F6P)": 0.062,
	"PFK[LPM] (F6P)": 	0.289,
	"ALDOA (FDP)": 	0.052, 
	"ALDOC (FDP)": 	0.013,
	"TPI (G3P)": 		0.525,
	"TPI (DHAP)": 		0.705,
	"GAPDH (G3P)":	0.111,
	"PGK1 (1,3 BP)":		0.004,
	"PGK1 (3PG)":		0.220,
	"PGK2 (1,3 BP)":		0.004,
	"PGK2 (3PG)":		0.160,
	"PGAM1 (3PG)": 	0.22,
	"PGAM2 (3PG)": 	0.22,
	"ENO[123] (2PG)": 	0.252,
	"PKM (PEP)":		0.334,
	"MPC[1,2] (Py)": 0.238,
	"LDHA (Pyr)":		0.114,
	"LDHB (Pyr)":		0.114,
	"MCT1 (Lactate)":		3.5,
	"MCT2 (Lactate)":		0.5
}

def normalize_list(lst):
	arr = np.array(lst)
	normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
	normalized_lst = normalized_arr.tolist()
	return normalized_lst

arr = np.array(list(KMvalues.values()))



#******************* normal normalization **************************************
#normalized_list = normalize_list(arr)
#****************** logarithmic normalization **********************************
log_data = np.log(arr)
normalized_list = (log_data - np.min(log_data)) / (np.max(log_data) - np.min(log_data))
#*******************************************************************************

print(arr)
print(normalized_list)

# Inverting
for i in range(len(normalized_list)):
	normalized_list[i] = 1.0-normalized_list[i]

# Printing
print(np.round(normalized_list,decimals=2))


MassActionEstimator = {}
for idx, km in enumerate(KMvalues):
	MassActionEstimator[km] = normalized_list[idx]

print("\nMassAction Estimations:")
for MAE in MassActionEstimator:
	print(f"{MAE.ljust(8)}\t{round(MassActionEstimator[MAE],1)}")






