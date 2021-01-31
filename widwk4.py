import pandas as pd
df = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(df)

import pandas as pd
destination = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(destination.iloc[2:8])

import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(data["inclusive"].mean())

import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\destination.csv")

import numpy as np
import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(df.nsmallest(1, ["feedback"]))

import numpy as np
import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(df.nlargest(1, ["feedback"]))

import numpy as np
import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(df[df.inclusive > 9])


import numpy as np
import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(df[df.feedback >8])


import numpy as np
import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(df[df.feedback <2])

import numpy as np
import pandas as pd
import sklearn 
from pandas.plotting import scatter_matrix

data = pd.read_csv(r"C:\Users\user\Documents\destination.csv")
print(df.plot.scatter(x="feedback", y="inclusive"))












 











                   








