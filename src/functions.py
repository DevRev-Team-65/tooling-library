devrev_functions = [
    {
        "name": "works_list",
        "description": "Returns a list of work items matching the request.",
        "parameters": {
            "type": "object",
            "properties": {
                "applies_to_part": {
                    "title": "applies_to_part",
                    "type": "array of strings",
                    "description": "Filters for work belonging to any of the provided parts."
                },
                "created_by": {
                    "title": "created_by",
                    "type": "array of strings",
                    "description": "Filters for work created by any of these users."
                },
                "issue.priority": {
                    "title": "issue.priority",
                    "type": ["P0", "P1", "P2", "P3"],
                    "description": "Filters for issues with any of the provided priorities. Allowed values: p0, p1, p2, p3."
                },
                "issue.rev_orgs": {
                    "title": "issue.rev_orgs",
                    "type": "array of strings",
                    "description": "Filters for issues with any of the provided Rev organizations."
                },
                "limit": {
                    "title": "limit",
                    "type": "integer (int32)",
                    "description": "The maximum number of works to return. The default is '50'."
                },
                "owned_by": {
                    "title": "owned_by",
                    "type": "array of strings",
                    "description": "Filters for work owned by any of these users."
                },
                "stage.name": {
                    "title": "stage.name",
                    "type": "array of strings",
                    "description": "Filters for records in the provided stage(s) by name."
                },
                "ticket.needs_response": {
                    "title": "ticket.needs_response",
                    "type": "boolean",
                    "description": "Filters for tickets that need a response."
                },
                "ticket.rev_org": {
                    "title": "ticket.rev_org",
                    "type": "array of strings",
                    "description": "Filters for tickets associated with any of the provided Rev organizations."
                },
                "ticket.severity": {
                    "title": "ticket.severity",
                    "type": "array of strings",
                    "description": "Filters for tickets with any of the provided severities. Allowed values: blocker, high, low, medium."
                },
                "ticket.source_channel": {
                    "title": "ticket.source_channel",
                    "type": "array of strings",
                    "description": "Filters for tickets with any of the provided source channels."
                },
                "type": {
                    "title": "type",
                    "type": "array of strings",
                    "description": "Filters for work of the provided types. Allowed values: issue, ticket, task."
                }
            },
            "required": []
        }
    },
    {
        "name": "summarize_objects",
        "description": "Summarizes a list of objects. The logic of how to summarize a particular object type is an internal implementation detail.",
        "parameters": {
            "type": "object",
            "properties": {
                "objects": {
                    "title": "objects",
                    "type": "array of objects",
                    "description": "List of objects to summarize."
                }
            },
            "required": []
        }
    },
    {
        "name": "prioritize_objects",
        "description": "Returns a list of objects sorted by priority. The logic of what constitutes priority for a given object is an internal implementation detail.",
        "parameters": {
            "type": "object",
            "properties": {
                "objects": {
                    "title": "objects",
                    "type": "array of objects",
                    "description": "A list of objects to be prioritized."
                }
            },
            "required": []
        }
    },
    {
        "name": "add_work_items_to_sprint",
        "description": "Adds the given work items to the sprint.",
        "parameters": {
            "type": "object",
            "properties": {
                "work_ids": {
                    "title": "work_ids",
                    "type": "array of strings",
                    "description": "A list of work item IDs to be added to the sprint."
                },
                "sprint_id": {
                    "title": "sprint_id",
                    "type": "str",
                    "description": "The ID of the sprint to which the work items should be added."
                }
            },
            "required": []
        }
    },
    {
        "name": "get_sprint_id",
        "description": "Returns the ID of the current sprint.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "get_similar_work_items",
        "description": "Returns a list of work items that are similar to the given work item.",
        "parameters": {
            "type": "object",
            "properties": {
                "work_id": {
                    "title": "work_id",
                    "type": "string",
                    "description": "The ID of the work item for which you want to find similar items."
                }
            },
            "required": []
        }
    },
    {
        "name": "search_object_by_name",
        "description": "Given a search string, returns the ID of a matching object in the system of record. If multiple matches are found, it returns the one where the confidence is highest.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "title": "query",
                    "type": "string",
                    "description": "The search string, could be for example customer’s name, part name, user name."
                }
            },
            "required": []
        }
    },
    {
        "name": "create_actionable_tasks_from_text",
        "description": "Given a text, extracts actionable insights, and creates tasks for them, which are kind of a work item.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "title": "text",
                    "type": "string",
                    "description": "The text from which the actionable insights need to be created."
                }
            },
            "required": []
        }
    },
    {
        "name": "who_am_i",
        "description": "Returns the ID of the current user.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },

    # bonus points functions

    {
        "name": "equal_to",
        "description": "Checks if two values are equal.",
        "parameters": {
            "type": "object",
            "properties": {
                "left_value": {
                    "title": "left_value",
                    "type": "string",
                    "description": "The left-hand side value for comparison."
                },
                "right_value": {
                    "title": "right_value",
                    "type": "string",
                    "description": "The right-hand side value for comparison."
                }
            },
            "required": ["left_value", "right_value"]
        }
    },


    {
        "name": "logical_and",
        "description": "Performs a logical AND operation on two conditions.",
        "parameters": {
            "type": "object",
            "properties": {
                "condition1": {
                    "title": "condition1",
                    "type": "boolean",
                    "description": "The first condition for the logical AND operation."
                },
                "condition2": {
                    "title": "condition2",
                    "type": "boolean",
                    "description": "The second condition for the logical AND operation."
                }
            },
            "required": []
        }
    },

    {
        "name": "logical_or",
        "description": "Performs a logical OR operation on two conditions.",
        "parameters": {
            "type": "object",
            "properties": {
                "condition1": {
                    "title": "condition1",
                    "type": "boolean",
                    "description": "The first condition for the logical OR operation."
                },
                "condition2": {
                    "title": "condition2",
                    "type": "boolean",
                    "description": "The second condition for the logical OR operation."
                }
            },
            "required": []
        }
    },


    {
        "name": "logical_not",
        "description": "Performs a logical NOT operation on a condition.",
        "parameters": {
            "type": "object",
            "properties": {
                "condition": {
                    "title": "condition",
                    "type": "boolean",
                    "description": "The condition to negate using logical NOT."
                }
            },
            "required": []
        }
    },


    {
        "name": "Lesser_than",
        "description": "Checks if the left value is lesser than the right value.",
        "parameters": {
            "type": "object",
            "properties": {
                "left_value": {
                    "title": "left_value",
                    "type": "number",
                    "description": "The left-hand side value for comparison."
                },
                "right_value": {
                    "title": "right_value",
                    "type": "number",
                    "description": "The right-hand side value for comparison."
                }
            },
            "required": []
        }
    },

    {
        "name": "Greater_than",
        "description": "Checks if the left value is greater than the right value.",
        "parameters": {
            "type": "object",
            "properties": {
                "left_value": {
                    "title": "left_value",
                    "type": "number",
                    "description": "The left-hand side value for comparison."
                },
                "right_value": {
                    "title": "right_value",
                    "type": "number",
                    "description": "The right-hand side value for comparison."
                }
            },
            "required": []
        }
    },

    {
        "name": "Equal_to",
        "description": "Checks if the left value is equal to the right value.",
        "parameters": {
            "type": "object",
            "properties": {
                "left_value": {
                    "title": "left_value",
                    "type": "number",
                    "description": "The left-hand side value for comparison."
                },
                "right_value": {
                    "title": "right_value",
                    "type": "number",
                    "description": "The right-hand side value for comparison."
                }
            },
            "required": []
        }
    },


    {
        "name": "resolution_status",
        "description": "Gives an array of only unresolved issues",
        "parameters": {
            "type": "object",
            "properties": {
                "unresolved_issue": {
                    "title": "unresolved_issue",
                    "type": "array",
                    "description": "An array of only unresolved issues."
                }
            },
            "required": []
        }
    },

    {
        "name": "length",
        "description": "Returns the length of an array.",
        "parameters": {
            "type": "object",
            "properties": {
                "array": {
                    "title": "array",
                    "type": "array",
                    "description": "The array for which to determine the length."
                }
            },
            "required": []
        }
    },

    {
        "name": "if_else_condition",
        "description": "Executes a conditional statement with if-else logic.",
        "parameters": {
            "type": "object",
            "properties": {
                "Function": {
                    "title": "Function",
                    "type": "string",
                    "description": "The conditional function or expression.",
                },
                "If_true": {
                    "title": "If_true",
                    "type": "string",
                    "description": "Action to be taken if the condition is true.",
                },
                "If_false": {
                    "title": "If_false",
                    "type": "string",
                    "description": "Action to be taken if the condition is false.",
                }
            },
            "required": []
        }
    },

    {
        "name": "loop_condition",
        "description": "Executes a loop for a specified number of repetitions.",
        "parameters": {
            "type": "object",
            "properties": {
                "Repetitions": {
                    "title": "Repetitions",
                    "type": "integer",
                    "description": "The number of repetitions for the loop.",
                },
                "Go_to": {
                    "title": "Go_to",
                    "type": "string",
                    "description": "The target location or action to jump to after each iteration.",
                }
            },
            "required": []
        }
    }
]
