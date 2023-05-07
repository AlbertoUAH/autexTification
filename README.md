# AutexTification contest 

[Source](https://sites.google.com/view/autextification/data?authuser=1)

## Organizers

<p align="center">
    <img src="/media/symanto.png"  width="40%" height="20%">
    <img src="/media/upv.jpg"  width="40%" height="20%">
</p>


## Approaches

### Transformer only: Multilingual BERT

#### 1. [Multilingual BERT uncased](https://huggingface.co/bert-base-multilingual-uncased)

|Epoch (best)|Training Loss|Validation Loss|Accuracy|Precision|Recall|F1|
|-----|-------------|---------------|--------|---------|------|--|
|2|0.149700|0.267662|0.922773|0.897985|0.954888|0.925563|

#### 2. [Multilingual BERT cased](https://huggingface.co/bert-base-multilingual-cased)

|Epoch (best)|Training Loss|Validation Loss|Accuracy|Precision|Recall|F1|
|-----|-------------|---------------|--------|---------|------|--|
|1|0.158400|0.248109|0.923380|0.898779|0.955190|0.926126|

#### 3. Extract features + [PyCaret](https://pycaret.org)

* Readability and/or Complexity
* Comprehension
* Volumetrics (text length, number of characters, number of words)
* [Sentiment analysis](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment)
* Hate comments via [detoxify](https://github.com/unitaryai/detoxify)
* [Emotion analysis](https://huggingface.co/MilaNLProc/xlm-emo-t)
* Part of Speech (POS) via [SpaCy](https://spacy.io/)
* Lemmas
* Repeated question and exclamation marks

__Results (sorted by best F1 scores)__

<p align="center">
    <img src="/media/ml_metrics_table.png"  width="70%" height="50%">
</p>

__Feature importance, top 4 models__

* CatBoost Classifier
* Random Forest Classifier
* Extreme Gradient Boosting
* Light Gradient Boosting Machine

<p align="center">
    <img src="/media/feature_importance.png"  width="80%" height="60%">
</p>

#### 4. Deep Learning approach with metadata

<p align="center">
    <img src="https://user-images.githubusercontent.com/45654081/235984368-f970703a-fe55-4d90-8c60-768cc8624e30.png"  width="40%" height="20%">
</p>

[Image source](https://www.semanticscholar.org/paper/Enriching-BERT-with-Knowledge-Graph-Embeddings-for-Ostendorff-Bourgonje/2cab7f5d64a427cb59fb21112fe8dc28fb753b56)

Q: __Beforehand, Which features should be used as "metadata" parameters?__

A: __Run Multi-Layer Perceptron (MLP) using previous features via PyCaret__

__Results__

|Model|Accuracy|AUC|Recall|Prec.|F1|Kappa|MCC|
|-----|--------|---|------|-----|--|-----|---|
|MLP Classifier|0.7712|0.8530|0.7787|0.7685|0.7736|0.5424|0.5424|

__Feature Importance__

<p align="center">
    <img src="/media/feature_importance_mlp.png"  width="60%" height="40%">
</p>

__Chosen features__:

* __nsent__: Number of sentences
* __LC__: Lexical Complexity Index
* __avgsentl__: Average sentence length
* __polini__: Polini's compressibility 
* __SSR index__
* __LDI index__

##### 4.1 Finetuning pretrained BERT uncased + fc (from scratch) - lr: 2e-05

|Epoch (best)|Training Loss|Validation Loss|Accuracy|Recall|F1|
|-----|-------------|---------------|--------|------|--|
|4 of 15|0.0100|0.1587|0.9354|0.9926|0.9392|

## References

[1] Automatic Detection of Machine Generated Text: A Critical Survey, by Ganesh Jawahar, Muhammad Abdul-Mageed, Laks V.S. Lakshmanan. URL: https://aclanthology.org/2020.coling-main.208.pdf

[2] To Chat GPT, or not to Chat GPT: That is the question! By Alessandro Pegoraro, Kavita Kumari, Hossein Fereidooni, Ahmad-Reza Sadeghi. URL: https://arxiv.org/pdf/2304.01487.pdf

[3] How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection. By Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang1, Jinran Nie, Yuxuan Ding, Jianwei Yue, Yupeng Wu. URL: https://arxiv.org/pdf/2301.07597.pdf
