def input_data(x_key: str, x_value: str, input_set: list[dict]) -> list[dict]:

    print(f"x_value: {x_value}")
    print(f"x_key: {x_key}")

    filter_set = []
    try:
        for input in input_set:
            target = input[x_key]
            if target == x_value:
                filter_set.append(input)
                #x.pop(x_key)
    except KeyError:
        print(f"KeyError: {x_value} not found in the input_set")

    return filter_set

    return filter_set
