from mockito import when, mock, unstub
import framework.graphs as graphs
import service.sampler as sampler
import framework.mixin as mixin
import service.retrieval as retrieval
import seaborn as sns; sns.set()
from random import randint
import subprocess
import re

responseDataSet = {
    'scatter_data': sns.load_dataset("iris"),
    'boxplot_data': sns.load_dataset("tips"),
    'barplot_data': sns.load_dataset("tips")
}
scatter_axis = {
        'x-axis':   responseDataSet['scatter_data'].sepal_length,
        'y-axis':   responseDataSet['scatter_data'].sepal_width
    }
boxplot_axis = {
        'x-axis':   "day",
        'y-axis':   "total_bill",
    }
barplot_axis= {
        'x-axis':  "tip",
        'y-axis':  "day"
    }
responseAxisInfo = {
    'scatter_axis': scatter_axis,
    'boxplot_axis': boxplot_axis,
    'barplot_axis': barplot_axis
}

responseSnippet={
    "scatterplot": ["scatterplot_code","scatterplot_graph"],
    "barplot": ["barplot_code","barplot_graph"], 
    "boxplot": ["boxplot_code","boxplot_graph"]
}


def randomplot():
    print("mocking random")
    a = subprocess.check_output("ls").decode()
    responseRetrive = re.findall('(\S+png)', a)
    # responseRetrive=['dutsfgnahw.png', 'dwshuugwer.png', 'glslcehgje.png']
    num_plots = randint(0,len(responseRetrive))
    imgs = []
    for i in range(1,num_plots):
        img = 'framework/allplots/'+responseRetrive[randint(0,len(responseRetrive)-1)]
        imgs.append(img)
    return imgs

responseRetrival = randomplot()


when(mixin).fetchDB_path().thenReturn('framework/allplots/')
when(graphs).load_dataset('scatterplot', ...).thenReturn(responseDataSet['scatter_data'])
when(graphs).load_dataset('boxplot', ...).thenReturn(responseDataSet['boxplot_data'])
when(graphs).load_dataset('barplot', ...).thenReturn(responseDataSet['barplot_data'])

when(graphs).fetchAxisInfo('scatterplot', ...).thenReturn(responseAxisInfo['scatter_axis'])
when(graphs).fetchAxisInfo('boxplot', ...).thenReturn(responseAxisInfo['boxplot_axis'])
when(graphs).fetchAxisInfo('barplot', ...).thenReturn(responseAxisInfo['barplot_axis'])

when(sampler).retrieve_snippet('scatterplot').thenReturn(responseSnippet['scatterplot'])
when(sampler).retrieve_snippet('barplot').thenReturn(responseSnippet['barplot'])
when(sampler).retrieve_snippet('boxplot').thenReturn(responseSnippet['boxplot'])

when(mixin).fetchplotfromDB(..., ...).thenReturn(responseRetrival)
