def apply_filter(filter: str, x_key: str, input_set: list[dict]) -> list[dict]:

    print(f"filter: {filter}")
    print(f"x_key: {x_key}")

    filter_set = []
    try:
        for x in input_set:
            xx = x[x_key]
            if xx == filter:
                filter_set.append(x)
                #x.pop(x_key)
    except KeyError:
        print(f"KeyError: {filter} not found in the input_set")

    return filter_set

def apply_env_filter(filter: str, x_key: str, input_set: list[dict]) -> list[dict]:
    filter_set = []
    for x in input_set:
        if x[x_key] == filter:
            # pop the x_key from the dictionary
            filter_set.append(x)
            #x.pop(x_key)
    
    return filter_set

def apply_harn_filter(filter: str, x_key: str, input_set: list[dict]) -> list[dict]:
    
    #filter_set = [x for x in input_set if x[x_key] == filter]
    filter_set = []
    for x in input_set:
        if x[x_key] == filter:
            # pop the x_key from the dictionary
            filter_set.append(x)
            #x.pop(x_key)
    
    return filter_set