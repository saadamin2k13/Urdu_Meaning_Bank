## Urdu Meaning Bank, The very first Semantic Resource for Urdu

In this repo, we include the code, dataset, and model for our LR&E paper entitled:

### "Semantic processing for Urdu: corpus creation, parsing, and generation"

Here, we include:

1. **code:** All dataset processing scripts for dataset development and augmentation are present in the folder.
2. **dataset:** This folder includes all flavors of augmented datasets and also the dataset without augmentation. 
3. **evaluation:** This folder contains scripts to evaluate model performance through automatic and pre-trained model-based evaluation metrics for both parsing and generation. 
4. **output_files:** This folder contains the model-generated outputs for all the experiments reported in the paper.




**1. The figure below represents multilingual different representations of the DRS/SBN.**
[drs-shapes.pdf](https://github.com/user-attachments/files/19407608/drs-shapes.pdf)




**2. Comparing English and Urdu SBN along with their corresponding textual representations based on syntactic structure and surface alignment. Note that word order in Urdu is right to left.**
[urdu-english-shapes.pdf](https://github.com/user-attachments/files/19407613/urdu-english-shapes.pdf)



**3. Augmentation examples for Urdu semantic parsing and generation. Note: Aug = Augmentation.**
[tab-1.pdf](https://github.com/user-attachments/files/19407618/tab-1.pdf)



**4. Meaning representation of the sentence “Bill didn’t commit the crime.” of fine-grained evaluation in node-level and edge-level. We highlight two examples in Nouns and Verbs in blue in (a) and one operator-triple in orange in (b).**
[examples.pdf](https://github.com/user-attachments/files/19407633/examples.pdf)

**5. Human Evaluation**

Perfect and ROSE evaluation based on manual analysis for Urdu generation task. We have listed 4 different cases each reporting: (1) Perfect: all those examples that have the same model-generated text as listed in
the gold examples; (2) Semantics: representing those examples that are semantically correct only; (3) Grammaticality: examples that are grammatically correct but not sustaining the same semantic information; and (4) ROSE: that is the product of semantic and grammatical evaluation scores. Note: for the first 2 columns, we have mentioned the English translations of the Urdu text (in double quotes) for understanding purposes.
[tab-2.pdf](https://github.com/user-attachments/files/19407634/tab-2.pdf)



### Contributors
Muhammad Saad Amin, Xiao Zhang, Luca Anselma, Alessandro Mazzei, and Johan Bos.

