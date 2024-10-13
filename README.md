# Python Tools

This repository contains a collection of Python tools for development.

## transform.py

The `transform.py` script is a tool that reads data from a CSV file and transforms it into a YAML file.

The CSV file should be located in the `resources` directory and should have the following structure:

```csv
country_code,country_NAME,ISO_Code,currency
us,United States,US,USD
ca,Canada,CA,CAD
gb,United Kingdom,GB,GBP
au,Australia,AU,AUD
jp,Japan,JP,JPY
```

The script will transform this data into a YAML file with the following structure:

```yaml
root:
  countries:
    AU:
      currency: AUD
      iso-code: AU
      name: Australia
    CA:
      currency: CAD
      iso-code: CA
      name: Canada
    GB:
      currency: GBP
      iso-code: GB
      name: United Kingdom
    JP:
      currency: JPY
      iso-code: JP
      name: Japan
    US:
      currency: USD
      iso-code: US
      name: United States
```

## Usage 
To run the transform.py script, navigate to the tools/hnevkop/tools directory and run the following command:
``
python transform.py
``

## Requirements
This script requires Python 3.11 and the following Python packages:  
csv
yaml

You can install these packages using pip:

``
pip install pyyaml
``
