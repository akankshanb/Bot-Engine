import mixin

mocking = True
if mocking:
    import plotter_mock as plotter
    import snippetter_mock as snippetter
else:
    import plotter as plotter
    import snippetter as snippetter


dataset = None
plotIDs = []
userIDs = []
greeting_list = ['hi', 'hey', 'hello']
graph_dict={
            "scatterplot": 
            {
                "snippet" : ('scatter', 'snippet'), 
                "plot": ('scatter', 'plot')
            }, 
            "barplot": 
            {
                "snippet" : ('bar', 'snippet'), 
                "plot": ('bar', 'plot')
            },
            "boxplot": 
            {
                "snippet" : ('box', 'snippet'), 
                "plot": ('box', 'plot')
            }
        }



def setDataset(newdataset):
    global dataset
    dataset = newdataset


