#!/usr/bin/python3
"""This module contains the convert_cvs_to_json function"""
import csv
import json


def convert_csv_to_json(csv_file):
    """Converts cvs data to json.
    Args:
        cvs_file: cvs file containing the data
    Returns: True if conversion was successful, else, false
    """
    my_list = []
    try:
        with open(csv_file, "r", encoding="utf-8") as myFile:
            csvReader = csv.DictReader(myFile)
            for rows in csvReader:
                my_list.append(rows)
        with open("data.json", "w", encoding="utf-8") as myFile:
            json.dump(my_list, myFile, indent=1)
        return True
    except FileNotFoundError:
        return False
    except AttributeError:
        return False
    except EOFError:
        return False
    except ImportError:
        return False
    except IndexError:
        return False
    except cvs.Error:
        return False
