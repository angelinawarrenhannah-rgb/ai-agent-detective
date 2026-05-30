from tools.tools import list_add, list_total, list_list, list_remove

TOOLS = {
    "list_add": list_add,
    "list_list": list_list,
    "list_remove": list_remove,
}

TOOL_DESCRIPTIONS = {
    "list_add": "Add an item to the list. args: item:str, amount:int",
    "list_list": "Return all items in the list. args: none",
    "list_remove": "Remove an item from the list by name. args: item_name:str",
}