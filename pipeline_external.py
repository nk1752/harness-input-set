import yaml

def  hello_world():
  print("Hello external World")

def add_header(pipeline_name: str, project_identifier: str) -> dict:

    pipeline_identifier: str = pipeline_name.replace(" ", "").replace("-", "").lower()

    header = {
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
                        "stages": [],
                    }
                }
            }
        }
    }
    return header

def add_stage(input_set: dict, env: str) -> dict:
    
    bg_name: str = input_set["apBusinessGroupName"].lower()
    client_id = f"account.{bg_name}CicdClientidNp"
    client_secret = f"account.{bg_name}CicdClientsecretNp"

    data_center = "dc12"
    if env == "dev": data_center = "dc12"
    if env == "qaa": data_center = "roc"
    if env == "qab": data_center = "dc12"
    
    policy = "**policy**"

    slaTiersSingleTier = "false"
    if bg_name == "sales": slaTiersSingleTier = "true"

    openshiftProject = f"fgw-{bg_name}-{env}"

    stage = {
        "stage": {
            "identifier": f"{env}",
            "template": {
                "templateInputs": {
                    "type": "Deployment",
                    "variables": [
                        {"name": "apBusinessGroupName", "type": "String", "value": f"{input_set['apBusinessGroupName']}"},
                        {"name": "fgwInstanceName", "type": "String", "value": f"{input_set['fgwInstanceName']}"},
                        {"name": "apiSpecAssetId", "type": "String", "value": f"{input_set['apiSpecAssetId']}"},
                        {"name": "apClientId", "type": "Secret", "value": f"{client_id}"},
                        {"name": "apClientSecret", "type": "Secret", "value": f"{client_secret}"},
                        {"name": "apEnvName", "type": "String", "value": f"{input_set['apEnvName']}"},
                        {"name": "apiSpecAssetVersion", "type": "String", "value": f"{input_set['apiSpecAssetVersion']}"},
                        {"name": "policy", "type": "String", "value": f"{policy}"},
                        {"name": "slaTiersSingleTier", "type": "String", "value": f"{slaTiersSingleTier}"},
                        {"name": "slaTiersBasicMaxReq", "type": "String", "value": "100"},
                        {"name": "slaTiersGoldMaxReq", "type": "String", "value": "100"},
                        {"name": "slaTiersPlatinumMaxReq", "type": "String", "value": "100"},
                        {"name": "slaTiersUnlimitedMaxReq", "type": "String", "value": ""},
                        {"name": "apiEnv", "type": "String", "value": f"{input_set['apiEnv']}"},
                        {"name": "apiVersion", "type": "String", "value": f"{input_set['apiVersion']}"},
                        {"name": "apiLabel", "type": "String", "value": f"{input_set['apiLabel']}"},
                        {"name": "extClientProvider", "type": "String", "value": ""},
                        {"name": "dnsGlobal", "type": "String", "value": f"{input_set['dnsGlobal']}"},
                        {"name": "dnsLocal", "type": "String", "value": f"{input_set['dnsLocal']}"},
                        {"name": "implHost", "type": "String", "value": f"{input_set['implHost']}"},
                        {"name": "implProtocol", "type": "String", "value": f"{input_set['implProtocol']}"},
                        {"name": "implPort", "type": "String", "value": f"{input_set['implPort']}"},
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
                    ],
                    "when": {"condition": "true"},
                }
            },
        }
    }

    return stage

def init_stage(env: str) -> dict:

    stage = {
        "stage": {
            "identifier": f"{env}",
            "template": {
                "templateInputs": {
                    "type": "Deployment",
                    "variables": [
                        {"name": "apBusinessGroupName", "type": "String", "value": ""},
                        {"name": "fgwInstanceName", "type": "String", "value": ""},
                        {"name": "apiSpecAssetId", "type": "String", "value": ""},
                        {"name": "apClientId", "type": "Secret", "value": ""},
                        {"name": "apClientSecret", "type": "Secret", "value": ""},
                        {"name": "apEnvName", "type": "String", "value": ""},
                        {"name": "apiSpecAssetVersion", "type": "String", "value": ""},
                        {"name": "policy", "type": "String", "value": ""},
                        {"name": "slaTiersSingleTier", "type": "String", "value": ""},
                        {"name": "slaTiersBasicMaxReq", "type": "String", "value": "100"},
                        {"name": "slaTiersGoldMaxReq", "type": "String", "value": "100"},
                        {"name": "slaTiersPlatinumMaxReq", "type": "String", "value": "100"},
                        {"name": "slaTiersUnlimitedMaxReq", "type": "String", "value": ""},
                        {"name": "apiEnv", "type": "String", "value": ""},
                        {"name": "apiVersion", "type": "String", "value": ""},
                        {"name": "apiLabel", "type": "String", "value": ""},
                        {"name": "extClientProvider", "type": "String", "value": ""},
                        {"name": "dnsGlobal", "type": "String", "value": ""},
                        {"name": "dnsLocal", "type": "String", "value": ""},
                        {"name": "implHost", "type": "String", "value": ""},
                        {"name": "implProtocol", "type": "String", "value": ""},
                        {"name": "implPort", "type": "String", "value": ""},
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
                    ],
                    "when": {"condition": "true"},
                }
            },
        }
    }

    return stage

def add_approval(env: str) -> dict:

    stage = {
        "stage": {
            "identifier": f"Approval_for_{env}",
            "type": "Approval",
            "spec": {
                "execution": {
                    "steps": [
                        {
                            "step": {
                                "identifier": f"Approval_for_{env}",
                                "type": "HarnessApproval",
                                "spec": {
                                    "approvers": {
                                        "userGroups": [
                                        "account.HARN_API_ADM"
                                        ]
                                    }
                                }
                            }
                        }
                    ]
                    
                }
            }
        }
    }

    return stage


def approval_init(env: str) -> dict:

    stage = {
        "stage": {
            "identifier": f"Approval_for_{env}",
            "type": "Approval",
            "spec": {
                "execution": {
                    "steps": [
                        {
                            "step": {
                                "identifier": f"Approval_for_{env}",
                                "type": "HarnessApproval",
                                "spec": {
                                    "approvers": {
                                        "userGroups": [
                                        "account.HARN_API_ADM"
                                        ]
                                    }
                                }
                            }
                        }
                    ]
                    
                }
            }
        }
    }

    return stage

def closing_approval_init() -> dict:

    stage = {
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
                                }
                            }
                        }
                    ]    
                }
            }
        }
    }

    return stage