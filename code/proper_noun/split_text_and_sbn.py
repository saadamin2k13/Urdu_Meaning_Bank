# Read the dataset from a file
with open(
        './pipeline/generation/urdu_test.sbn', 'r') as f:
    dataset = f.readlines()

# Separate text and SBN and save them in separate files
text_file = open('./original_urdu_dataset_files/urdu_testset_text.txt', 'w')
sbn_file = open('./original_urdu_dataset_files/urdu_testset_sbn.txt', 'w')

for example in dataset:
    parts = example.strip().split('\t')
    if len(parts) == 2:
        text, sbn = parts
        text_file.write(text + '\n')
        sbn_file.write(sbn + '\n')

# Close the files
text_file.close()
sbn_file.close()
