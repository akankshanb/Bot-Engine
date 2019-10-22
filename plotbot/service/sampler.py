snippet_dict={"scatterplot": ["scatter_code","scatter_graph"],
         "barplot": ["barplot_code","barplot_graph"], "boxplot": ["boxplot_code","boxplot_graph"]} 

def fetch(input_txt):
    text_list = input_txt.lower().strip().split()
    files=[]
    if text_list[1] in snippet_dict.keys():
        filenames = snippet_dict[text_list[1]]
        #Code
        files.append["sample_plots/"+filenames[0]+".png"]
        #Graph
        files.append["sample_plots/"+filenames[1]+".png"]
        return "Here is you code snippet for **{}**".format(text_list[1]),files
    else:
        raise ValueError('A very specific bad thing happened')