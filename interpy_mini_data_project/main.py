import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("spotify_history.csv")
df_cleaned = df.dropna()

'''fig, ax = plt.subplots()
ax.set(xlabel='Reason Start', ylabel='Milliseconds Played', title='MS Played vs. Reason Start')
ax.grid()

reasonStart = list(set(df_cleaned['reason_start']))
msPlayed1 = []
for reason in reasonStart:
    numMS = (df_cleaned[df_cleaned['reason_start'] == reason]['ms_played']).mean()
    msPlayed1 += [numMS]
ax.bar(reasonStart, msPlayed1)'''

fig, ax = plt.subplots()
ax.set(xlabel='Reason End', ylabel='Milliseconds Played', title='MS Played vs. Reason End')
ax.grid()

reasonEnd = list(set(df_cleaned['reason_end']))
reasonEnd.remove('unexpected-exit-while-paused')
reasonEnd.remove('unexpected-exit')
remove = []
msPlayed2 = []
for reason in reasonEnd:
    numMS = (df_cleaned[df_cleaned['reason_end'] == reason]['ms_played']).mean()
    if numMS == 0:
        remove += [reason]
    else:
        msPlayed2 += [numMS]
for reason in remove:
    reasonEnd.remove(reason)

ax.bar(reasonEnd, msPlayed2)

plt.show()

