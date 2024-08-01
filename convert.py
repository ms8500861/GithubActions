import yaml
import json

input_file = 'input.yaml'
output_file = 'output.json'

# Load the YAML file
with open(input_file, 'r', encoding='utf8') as file:
    data = yaml.safe_load(file)

# Write the JSON file
with open(output_file, 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("Conversion from YAML to JSON completed successfully.")
