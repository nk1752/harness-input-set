def template_init(pipeline_name: str, project_name: str, env: str) -> dict:

    pipeline_identifier: str = pipeline_name.replace(" ", "").replace("-", "").lower()
    project_identifier: str = project_name.replace(" ", "").replace("-", "").lower()

    if env == "Internal":
        dev = "dev"
        qaa = "qaa"
        qab = "qab"
        proda = "proda"
        prodb = "prodb"
    elif env == "External":
        dev = "devz"
        qaa = "qaza"
        qab = "qazb"
        proda = "prodza"
        prodb = "prodzb"
    else:
        raise ValueError("Invalid type")

    harn = {
        "inputSet": {
            "name": f"{pipeline_name}",
            "tages": {},
            "identifier": f"{pipeline_identifier}",
            "orgIdentifier": "regionsappdev",
            "projectIdentifier": f"{project_identifier}",
            "pipeline": {
                "identifier": f"Flex_Gateway_Proxy_Deployment{env}",
                "template": {
                    "templateInputs": {
                        "stages": [
                            {
                                "stage": {
                                    "identifier": f"{dev}",
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
                                    "identifier": f"{qaa}",
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
                                    "identifier": f"{qab}",
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
                                    "identifier": "Approval_for_prod",
                                    "type": "Approval",
                                    "spec": {
                                        "execution": {
                                            "steps": [
                                                {
                                                    "step": {
                                                        "identifier": "Approval_for_prod",
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
                                    "identifier": f"{proda}",
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
                                    "identifier": f"{prodb}",
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
                                    "identifier": "Closing_Approval",
                                    "type": "Approval",
                                    "spec": {
                                        "execution": {
                                            "steps": [
                                                {
                                                    "step": {
                                                        "identifier": "Closing_Approval",
                                                        "type": "HarnessApproval",
                                                        "spec": {
                                                            "approvers": {
                                                                "userGroups": ""
                                                            }
                                                        },
                                                    }
                                                }
                                            ]
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
    return harn

def stage_init(input_set: dict, stage: str) -> dict:
    parms = {
        "variables": [
            {"name": "apBusinessGroupName", "type": "String", "value": ""},
            {"name": "fgwInstanceName", "type": "String", "value": ""},
            {"name": "apiSpecAssetId", "type": "String", "value": ""},
            {"name": "apClientId", "type": "Secret", "value": ""},
            {"name": "apClientSecret", "type": "Secret", "value": ""},
            {"name": "apEnvName", "type": "String", "value": ""},
            {"name": "apiSpecAssetVersion", "type": "String", "value": "1.0.0"},
            {"name": "policy", "type": "String", "value": ""},
            {"name": "slaTiersSingleTier", "type": "String", "value": ""},
            {"name": "slaTiersBasicMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersGoldMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersPlatinumMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersUnlimitedMaxReq", "type": "String", "value": ""},
            {"name": "apiEnv", "type": "String", "value": "qa"},
            {"name": "apiVersion", "type": "String", "value": "v1"},
            {"name": "apiLabel", "type": "String", "value": ""},
            {"name": "extClientProvider", "type": "String", "value": ""},
            {"name": "dnsGlobal", "type": "String", "value": ""},
            {"name": "dnsLocal", "type": "String", "value": ""},
            {"name": "implHost", "type": "String", "value": ""},
            {"name": "implProtocol", "type": "String", "value": "https"},
            {"name": "implPort", "type": "String", "value": "443"},
            {"name": "implPath", "type": "String", "value": "/"},
            {"name": "implAuthHeader", "type": "String", "value": ""},
            {"name": "implClientId", "type": "Secret", "value": ""},
            {"name": "implClientSecret", "type": "Secret", "value": ""},
            {"name": "implRespTimeout", "type": "String", "value": "30000"},
            {"name": "dataCenter", "type": "String", "value": ""},
            {"name": "fgwTimeout", "type": "String", "value": "30s"},
            {"name": "openshiftProject", "type": "String", "value": ""},
            {"name": "Hostname", "type": "String", "value": '""'},
            {"name": "implTlsSecretGroup", "type": "String", "value": "tls-secret-group"},
            {"name": "implTlsContext", "type": "String", "value": "tls-context"},
        ]
    }

    if stage == "dev":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][0][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "devz":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][0][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "qaa":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][2][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "qaza":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][2][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "qab":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][3][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "qazb":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][3][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "proda":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][5][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "prodza":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][5][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "prodb":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][6][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "prodzb":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][6][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    

    return input_set


    variables = {
        "variables": [
            {"name": "apBusinessGroupName", "type": "String", "value": ""},
            {"name": "fgwInstanceName", "type": "String", "value": ""},
            {"name": "apiSpecAssetId", "type": "String", "value": ""},
            {"name": "apClientId", "type": "Secret", "value": ""},
            {"name": "apClientSecret", "type": "Secret", "value": ""},
            {"name": "apEnvName", "type": "String", "value": ""},
            {"name": "apiSpecAssetVersion", "type": "String", "value": "1.0.0"},
            {"name": "policy", "type": "String", "value": ""},
            {"name": "slaTiersSingleTier", "type": "String", "value": ""},
            {"name": "slaTiersBasicMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersGoldMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersPlatinumMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersUnlimitedMaxReq", "type": "String", "value": ""},
            {"name": "apiEnv", "type": "String", "value": "qa"},
            {"name": "apiVersion", "type": "String", "value": "v1"},
            {"name": "apiLabel", "type": "String", "value": ""},
            {"name": "extClientProvider", "type": "String", "value": ""},
            {"name": "dnsGlobal", "type": "String", "value": ""},
            {"name": "dnsLocal", "type": "String", "value": ""},
            {"name": "implHost", "type": "String", "value": ""},
            {"name": "implProtocol", "type": "String", "value": "https"},
            {"name": "implPort", "type": "String", "value": "443"},
            {"name": "implPath", "type": "String", "value": "/"},
            {"name": "implAuthHeader", "type": "String", "value": ""},
            {"name": "implClientId", "type": "Secret", "value": ""},
            {"name": "implClientSecret", "type": "Secret", "value": ""},
            {"name": "implRespTimeout", "type": "String", "value": "30000"},
            {"name": "dataCenter", "type": "String", "value": ""},
            {"name": "fgwTimeout", "type": "String", "value": "30s"},
            {"name": "openshiftProject", "type": "String", "value": ""},
            {"name": "Hostname", "type": "String", "value": '""'},
            {"name": "implTlsSecretGroup", "type": "String", "value": "tls-secret-group"},
            {"name": "implTlsContext", "type": "String", "value": "tls-context"},
        ]
    }

    if stage == "devz":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][0][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(variables)
    elif stage == "qaza":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][2][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(variables)
    elif stage == "qazb":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][3][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(variables)
    elif stage == "prodza":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][5][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(variables)
    elif stage == "prodzb":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][6][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(variables)

    return input_set

def stage_update(input_set: dict, variable: dict, stage: str) -> dict:

    bg_name: str = variable["apBusinessGroupName"].lower()
    client_id = f"account.{bg_name}CicdClientidNp"
    client_secret = f"account.{bg_name}CicdClientsecretNp"

    data_center = "dc12"
    if stage == "dev": data_center = "dc12"
    if stage == "qaa": data_center = "roc"
    if stage == "qab": data_center = "dc12"
    
    policy = "**policy**"

    slaTiersSingleTier = "false"
    if bg_name == "sales": slaTiersSingleTier = "true"

    openshiftProject = f"fgw-{bg_name}-{stage}"

    parms = {
        "variables": [
            {"name": "apBusinessGroupName", "type": "String", "value": f"{variable['apBusinessGroupName']}"},
            {"name": "fgwInstanceName", "type": "String", "value": f"{variable['fgwInstanceName']}"},
            {"name": "apiSpecAssetId", "type": "String", "value": f"{variable['apiSpecAssetId']}"},
            {"name": "apClientId", "type": "Secret", "value": f"{client_id}"},
            {"name": "apClientSecret", "type": "Secret", "value": f"{client_secret}"},
            {"name": "apEnvName", "type": "String", "value": f"{variable['apEnvName']}"},
            {"name": "apiSpecAssetVersion", "type": "String", "value": f"{variable['apiSpecAssetVersion']}"},
            {"name": "policy", "type": "String", "value": f"{policy}"},
            {"name": "slaTiersSingleTier", "type": "String", "value": f"{slaTiersSingleTier}"},
            {"name": "slaTiersBasicMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersGoldMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersPlatinumMaxReq", "type": "String", "value": "100"},
            {"name": "slaTiersUnlimitedMaxReq", "type": "String", "value": ""},
            {"name": "apiEnv", "type": "String", "value": f"{variable['apiEnv']}"},
            {"name": "apiVersion", "type": "String", "value": f"{variable['apiVersion']}"},
            {"name": "apiLabel", "type": "String", "value": f"{variable['apiLabel']}"},
            {"name": "extClientProvider", "type": "String", "value": ""},
            {"name": "dnsGlobal", "type": "String", "value": f"{variable['dnsGlobal']}"},
            {"name": "dnsLocal", "type": "String", "value": f"{variable['dnsLocal']}"},
            {"name": "implHost", "type": "String", "value": f"{variable['implHost']}"},
            {"name": "implProtocol", "type": "String", "value": f"{variable['implProtocol']}"},
            {"name": "implPort", "type": "String", "value": f"{variable['implPort']}"},
            {"name": "implPath", "type": "String", "value": "/"},
            {"name": "implAuthHeader", "type": "String", "value": f"myAuthHeader"},
            {"name": "implClientId", "type": "Secret", "value": f"myImplClientId"},
            {"name": "implClientSecret", "type": "Secret", "value": f"myImplClientSecret"},
            {"name": "implRespTimeout", "type": "String", "value": "30000"},
            {"name": "dataCenter", "type": "String", "value": f"{data_center}"},
            {"name": "fgwTimeout", "type": "String", "value": "30s"},
            {"name": "openshiftProject", "type": "String", "value": f"{openshiftProject}"},
            {"name": "Hostname", "type": "String", "value": '""'},
            {"name": "implTlsSecretGroup", "type": "String", "value": "tls-secret-group"},
            {"name": "implTlsContext", "type": "String", "value": "tls-context"},
        ]
    }

    if stage == "dev":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][0][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "qaa":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][2][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "qab":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][3][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "proda":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][5][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "prodb":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][6][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    if stage == "devz":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][0][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "qaza":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][2][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "qazb":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][3][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "prodza":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][5][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)
    elif stage == "prodzb":
        input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][6][
            "stage"
        ]["template"]["templateInputs"]["variables"].append(parms)

    return input_set

def filter(x_key: str, x_value: str, input_set: list[dict]) -> list[dict]:

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

def header_init(pipeline_name: str,project_identifier: str) -> dict:

    pipeline_identifier: str = pipeline_name.replace(" ", "").replace("-", "").lower()

    header = {
        "inputSet": {
            "name": f"{pipeline_name}",
            "tages": {},
            "identifier": f"{pipeline_identifier}",
            "orgIdentifier": "regionsappdev",
            "projectIdentifier": f"{project_identifier}",
            "pipeline": {
                "identifier": "Flex_Gateway_Proxy_Deployment",
                "template": {
                    "templateInputs": {
                        "stages": [
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
                                    "identifier": "Approval_for_prod",
                                    "type": "Approval",
                                    "spec": {
                                        "execution": {
                                            "steps": [
                                                {
                                                    "step": {
                                                        "identifier": "Approval_for_prod",
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
                                    "identifier": "Closing_Approval",
                                    "type": "Approval",
                                    "spec": {
                                        "execution": {
                                            "steps": [
                                                {
                                                    "step": {
                                                        "identifier": "Closing_Approval",
                                                        "type": "HarnessApproval",
                                                        "spec": {
                                                            "approvers": {
                                                                "userGroups": ""
                                                            }
                                                        },
                                                    }
                                                }
                                            ]
                                        }
                                    },
                                }
                            },
                            

                        ]
                    }
                }
            }
        }
    }
    return header