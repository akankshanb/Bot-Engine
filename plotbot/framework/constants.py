import os
import matplotlib
import logging

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger("PlotBot-logger")

plotIDs = []
userIDs = {}
metadata = {}
greetinglist = ['hi', 'hey', 'hello']
mockPlots = []
baseStorage='storage/'
dbFile='metadata.db'
cwd = os.getcwd()
color_pallet = list(matplotlib.colors.CSS4_COLORS.keys())