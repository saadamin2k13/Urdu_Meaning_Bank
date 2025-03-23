import re
from collections import OrderedDict

# Regular expression pattern to match the entities within double quotes
pattern = r'(male\.n\.[0-9]+ Name|female\.n\.[0-9]+ Name|city\.n\.[0-9]+ Name|state\.n\.[0-9]+ Name|country\.n\.[0-9]+ Name|island\.n\.[0-9]+ Name) "(.*?)"'

# Initialize an ordered dictionary to store the extracted entities in order
extracted_entities = OrderedDict()

# Read data from the input file and extract entities
with open('./splitted_english_dataset_files/en_test_sbn.txt', 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            entity = match[1]  # Extract the second group (the entity name)
            extracted_entities[entity] = None  # Use a dictionary to ensure uniqueness while preserving order

# Save the unique entities in the same order to the output file
with open('augmentation/augmentation_without_urdu_alignment/proper_nouns/pn_processing/test_pn_eng.txt', 'w') as output_file:
    for entity in extracted_entities.keys():
        output_file.write(entity + '\n')
