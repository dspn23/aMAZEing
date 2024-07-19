def evaluate_type(type_to_check_against, *variables_to_evaluate) -> bool:
    """
    Parameters
    ----------
    type_to_check_against : Class (int, str, bool...)
        DESCRIPTION.
    *variables_to_evaluate : any
        DESCRIPTION.

    Returns
    -------
    bool
        True if they are all the reqired Class, False if not
    """
    return all(isinstance(arg, type_to_check_against) for arg in variables_to_evaluate)

