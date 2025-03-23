# # Initialize an empty dictionary to store the mapping
# noun_mapping = {}
#
# # Open and read the English and Urdu files
# with open('tatoeba_pn_eng.txt', 'r', encoding='utf-8') as eng_file, open('tatoeba_pn_urdu.txt', 'r', encoding='utf-8') as urdu_file:
#     english_nouns = eng_file.read().splitlines()
#     urdu_nouns = urdu_file.read().splitlines()
#
# # Ensure both lists have the same number of items
# if len(english_nouns) == len(urdu_nouns):
#     # Create the dictionary by pairing English nouns with their Urdu translations
#     noun_mapping = dict(zip(english_nouns, urdu_nouns))
# else:
#     print("The files do not have the same number of lines.")
#
# # Print the resulting dictionary
# for eng, urdu in noun_mapping.items():
#     print(f"'{eng}' : '{urdu}'")
# Initialize an empty dictionary to store the mapping
noun_mapping = {}

# Open and read the English and Urdu files
with open('augmentation/augmentation_without_urdu_alignment/proper_nouns/pn_processing/train_pn_eng.txt', 'r', encoding='utf-8') as eng_file, open(
        'augmentation/augmentation_without_urdu_alignment/proper_nouns/pn_processing/train_pn_urdu.txt', 'r', encoding='utf-8') as urdu_file:
    english_nouns = eng_file.read().splitlines()
    urdu_nouns = urdu_file.read().splitlines()

# Ensure both lists have the same number of items
if len(english_nouns) == len(urdu_nouns):
    # Create the dictionary by pairing English nouns with their Urdu translations
    noun_mapping = dict(zip(english_nouns, urdu_nouns))
else:
    print("The files do not have the same number of lines.")

# Save the dictionary to a text file
with open('augmentation/augmentation_without_urdu_alignment/proper_nouns/pn_processing/train_eng_urdu_pn_dict.txt', 'w', encoding='utf-8') as dict_file:
    for eng, urdu in noun_mapping.items():
        dict_file.write(f"'{eng}' : '{urdu}',\n")

print("Dictionary saved to 'eng_urdu_pn_dict.txt'")
