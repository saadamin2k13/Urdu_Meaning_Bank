import random
import re

# Read city, state, country, and island urdu_names from files
with open('urdu_names/city_names.txt', 'r') as city_file:
    city_names = city_file.read().splitlines()

with open('urdu_names/state_names.txt', 'r') as state_file:
    state_names = state_file.read().splitlines()

with open('urdu_names/country_names.txt', 'r') as country_file:
    country_names = country_file.read().splitlines()

with open('urdu_names/island_names.txt', 'r') as island_file:
    island_names = island_file.read().splitlines()


# Function to extract and replace urdu_names in logical and textual representations
def replace_names(logical_rep, text_rep):
    # Find all name occurrences and their entity types
    name_matches = re.findall(r'((city\.n\.\d+|state\.n\.\d+|country\.n\.\d+|island\.n\.\d+) Name "([^"]+)")',
                              logical_rep)
    new_logical_rep = logical_rep
    new_text_rep = text_rep

    for full_match, entity_type, old_name in name_matches:
        if entity_type.startswith('city'):
            new_name = random.choice(city_names)
        elif entity_type.startswith('state'):
            new_name = random.choice(state_names)
        elif entity_type.startswith('country'):
            new_name = random.choice(country_names)
        elif entity_type.startswith('island'):
            new_name = random.choice(island_names)

        # Replace the name in both logical and textual representations
        new_logical_rep = new_logical_rep.replace(full_match, f'{entity_type} Name "{new_name}"')
        new_text_rep = new_text_rep.replace(f'{old_name}', f'{new_name}')

    return new_logical_rep, new_text_rep


# Read the dataset file and process each line
with open('../../augmentation_with_urdu_aligned_re_splitted_data/proper_noun/urdu_train_with_pn-PER-only.sbn', 'r') as dataset_file:
    lines = dataset_file.readlines()

# Create a new file to save the modified data
with open('../../augmentation_with_urdu_aligned_re_splitted_data/proper_noun/urdu_train_with_pn_aug.sbn', 'w') as new_dataset_file:
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            logical_rep, text_rep = replace_names(parts[1], parts[0])
            new_line = f'{text_rep}\t{logical_rep}\n'
            new_dataset_file.write(new_line)

print("Data modification and saving complete.")
# import random
# import re
#
# # Read city, state, country, and island urdu_names from files
# with open('./p_nouns_from_sbn/cities/shuffled_city.txt', 'r') as city_file:
#     city_names = city_file.read().splitlines()
#
# with open('./p_nouns_from_sbn/states/shuffled_states.txt', 'r') as state_file:
#     state_names = state_file.read().splitlines()
#
# with open('./p_nouns_from_sbn/countries/shuffled_country.txt', 'r') as country_file:
#     country_names = country_file.read().splitlines()
#
# with open('./p_nouns_from_sbn/island/shuffled_island.txt', 'r') as island_file:
#     island_names = island_file.read().splitlines()
#
# # Function to extract and replace urdu_names in logical and textual representations
# def replace_names(logical_rep, text_rep):
#     # Find all name occurrences and their entity types
#     name_matches = re.findall(r'((city\.n\.\d+|state\.n\.\d+|country\.n\.\d+|island\.n\.\d+) Name "([^"]+)")',
#                               logical_rep)
#     new_logical_rep = logical_rep
#     new_text_rep = text_rep
#
#     for full_match, entity_type, old_name in name_matches:
#         if entity_type.startswith('city'):
#             new_name = random.choice(city_names)
#         elif entity_type.startswith('state'):
#             new_name = random.choice(state_names)
#         elif entity_type.startswith('country'):
#             new_name = random.choice(country_names)
#         elif entity_type.startswith('island'):
#             new_name = random.choice(island_names)
#
#         # Create a regex pattern to match the old name with case insensitivity
#         pattern = re.compile(f'({re.escape(entity_type)} Name "{re.escape(old_name)}")', re.IGNORECASE)
#
#         # Replace the name in both logical and textual representations (case-insensitive)
#         new_logical_rep = pattern.sub(f'{entity_type} Name "{new_name}"', new_logical_rep)
#         new_text_rep = pattern.sub(f'{new_name}', new_text_rep)
#
#     return new_logical_rep, new_text_rep
#
# # Read the dataset file and process each line
# with open('gold_train.sbn', 'r') as dataset_file:
#     lines = dataset_file.readlines()
#
# # Create a new file to save the modified data
# with open('per_and_gpe_aug_inside.sbn', 'w') as new_dataset_file:
#     for line in lines:
#         parts = line.strip().split('\t')
#         if len(parts) == 2:
#             logical_rep, text_rep = replace_names(parts[1], parts[0])
#             new_line = f'{text_rep}\t{logical_rep}\n'
#             new_dataset_file.write(new_line)
#
# print("Data modification and saving complete.")
