# -- Unit test modules
# -- Import libraries
from transformers import AutoTokenizer, AutoModel
import yaml
import os

with open('./wandb/test/sweep.yaml', 'r') as yaml_file:
	config_file = dict(yaml.safe_load(yaml_file))

# -- Check if code file for training is in config_file
def test_check_if_train_file_exists():
	train_file = config_file['program']
	assert train_file in os.listdir('./wandb/train/'), "Code file for training not found in ./wandb/train/ folder"

# -- Check if model & tokenizer exist
def test_check_model_existence():
	model_name = config_file['parameters']['model']['value']
	exist = False
	try:
		print("Exist: ", exist)
		tokenizer = AutoTokenizer.from_pretrained(model_name)
		model     = AutoModel.from_pretrained(model_name)
		exist     = True
	except Exception as e:
		print("EXCEPTION!!")
		print(e)
		exist = False
	finally:
		assert exist, "Model and/or tokenizer does not exist"

# -- Check if number of epochs is greater than zero
def test_check_num_epochs():
	num_epochs = int(config_file['parameters']['num_train_epochs']['value'])
	assert num_epochs > 0, "Number of epochs must be greater than zero"

# -- Check if convert_to_lowercase parameters is 0 or 1
def test_check_convert_to_lowercase():
	convert_to_lowercase = int(config_file['parameters']['text_to_lowercase']['value'])
	assert convert_to_lowercase >= 0 and convert_to_lowercase <= 1, "convert_to_lowercase is a binary variable (0, 1)"
