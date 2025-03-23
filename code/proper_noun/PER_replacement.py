import random
import re

# Read male and female urdu_names from files
with open('urdu_names/male_names.txt', 'r') as male_names_file:
    male_names = male_names_file.read().splitlines()

with open('urdu_names/female_names.txt', 'r') as female_names_file:
    female_names = female_names_file.read().splitlines()


# Function to extract and replace urdu_names in logical and textual representations
def replace_names(logical_rep, text_rep):
    # Find all name occurrences and their genders
    name_matches = re.findall(r'(male\.n\.02|female\.n\.02) Name "([^"]+)"', logical_rep)

    for gender, old_name in name_matches:
        # Identify the same name in the corresponding text representation
        text_name_matches = re.findall(f'{old_name}', text_rep, re.IGNORECASE)

        # If there is at least one match in the text representation, replace it
        if text_name_matches:
            new_name = random.choice(male_names) if gender == 'male.n.02' else random.choice(female_names)
            logical_rep = logical_rep.replace(f'{gender} Name "{old_name}"', f'{gender} Name "{new_name}"')
            text_rep = re.sub(f'{old_name}', f'{new_name}', text_rep, flags=re.IGNORECASE)

    return logical_rep, text_rep


# Read the dataset file and process each line
with open('urdu_train.sbn', 'r') as dataset_file:
    lines = dataset_file.readlines()

# Create a new file to save the modified data
with open('urdu_train_with_pn-PER-only.sbn', 'w') as new_dataset_file:
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            logical_rep, text_rep = replace_names(parts[1], parts[0])
            new_line = f'{text_rep}\t{logical_rep}\n'
            new_dataset_file.write(new_line)

print("Data modification and saving complete.")
