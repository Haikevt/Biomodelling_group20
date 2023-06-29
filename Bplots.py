import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)




#*******************************************************************************
def plot_csv_data(csv_name, maxheight=False):
	data = pd.read_csv(csv_name)
	time = data.iloc[:, 0]
	data_columns = data.iloc[:, 1:]
	colors = plt.cm.tab20(np.linspace(0, 1, 12))
	#colors = plt.cm.get_cmap('rainbow_r', 12)
	fig, ax = plt.subplots()
	
	if maxheight: ax.set_ylim(0, maxheight)  # Adjust the upper limit (100) as desired

	for i, column in enumerate(data_columns):
		ax.plot(time, data_columns[column], color=colors[i], label=column)

	# Add legend, labels, and title
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	ax.set_xlabel('Time')
	ax.set_ylabel('Concentration')
	ax.set_title('Metabolites')
	
	plt.tight_layout()  # Ensure all elements fit in the plot
	
	# Show the plot
	#plt.show()

	# Save the plot with the specified name
	new_csv_name = csv_name.split('_')[3]+"_["+re.findall(r'\[(.*?)\]', csv_name)[0] + "]"   # Regular expression pattern to match text between [ and ]
	new_csv_name = new_csv_name.replace(", ", "_")
	fig.savefig(f'{new_csv_name}.png')
#*******************************************************************************

def get_highest_value(filename):
	data = pd.read_csv(filename) # Read the CSV file
	data = data.iloc[:, 1:] # Exclude the first column (time)
	highest_value = data.values.max() # Find the highest value
	return highest_value

#*******************************************************************************

csv_files = [
	#"New_Model_Group20_Metabolites_[0%, MA=1, 50.000runs, ConstInput=False, End=70].csv",
	#"New_Model_Group20_Metabolites_[0%, MA=MinMax, 50.000runs, ConstInput=False, End=70].csv",
	#"New_Model_Group20_Metabolites_[0%, MA=Log, 50.000runs, ConstInput=False, End=70].csv",

	#"New_Model_Group20_Metabolites_[0%, MA=Log, 50.000runs, ConstInput=False, End=70].csv",
	#"New_Model_Group20_Metabolites_[50%, MA=Log, 50.000runs, ConstInput=False, End=70].csv",
	#"New_Model_Group20_Metabolites_[70%, MA=Log, 50.000runs, ConstInput=False, End=70].csv",
	#"New_Model_Group20_Metabolites_[90%, MA=Log, 50.000runs, ConstInput=False, End=70].csv",

	#"New_Model_Group20_Metabolites_[0%, MA=Log, 50.000runs, ConstInput=False, End=70].csv",
	#"New_Model_Group20_Metabolites_[0%, MA=Log, 50.000runs, ConstInput=True, End=70].csv",
	#"New_Model_Group20_Metabolites_[50%, MA=Log, 50.000runs, ConstInput=True, End=70].csv",
	
	"New_Model_Group20_Metabolites_[0%, MA=Log, 50.000runs, ConstInput=False, End=70].csv",
	#"New_Model_Group20_Metabolites_[0%, MA=Log, 50.000runs, ConstInput=False, End=70, DHAPout=False].csv"
	"New_Model_Group20_Metabolites_[0%,MA=Log, 50000runs, ConstInput=False, End=70, DHAP_out=1].csv",
	"New_Model_Group20_Metabolites_[0%, MA=Log, 50000runs, ConstInput=False, End=70, DHAP_out=20].csv",
]

highest = 0
for csv in csv_files:
	high = get_highest_value(csv)
	if high > highest: highest = high
	print("The highest value in the CSV is:", highest)



for csv in csv_files:
	plot_csv_data(csv, maxheight=highest)







