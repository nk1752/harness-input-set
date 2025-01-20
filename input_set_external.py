def template_init(pipeline_name: str, project_name: str) -> dict:

    pipeline_identifier: str = pipeline_name.replace(" ", "").replace("-", "").lower()
    project_identifier: str = project_name.replace(" ", "").replace("-", "").lower()

    harn = {
        "inputSet": {
            "name": f"{pipeline_name}",
            "tages": {},
            "identifier": f"{pipeline_identifier}",
            "orgIdentifier": "regionsappdev",
            "projectIdentifier": f"{project_identifier}",
            "pipeline": {
                "identifier": "Flex_Gateway_Proxy_DeploymentExternal",
                "template": {
                    "templateInputs": {
                        "stages": [
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
                                    "identifier": "qaza",
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
                                    "identifier": "qazb",
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
                                    "identifier": "prodza",
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
                                    "identifier": "prodzb",
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
