
import pandas as pd
import io
import matplotlib.pyplot as plt

"""
dataframepre = pd.read_csv("newest_training_sets/6w_pb_fiesta_3000_pop_v3/pre_program_logs.csv", sep='|', index_col=False)
dataframepost = pd.read_csv("newest_training_sets/6w_pb_fiesta_3000_pop_v3/program_logs.csv", sep='|', index_col=False)


dataframepre = dataframepre.sort_values(by='Timestamp')
dataframepost = dataframepost.sort_values(by='Timestamp')

dataframepre = dataframepre.sort_values(by='ID')
dataframepost = dataframepost.sort_values(by='ID')

#print(dataframepre)
#print(dataframepost)

dataframepre = dataframepre.iloc[0:48, :]
dataframepost = dataframepost.iloc[0:48, :]


dataframepre = dataframepre.sort_values(by='Timestamp')
dataframepost = dataframepost.sort_values(by='Timestamp')

print(dataframepre)
print(dataframepost)

headers = ["ID", "Exercise", "Weight", "Reps", "Timestamp", "Performance"]
dataframe = pd.DataFrame(columns=headers)

dataframe = dataframe.append(dataframepre)
# dataframe = dataframe.append(dataframepost)


import matplotlib.ticker as ticker


dataframe.set_index('Timestamp', inplace=True)
ax = dataframe[["Exercise", "Weight", "Reps", "Performance"]].plot()

ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
plt.show()
"""

#pre
"""
dataframepre = pd.read_csv("newest_training_sets/6w_pb_fiesta_3000_pop_v3/pre_program_logs.csv", sep='|', index_col=False)

dataframepre = dataframepre.sort_values(by='Timestamp')

dataframepre = dataframepre.sort_values(by='ID')

dataframepre = dataframepre.iloc[0:222, :]

dataframepre = dataframepre.sort_values(by='Timestamp')

print(dataframepre)

headers = ["ID", "Exercise", "Weight", "Reps", "Timestamp", "Performance"]
dataframe = pd.DataFrame(columns=headers)

dataframe = dataframe.append(dataframepre)

import matplotlib.ticker as ticker

dataframe.set_index('Timestamp', inplace=True)
ax = dataframe[["Exercise", "Weight", "Reps", "Performance"]].plot()

ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))


plt.show()
"""




# Post

dataframepost = pd.read_csv("newest_training_sets/6w_pb_fiesta_3000_pop_v3/pre_program_logs.csv", sep='|', index_col=False)

dataframepost = dataframepost.sort_values(by='Timestamp')

dataframepost = dataframepost.sort_values(by='ID')

dataframepost = dataframepost.iloc[0:48, :]

dataframepost = dataframepost.sort_values(by='Timestamp')

print(dataframepost)

headers = ["ID", "Exercise", "Weight", "Reps", "Timestamp", "Performance"]
dataframe = pd.DataFrame(columns=headers)

dataframe = dataframe.append(dataframepost)

import matplotlib.ticker as ticker

dataframe.set_index('Timestamp', inplace=True)
ax = dataframe[["Exercise", "Weight", "Reps", "Performance"]].plot()

ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))



plt.show()
