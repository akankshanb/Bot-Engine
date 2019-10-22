def retrieve_snippet(plottype):
    snippet_dict={"scatterplot": ["scatterplot_code","scatterplot_graph"],
<<<<<<< HEAD
         "barplot": ["barplot_code","barplot_graph"], "boxplot": ["boxplot_code","boxplot_graph"]} 
    if plottype in snippet_dict:
        return snippet_dict[plottype]
=======
         "barplot": ["barplot_code","barplot_graph"], "boxplot": ["boxplot_code","boxplot_graph"]}
    if type in snippet_dict:
        return snippet_dict[type]
>>>>>>> 586e0ede01853fb21c441313b98bbcdc4e68a9d7
    else:
        raise ValueError('Requested plot sample not available')

def fetch(input_txt):
    text_list = input_txt.lower().strip().split()
    files=[]

    snippets=retrieve_snippet(text_list[1])
    for name in snippets:
        path="sample_plots/"+name+".png"
        files.append(path)
    return "Here is you code snippet for **{}**".format(text_list[1]),files
    