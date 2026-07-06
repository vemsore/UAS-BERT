"""
TEST TRAINER BUILDER
"""

from app.training.trainer_builder import build_training_arguments

args = build_training_arguments()

print("=" * 60)

print("TRAINING ARGUMENTS")

print("=" * 60)

print(args)