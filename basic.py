import yaml


def basic():

    person: dict = {}
    person = {"name": "Alice", "age": 25}
    print(person)  # {'name': 'Alice', 'age': 25}

    new_person = {"name": "Nadeem", "age": 58}
    person.update(new_person)  # Adds 'city' and updates 'age'
    print(person)  # {'name': 'Nadeem', 'age': 58}

    harn = {
        "inputSet": {
            "name": "",
            "tages": {},
            "orgIdentifier": "regionsappdev",
            "projectIdentifier": "treasurymanagementapis",
            "pipeline": {
                "identifier": "Flex_Gateway_Proxy_DeploymentExternal",
                "template": {
                    "templateInputs": {
                        "stages": [
                            {
                                "stage": {
                                    "identifier": "dev",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [],
                                            "when": {"condition": "true"},
                                        }
                                    },
                                }
                            },
                            {
                                "stage": {
                                    "identifier": "devz",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [],
                                            "when": {"condition": "true"},
                                        }
                                    },
                                }
                            },
                            {
                                "stage": {
                                    "identifier": "Approval_for_qa",
                                    "type": "Approval",
                                    "spec": {
                                        "execution": {
                                            "steps": [
                                                {
                                                    "step": {
                                                        "identifier": "Approval_for_qa",
                                                        "type": "HarnessApproval",
                                                        "spec": {
                                                            "approvers": {
                                                                "userGroups": [
                                                                    "account.HARN_API_ADM"
                                                                ]
                                                            }
                                                        },
                                                    }
                                                }
                                            ]
                                        }
                                    },
                                }
                            },
                            {
                                "stage": {
                                    "identifier": "qaa",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [],
                                            "when": {"condition": "true"},
                                        }
                                    },
                                }
                            },
                            {
                                "stage": {
                                    "identifier": "qab",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [],
                                            "when": {"condition": "true"},
                                        }
                                    },
                                }
                            },
                            {
                                "stage": {
                                    "identifier": "proda",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [],
                                            "when": {"condition": "true"},
                                        }
                                    },
                                }
                            },
                            {
                                "stage": {
                                    "identifier": "prodb",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [],
                                            "when": {"condition": "true"},
                                        }
                                    },
                                }
                            },
                        ]
                    }
                },
            },
        }
    }

    variable = {"name": "apBusinessGroupName", "type": "String", "value": "Nadeem"}

    # append variable to variables in harn
    harn["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][0]["stage"][
        "template"
    ]["templateInputs"]["variables"].append(variable)

    input_set = yaml.dump(harn, default_flow_style=False, sort_keys=False)
    print(input_set)


if __name__ == "__main__":
    basic()
