# Description: This script creates a dictionary and adds a stage section to it.
import yaml

import pipeline_internal


def main():
    
    input_set: dict = {}

    # Create a dictionary
    header = {
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
                        "stages": [],
                    },
                },
            },
        },
    }

    # build stage section
    stage = "dev"
    dev = {
        "stage": {
            "identifier": f"{stage}",
            "template": {
                "templateInputs": {
                    "type": "Deployment",
                    "variables": [
                        {
                            "name": "apBusinessGroupName",
                            "type": "String",
                            "value": "Party",
                        },
                        {
                            "name": "fgwInstanceName",
                            "type": "String",
                            "value": "fgw-party-dev-z-b-small-1",
                        },
                    ],
                },
            },
        },
    }

    stage = "qa"
    qa = {
        "stage": {
            "identifier": f"{stage}",
            "template": {
                "templateInputs": {
                    "type": "Deployment",
                    "variables": [
                        {
                            "name": "apBusinessGroupName",
                            "type": "String",
                            "value": "Party",
                        },
                        {
                            "name": "fgwInstanceName",
                            "type": "String",
                            "value": "fgw-party-dev-z-b-small-1",
                        },
                    ],
                },
            },
        },
    }

    # Add a stage section to the input_set
    input_set.update(header)
    input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][0].append(qa)
    input_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"][1].append(dev)

    print(yaml.dump(input_set, default_flow_style=False, sort_keys=False))


if __name__ == "__main__":
    main()
