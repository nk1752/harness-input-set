import csv
import json

def build_internal(dev_b: dict, qa_a: dict, qa_b: dict) -> dict:

    print(" ********* strat build_input_set ********* ")


    data = {
        "inputSet": {
            "name": "fgw-tmapi-rtp-send-proxy",
            "tags": {},
            "identifier": "fgwtmapirtpsendproxy",
            "orgIdentifier": "regionsappdev",
            "projectIdentifier": "treasurymanagementapis",
            "pipeline": {
                "identifier": "Flex_Gateway_Proxy_DeploymentInternal",
                "template": {
                    "templateInputs": {
                        "stages": [
                            {
                                "stage": {
                                    "identifier": "dev",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [
                                                {
                                                    "name": "apBusinessGroupName",
                                                    "type": "String",
                                                    "value": f"{dev_b['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{dev_b['fgwInstanceName']}",
                                                },
                                            ],
                                        },
                                    },
                                },
                            },
                            {
                                "stage": {
                                    "identifier": "qaa",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [
                                                {
                                                    "name": "apBusinessGroupName",
                                                    "type": "String",
                                                    "value": f"{qa_a['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{qa_a['fgwInstanceName']}",
                                                },
                                            ],
                                        },
                                    },
                                },
                            },
                            {
                                "stage": {
                                    "identifier": "qab",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [
                                                {
                                                    "name": "apBusinessGroupName",
                                                    "type": "String",
                                                    "value": f"{qa_b['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{qa_b['fgwInstanceName']}",
                                                },
                                            ],
                                        },
                                    },
                                },
                            }
                        ],
                    },
                },
            },
        },
    }
                            
    return data

def build_extrernal(dev_z_b: dict, qa_z_a: dict, qa_z_b: dict) -> dict:

    print(" ********* strat build_input_set ********* ")


    data = {
        "inputSet": {
            "name": "fgw-tmapi-rtp-send-proxy",
            "tags": {},
            "identifier": "fgwtmapirtpsendproxy",
            "orgIdentifier": "regionsappdev",
            "projectIdentifier": "treasurymanagementapis",
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
                                            "variables": [
                                                {
                                                    "name": "apBusinessGroupName",
                                                    "type": "String",
                                                    "value": f"{dev_z_b['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{dev_z_b['fgwInstanceName']}",
                                                },
                                            ],
                                        },
                                    },
                                },
                            },
                            {
                                "stage": {
                                    "identifier": "qaza",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [
                                                {
                                                    "name": "apBusinessGroupName",
                                                    "type": "String",
                                                    "value": f"{qa_z_a['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{qa_z_a['fgwInstanceName']}",
                                                },
                                            ],
                                        },
                                    },
                                },
                            },
                            {
                                "stage": {
                                    "identifier": "qazb",
                                    "template": {
                                        "templateInputs": {
                                            "type": "Deployment",
                                            "variables": [
                                                {
                                                    "name": "apBusinessGroupName",
                                                    "type": "String",
                                                    "value": f"{qa_z_b['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{qa_z_b['fgwInstanceName']}",
                                                },
                                            ],
                                        },
                                    },
                                },
                            }
                        ],
                    },
                },
            },
        },
    }
                            
    return data
    
