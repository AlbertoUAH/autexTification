# -- Unit test modules
# -- Import libraries
from transformers import AutoTokenizer, AutoModel
import yaml

with open('./wandb/test/sweep.yaml', 'r') as yaml_file:
	config_file = dict(yaml.safe_load(yaml_file))

print(config_file)
# -- Check if model & tokenizer exist
def test_check_model_existence():
	model_name = config_file['parameters']['model']['value']
	exist = False
	try:
		tokenizer = AutoTokenizer.from_pretrained(model_name)
		model     = AutoModel.from_pretrained(model_name)
		exist     = True
	except OSError:
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
