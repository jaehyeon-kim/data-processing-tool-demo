import importlib
import src.funcs


def get_func_names():
    """Return a list of source functions to be used in GroupBy operations"""
    return [item for item in dir(src.funcs) if not item.startswith("__") and item != "numpy"]


def map_plugins():
    """Create a dictionary of callable functions"""
    plugins = {}
    for fun in get_func_names():
        plugins[fun] = getattr(importlib.import_module("src.funcs"), fun)
    return plugins
