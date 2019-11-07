import os
import matplotlib
plotIDs = []
userIDs = {}
metadata = {}
greetinglist = ['hi', 'hey', 'hello']
mockPlots = []
baseStorage='storage/'
dbFile='metadata.db'
cwd = os.getcwd()
color_pallet = list(matplotlib.colors.CSS4_COLORS.keys())