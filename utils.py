"""
This module contains functions that can be used across the project
"""

def evaluate_type(type_to_check_against, *variables_to_evaluate) -> bool:
    """checks if all variables_to_evaluate are type_to_check_against"""
    return all(isinstance(arg, type_to_check_against) for arg in variables_to_evaluate)
