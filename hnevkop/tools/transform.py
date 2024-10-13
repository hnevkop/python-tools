import csv
import yaml

data_dic = {}  # initialize the dictionary outside the 'with' block

with open('../../resources/data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:  # move this block inside the 'with' block
        country_name = row['country_code'].upper().replace(" ", "_")
        data_dic[country_name] = {
            'name': row['country_NAME'],
            'iso-code': row['ISO_Code'],
            'currency': row['currency']
        }

# continue with the rest of your code
final_yaml = {
    'root': {
        'countries': data_dic
    }
}

with open('output.yaml', 'w') as outfile:
    yaml.safe_dump(final_yaml, outfile)
