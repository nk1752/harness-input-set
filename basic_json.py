def basic():
    print("Hello from basic.py")

    template = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "variables": [
            {
                "name": "apBusinessGroupName",
                "type": "String",
                "value": "Party"
            },
            {
                "name": "fgwInstanceName",
                "type": "String",
                "value": "fgw-party-dev-z-b-small-1",
            },
        ],
        "extra": "extra",
    }

    # find all keys in template
    # find all keys in input_set
    # if key exists in input_set, update template with input_set value
    # if key does not exist in input_set, do nothing

    for key in template["variables"]:
        print(key)
    

    input_set = {"name": "apBusinessGroupName", "type": "String", "value": "Alabama"}

    for key in template:
        print(key)
        target_key = key
        if target_key in input_set:
            print("Key exists in input_set")
            template[f"{target_key}"] = input_set[f"{target_key}"]

        else:
            print("Key does not exist in input_set")

    print(template)


if __name__ == "__main__":
    basic()
