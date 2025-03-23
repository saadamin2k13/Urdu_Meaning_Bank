## Urdu Meaning Bank, The very first Semantic Resource for Urdu

In this repo, we include the code, dataset, and model for our LR&E paper entitled:

### "Semantic processing for Urdu: corpus creation, parsing, and generation"

Here, we include:

1. **code:** All dataset processing scripts for dataset development and augmentation are present in the folder.
2. **dataset:** This folder includes all flavors of augmented datasets and also the dataset without augmentation. 
3. **evaluation:** This folder contains scripts to evaluate model performance through automatic and pre-trained model-based evaluation metrics for both parsing and generation. 
4. **output_files:** This folder contains the model-generated outputs for all the experiments reported in the paper.

Our fine-tuned models for Urdu [**Semantic Parsing**](https://huggingface.co/saadamin2k13/urdu_semantic_parsing) and [**Text Generation**](https://huggingface.co/saadamin2k13/urdu_text_generation) are publically available for research purposes.

**1. The figure below represents multilingual different representations of the DRS/SBN.**
![image](https://github.com/user-attachments/assets/93bd6664-3749-4f70-b7ea-5e2a0c1b299e)




**2. Comparing English and Urdu SBN along with their corresponding textual representations based on syntactic structure and surface alignment. Note that word order in Urdu is right to left.**
![image](https://github.com/user-attachments/assets/38895b49-5f5e-415b-8c4b-7b580a9ec98d)



**3. Augmentation examples for Urdu semantic parsing and generation. Note: Aug = Augmentation.**
![image](https://github.com/user-attachments/assets/af882876-6222-46d9-84f9-ba8453b04b38)



**4. Meaning representation of the sentence “Bill didn’t commit the crime.” of fine-grained evaluation in node-level and edge-level. We highlight two examples in Nouns and Verbs in blue in (a) and one operator-triple in orange in (b).**

![image](https://github.com/user-attachments/assets/37622076-0fa6-4ad8-a209-f1f55a0c180d)


**5. Human Evaluation**

Perfect and ROSE evaluation based on manual analysis for Urdu generation task. We have listed 4 different cases each reporting: (1) Perfect: all those examples that have the same model-generated text as listed in
the gold examples; (2) Semantics: representing those examples that are semantically correct only; (3) Grammaticality: examples that are grammatically correct but not sustaining the same semantic information; and (4) ROSE: that is the product of semantic and grammatical evaluation scores. Note: for the first 2 columns, we have mentioned the English translations of the Urdu text (in double quotes) for understanding purposes.
![image](https://github.com/user-attachments/assets/80a6db4c-1abe-43b9-bc4f-a0885ce80797)

**6. Results**

![image](https://github.com/user-attachments/assets/701a5af5-22c9-4ed3-a5bb-49fe9db67dc9)




### Contributors
Muhammad Saad Amin, Xiao Zhang, Luca Anselma, Alessandro Mazzei, and Johan Bos.

