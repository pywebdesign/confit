import importlib



def import_anything(fully_qualified_path: str):
    """Import anything, class or function or class method or even property
    Args:
        fully_qualified_path (str): The fully qualified path to the class or function
    Returns:
        The imported class or function
    """
    current_thing = None
    acc = []
    for particle in fully_qualified_path.split("."):
        try:
            acc.append(particle)
            current_thing = importlib.import_module(".".join(acc))
        except ModuleNotFoundError:
            if current_thing is None:
                raise ModuleNotFoundError(f"Module {particle} not found")
            else:
                if hasattr(current_thing, particle):
                    current_thing = getattr(current_thing, particle)
                else:
                    raise AttributeError(f"Attribute {particle} not found in module {'.'.join(acc)}")
        
    return current_thing