"""
=========================================================
TRAINER BUILDER

UAS Analisis Sentimen
IndoBERT

Rekhan Fadhillah Syahputra
2313500122
=========================================================
"""
from app.training.callbacks import CSVLoggerCallback
from transformers import (
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback
)

from app.training.train_config import (
    CONFIG,
    OUTPUT_DIR,
    LOG_DIR
)

from app.training.metrics import compute_metrics


def build_training_arguments():

    return TrainingArguments(

        # Output
        output_dir=str(OUTPUT_DIR),

        # Epoch
        num_train_epochs=CONFIG["epochs"],

        # Batch
        per_device_train_batch_size=CONFIG["train_batch_size"],

        per_device_eval_batch_size=CONFIG["valid_batch_size"],

        gradient_accumulation_steps=CONFIG["gradient_accumulation"],

        # Optimizer
        learning_rate=CONFIG["learning_rate"],

        weight_decay=CONFIG["weight_decay"],

        # Evaluation
        eval_strategy=CONFIG["evaluation_strategy"],

        save_strategy=CONFIG["save_strategy"],

        load_best_model_at_end=CONFIG["load_best_model"],

        metric_for_best_model="f1",

        greater_is_better=True,

        # Logging
        logging_dir=str(LOG_DIR),

        logging_steps=CONFIG["logging_steps"],

        report_to="none",

        seed=CONFIG["random_state"],

        save_total_limit=2
    )


def build_trainer(
        model,
        train_dataset,
        valid_dataset,
):

    args = build_training_arguments()

    trainer = Trainer(

        model=model,

        args=args,

        train_dataset=train_dataset,

        eval_dataset=valid_dataset,

        compute_metrics=compute_metrics,

        callbacks=[

    EarlyStoppingCallback(
        early_stopping_patience=CONFIG["early_stopping"]
    ),

    CSVLoggerCallback()

]
    )

    return trainer