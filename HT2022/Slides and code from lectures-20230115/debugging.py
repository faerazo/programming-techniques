# In the following exercises you will be given a series of buggy code
# examples, your task will be to identify these bugs by reading the
# code line by line.
#
# While reading, you will have to:
#
# 1. Recognize the bug,
# 2. Identify the cause of the bug,
# 3. Propose a fix


# Exercise 1: all_zero

def all_zero(p_list):
    """ Check if all elements are zero.
    :param p_list: list of integers
    :return: boolean
    """
    for x in p_list:
        if x != 0:
            return "False"
        else:
            return "True"

# What are the bugs in this code?
# What tests can we write to find the bugs?
# How can we fix the bugs?




# Exercise 2: add_hyphens

def add_hyphens(text):
    """ Adds a hyphen between letters
    :param text: string
    :return: string
    """
    new_text = " "

    for idx in range(text):
        if idx == 0:
            # add first letter
            new_text = text[i] + "-"
        elif idx == len(text):
            # add last letter
            new_text = text[idx]

        new_text = text[idx] + "-"

    return new_text

# What are the bugs in this code?
# What tests can we write to find the bugs?
# How can we fix the bugs?
