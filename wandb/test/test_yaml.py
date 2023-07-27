# -- Unit test modules
# -- Import libraries
from transformers import AutoTokenizer, AutoModel
import yaml
import os

print("PRINT")
print(os.listdir('./wandb/test'))

with open('./wandb/test/sweep.yaml', 'r') as yaml_file:
	config_file = yaml.safe_load(yaml_file)

# -- Check if model & tokenizer exist
def check_model_existence():
	model_name = config_file['parameters']['model']['value']
	try:
		tokenizer = AutoTokenizer.from_pretrained(model_name)
		model     = AutoModel.from_pretrained(model_name)
		exist     = True
	except OSError:
		exist = False
	finally:
		assert exist

# -- Check if number of epochs is greater than zero
def check_num_epochs():
	num_epochs = int(config_file['num_train_epochs']['value'])
	assert num_epochs > 0

# -- Check if convert_to_lowercase parameters is 0 or 1
def check_convert_to_lowercase():
	convert_to_lowercase = int(config_file['text_to_lowercase']['value'])
	assert convert_to_lowercase >= 0 and convert_to_lowercase <= 1
