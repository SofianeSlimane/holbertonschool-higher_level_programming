#!/usr/bin/python3
"""This module contains the serialize_to_xml
function and the deserialize_from_xml function.
"""
import xml.etree.ElementTree as ET


# Random commentaries are for testing purposes, don't mind them.
def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to xml data.
    Args:
        dictionary: dictionary where each keys
        represent an element in the tree and
        each values, is some text in the element.
        filename: xml file
    """
    root = ET.Element("data")
    for keys, value in dictionary.items():
        child_element = ET.Element(keys)
        child_element.text = value
        root.append(child_element)
    tree_string = ET.tostring(root, encoding='utf8').decode('utf8')
    with open(filename, "w") as myFile:
        myFile.write(tree_string)


def deserialize_from_xml(filename):
    """Deserialize xml tree into Python
    dictionary.
    Args:
        filename: xml file to read from
    Returns: dictionary of xml tree
    """
    my_dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    # print(ET.tostring(root, encoding='utf8').decode('utf8'))
    for child in root:
        # print(child.tag)
        # print(child.text)
        my_dict.update({child.tag: child.text})

    return my_dict
