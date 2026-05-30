from core.state import STATE

def list_add(list_name: str, item: str, amount: int):
    if list_name not in STATE:
        STATE[list_name] = []
    
    STATE[list_name].append({"name": item, "amount": amount})
    return f"Added {item} to {list_name}."

def list_list(list_name: str):
    if list_name not in STATE:
        return f"List '{list_name}' does not exist."
    return str(STATE[list_name])

def list_remove(list_name: str, item_name: str):
    if list_name not in STATE:
        return f"List '{list_name}' not found."
    
    original_len = len(STATE[list_name])
    STATE[list_name] = [i for i in STATE[list_name] if i["name"] != item_name]
    
    return f"Removed {item_name} from {list_name}." if len(STATE[list_name]) < original_len else "Item not found."