import yaml

def basic_yaml():
    print("Hello from basic_yaml.py")

    test_value = "hello yaml"

    yaml_template = """
    inputSet:
        name: fgw-tmapi-rtp-send-proxy
        tags: {}
        identifier: fgwtmapirtpsendproxy
        orgIdentifier: regionsappdev
        projectIdentifier: ''
        pipeline:
            identifier: Flex_Gateway_Proxy_DeploymentExternal
            template:
                templateInputs:
                    stages:
                    - stage:
                        identifier: devz
                        template:
                            templateInputs:
                            type: Deployment
                            variables:
                                - name: apBusinessGroupName
                                type: String
                                value: Party
                                - name: fgwInstanceName
                                type: String
                                value: fgw-party-dev-z-b-small-1
                                - name: apiSpecAssetId
    """

    data = yaml.safe_load(yaml_template)
    print(data)

    data["inputSet"]["pipeline"]["template"]["template"] = test_value

if __name__ == "__main__":
    basic_yaml()