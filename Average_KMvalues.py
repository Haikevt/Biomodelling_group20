import pandas as pd
import numpy as np

#*******************************************************************************
def PRINT_RESUTLS(df, enz, subs):
	print(f"\n______\033[32m{enz}\033[0m________\033[32m{subs}\033[0m_____________")
	print("Mean:", round(df["Km-value"].mean(), 3) )
	print("Standard deviation:", round(df["Km-value"].std(), 3) )
	print(f"\n")
#*******************************************************************************
def check_temperature(df):
	temp = []
	hold = df
	for index, row in df.iterrows():
		if '°C' in row['COMMENTARY']:
			idx = row['COMMENTARY'].index('°C')
			try: temperature = int(row['COMMENTARY'][idx-2:idx])
			except: temperature = int(row['COMMENTARY'][idx-3:idx-1])
			if temperature >= 35 and temperature <= 38: # check if temperature is between 35 and 38 degrees
				temp.append(index)
		else: temp.append(index)
	df = df.loc[temp] 
	
	if len(df) == 0:
		input("\033[31m\nWARNING! there are no Km-values of the right temperature. Now returning the original dataframe. Oke?\033[0m")
		return hold
	return df
#*******************************************************************************
def check_PH(df):
	temp = []
	hold = df
	for index, row in df.iterrows():
		if any(s in row['COMMENTARY'] for s in ['ph ', 'PH ', 'pH ']):
			idx = row['COMMENTARY'].lower().index('ph ')
			try: ph = float(row['COMMENTARY'][idx+3:idx+6])
			except: pass #temp.append(index)
			if ph >= 7 and ph <= 8.5: # check if temperature is between 35 and 38 degrees
				temp.append(index)
		else: temp.append(index)
	df = df.loc[temp] 
	
	if len(df) == 0:
		input("\033[31m\nWARNING! there are no Km-values of the right pH. Now returning the original dataframe. Oke?\033[0m")
		return hold
	return df
#*******************************************************************************
def read_and_select(EnzymeAcronym, Substrate):
	df = pd.read_csv(EnzymeAcronym+".txt", sep="\t", header=None, names=["Km-value", "SUBSTRATE", "ORGANISM", "UNIPROT", "COMMENTARY", "LITERATURE", "IMAGE"])
	df = df[df["SUBSTRATE"] == Substrate] # Select on only rows that have the correct substrate
	#print(df)
	df = check_temperature(df) # select on not another temperature than 37
	df = check_PH(df)
	df['Km-value'] = pd.to_numeric(df['Km-value'], errors='coerce') # Cast to umerical values
	df = df[~df['COMMENTARY'].str.contains('activator|Activator')] # Remove the word 'activator'
	df = df[~df['COMMENTARY'].str.contains('mutant|Mutant')] # Remove the word 'mutant'
	df = df.dropna(subset=['Km-value']) # Remove rows with NaN values in 'Commentary' column
	return df
#*******************************************************************************
#*******************************************************************************
#*******************************************************************************

enzyme, substrate = "HK1", "D-glucose"
#enzyme, substrate = "GPI", "glucose 6-phosphate"
#enzyme, substrate = "GPI", "fructose 6-phosphate"
#enzyme, substrate = "PFK[LPM]", "D-fructose 6-phosphate"
#enzyme, substrate = "ALDOA", "D-fructose 1,6-bisphosphate" # FDP
#enzyme, substrate = "ALDOC", "D-fructose 1,6-bisphosphate" # FDP
#enzyme, substrate = "TPI", "D-glyceraldehyde 3-phosphate"
#enzyme, substrate = "TPI", "glycerone phosphate" # DHAP (Dihydroxyacetone phosphate/glycerone phosphate
#enzyme, substrate = "GAPDH", "D-glyceraldehyde 3-phosphate" # 
#enzyme, substrate = "PGK[12]", "3-phospho-D-glyceroyl phosphate"
#enzyme, substrate = "PGK[12]", "3-phospho-D-glycerate"
#enzyme, substrate = 	"PGAM[12]", " "
#enzyme, substrate = "ENO[123]", "2-phospho-D-glycerate"
#enzyme, substrate = "PKM", "phosphoenolpyruvate"
#enzyme, substrate = "LDH[AB]", "pyruvate"
#enzyme, substrate = "LDH[AB]", "(S)-lactate"

df = read_and_select(enzyme, substrate) 

print(df)
#print("*****************************************************************")
#for index, row in df.iterrows():
#	input(row['COMMENTARY'])
#print("*****************************************************************")

PRINT_RESUTLS(df, enzyme, substrate)




