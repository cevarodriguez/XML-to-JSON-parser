import json
from copy import copy

#Function to convert the tree to a dictionary
def tree_to_dict(r,root=True):
    if root:
        #Return a dictionary with format: key- the element tag, value- the result of the function itself
        return {r.tag : tree_to_dict(r, False)}
        #Shallow copy of the element attributes to the dictionary
    d = copy(r.attrib)
    #If there's text, process it
    if r.text:
        d["_text"] = r.text
        #Loop through the whole tree
    for x in r.findall("./*"):
        #If new tags are found, add them to the dictionary
        if x.tag not in d:
            d[x.tag] = []
        d[x.tag].append(tree_to_dict(x,False))
    return d

#Transform dict to JSON
def dict_to_json(a_dict, file_name):
    with open (file_name +"_parsed.json", "w") as outfile:
        json.dump(a_dict, outfile)