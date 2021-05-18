import sys
import xml.etree.ElementTree as ET
import data_converter

def main():
    #Check for file name in argument vector
    if len(sys.argv)==1: 
        sys.exit("File name cannot be empty. Please type the name of the file to be parsed")
    
    #Get file name from argument vector
    file_name = sys.argv[1]

    #Parse XML document into element tree
    tree = ET.parse(file_name)
    #Get root element from the tree
    root = tree.getroot()

    #Convert the element tree to a dictionary
    dict = data_converter.tree_to_dict(root)

    #Convert the dictionary to JSON format    
    parsed_file = data_converter.dict_to_json(dict, file_name)

    #Notify user
    print(file_name + " successfully parsed!")

if __name__ == "__main__":
    main()
