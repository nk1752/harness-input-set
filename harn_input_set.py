import csv
import json

def build_input_set(dev_input: dict, qa_input: dict) -> dict:

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
                                                    "value": f"{dev_input['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{dev_input['fgwInstanceName']}",
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
                                                    "value": f"{qa_input['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{qa_input['fgwInstanceName']}",
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
                                                    "value": f"{qa_input['apBusinessGroupName']}",
                                                },
                                                {
                                                    "name": "fgwInstanceName",
                                                    "type": "String",
                                                    "value": f"{qa_input['fgwInstanceName']}",
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
    
