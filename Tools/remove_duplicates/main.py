import os
import csv
import json
import subprocess
import sys
import xml.etree.ElementTree as ET


def ensure_package_installed(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"Installing {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

ensure_package_installed("pandas")
ensure_package_installed("openpyxl")

import pandas as pd


def remove_duplicates(input_file, output_file):
    file_ext = os.path.splitext(input_file)[1].lower()

    if file_ext == '.txt':
        process_text_file(input_file, output_file)
    elif file_ext == '.csv':
        process_csv_file(input_file, output_file)
    elif file_ext == '.json':
        process_json_file(input_file, output_file)
    elif file_ext == '.xlsx':
        process_excel_file(input_file, output_file)
    elif file_ext == '.xml':
        process_xml_file(input_file, output_file)
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")


def process_text_file(input_file, output_file):
    unique_lines = set()
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
        unique_lines = list(dict.fromkeys(line.strip() for line in lines))

    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(unique_lines))


def process_csv_file(input_file, output_file):
    unique_rows = set()
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        unique_rows = {tuple(row) for row in reader}

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(list(unique_rows))


def process_json_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    if isinstance(data, list):
        unique_data = list({json.dumps(item, sort_keys=True) for item in data})
        unique_data = [json.loads(item) for item in unique_data]

        with open(output_file, 'w') as outfile:
            json.dump(unique_data, outfile, indent=4)
    else:
        raise ValueError("Only JSON arrays are supported.")


def process_excel_file(input_file, output_file):
    df = pd.read_excel(input_file)
    df.drop_duplicates(inplace=True)
    df.to_excel(output_file, index=False)


def process_xml_file(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    seen = set()
    unique_elements = []
    for element in root:
        serialized = ET.tostring(element, encoding='unicode')
        if serialized not in seen:
            seen.add(serialized)
            unique_elements.append(element)

    new_root = ET.Element(root.tag)
    for unique_element in unique_elements:
        new_root.append(unique_element)

    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_file, encoding='unicode')


