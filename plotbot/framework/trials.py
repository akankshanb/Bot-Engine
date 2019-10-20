import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")
sns.stripplot(x="x-axis", y="petal_length", data=iris)
plt.savefig('foo.png')
