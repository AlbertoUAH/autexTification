# AutexTification contest 

[Source](https://sites.google.com/view/autextification/data?authuser=1)

## Organizers

<p align="center">
    <img src="/media/symanto.png"  width="40%" height="20%">
    <img src="/media/upv.jpg"  width="40%" height="20%">
</p>


## Approaches

### Transformer only: Multilingual BERT

#### 1. [Multilingual BERT cased](https://huggingface.co/bert-base-multilingual-cased)

|Epoch (best)|Training Loss|Validation Loss|Accuracy|Precision|Recall|F1|
|-----|-------------|---------------|--------|---------|------|--|
|1|0.241600|0.236673|0.906387|0.880825|0.941159|0.909993|

#### 2. [Multilingual BERT uncased](https://huggingface.co/bert-base-multilingual-uncased)

|Epoch (best)|Training Loss|Validation Loss|Accuracy|Precision|Recall|F1|
|-----|-------------|---------------|--------|---------|------|--|
|1|0.158400|0.248109|0.923380|0.898779|0.955190|0.926126|

#### 3. Extract features + PyCaret

__Top models__

|Model|Accuracy|Precision|Recall|F1|
|-----|--------|---------|------|--|
|CatBoost Classifier|0.7851|0.7844|0.7886|0.7864|
|Random Forest Classifier|0.7750|0.7681|0.7901|0.7789|
|Extreme Gradient Boosting|0.7725|0.7730|0.7740|0.7734|
|Light Gradient Boosting Machine|0.7680|0.7770|0.7886|0.7707|

### Metadata + Transformer approach

* Readability and/or Complexity
* Comprehension
* Volumetrics (text length, number of characters, number of words)
* Sentiment
* Hate comments
* Subjectivity (TextBlob -> English only: https://github.com/sloria/TextBlob/iss<zues/209)
* Lemmas
* Topic Modelling
* Bag of Words (BoW)
* Part of Speech (POS)
* Emotions

## References

[1] Automatic Detection of Machine Generated Text: A Critical Survey, by Ganesh Jawahar, Muhammad Abdul-Mageed, Laks V.S. Lakshmanan. URL: https://aclanthology.org/2020.coling-main.208.pdf

[2] To Chat GPT, or not to Chat GPT: That is the question! By Alessandro Pegoraro, Kavita Kumari, Hossein Fereidooni, Ahmad-Reza Sadeghi. URL: https://arxiv.org/pdf/2304.01487.pdf

[3] How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection. By Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang1, Jinran Nie, Yuxuan Ding, Jianwei Yue, Yupeng Wu. URL: https://arxiv.org/pdf/2301.07597.pdf
