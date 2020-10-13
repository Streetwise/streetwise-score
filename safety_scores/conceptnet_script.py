import pandas as pd
from sklearn.model_selection import train_test_split
from simpletransformers.t5 import T5Model
import logging 
logging.basicConfig(level = logging.ERROR)

data = pd.read_csv("training/training_data.csv").astype(str)

train_df, eval_df = train_test_split(df, test_size=0.1)

model_args = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "max_seq_length": 128,
    "train_batch_size": 8,
    "num_train_epochs": 1,
    "save_eval_checkpoints": True,
    "save_steps": -1,
    "use_multiprocessing": False,
    "evaluate_during_training": True,
    "evaluate_during_training_steps": 15000,
    "evaluate_during_training_verbose": True,
    "fp16": False,

    "wandb_project": "conceptnet_t5",
}

model = T5Model("t5-base", args=model_args, use_cuda = False)
#model = T5Model("t5-large", args=model_args)

model.train_model(train_df, eval_data=eval_df)