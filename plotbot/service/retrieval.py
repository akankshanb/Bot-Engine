import framework.mocking_agent
import framework.mixin as mixin
import framework.constants as constants


def fetch(message, user):
    print("----")
    text_list = message.lower().strip().split()
    plot = text_list[len(text_list)-1]
    filenames = mixin.fetchplotfromDB(plot, user)
    print(filenames)
    return "Here are your plots", filenames
    # for each user id, filename of the graphs