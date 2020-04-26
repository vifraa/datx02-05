
import pandas as pd
import io
import matplotlib.pyplot as plt

dataframepre = pd.read_csv("output/pre_program_logs.csv", sep='|', index_col=False)
dataframepost = pd.read_csv("output/program_logs.csv", sep='|', index_col=False)


dataframepre = dataframepre.sort_values(by='Timestamp')
dataframepost = dataframepost.sort_values(by='Timestamp')

dataframepre = dataframepre.sort_values(by='ID')
dataframepost = dataframepost.sort_values(by='ID')

#print(dataframepre)
#print(dataframepost)

dataframepre = dataframepre.iloc[0:222, :]
dataframepost = dataframepost.iloc[0:222, :]


dataframepre = dataframepre.sort_values(by='Timestamp')
dataframepost = dataframepost.sort_values(by='Timestamp')

print(dataframepre)
print(dataframepost)

headers = ["ID", "Exercise", "Weight", "Reps", "Timestamp", "Performance"]
dataframe = pd.DataFrame(columns=headers)

# dataframe = dataframe.append(dataframepre)
dataframe = dataframe.append(dataframepost)


import matplotlib.ticker as ticker


dataframe.set_index('Timestamp', inplace=True)
ax = dataframe[["Exercise", "Weight", "Reps", "Performance"]].plot()

ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
plt.show()


#print(dataframe)
#dataframe.plot()
bytes_image = io.BytesIO()
plt.savefig(bytes_image, format='png')
bytes_image.seek(0)
plt.show()
