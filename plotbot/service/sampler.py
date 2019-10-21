snippet_dict={"scatterplot": "<file_path>", "barplot": "<file_path>", "boxplot": "<file_path>"} 

def fetch(input_txt):
    text_list = input_txt.lower().strip().split()
    if text_list[1] in snippet_dict.keys():
        file_name = snippet_dict[text_list[1]]
        return "Here is you code snippet for **{}**".format(text_list[1])
    else:
        raise ValueError('A very specific bad thing happened')