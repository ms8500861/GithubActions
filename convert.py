import yaml
import json

# Load the YAML file
with open('input.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Convert the YAML data to JSON and save it to a file
with open('output.json', 'w') as json_file:
    json.dump(yaml_data, json_file, indent=4)

print("Conversion from YAML to JSON completed successfully.")
