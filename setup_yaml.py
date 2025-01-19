import yaml

def setup_yaml() -> dict:
  yaml_data = """
    inputSet:
      name: "sample name"
      tags: {}
      identifier: fgwtmapirtpsendproxy
      orgIdentifier: regionsappdev
      projectIdentifier: treasurymanagementapis
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
                          value: "bg name"
                        - name: fgwInstanceName
                          type: String
                          value: "fgw instance name"

  """
  data = yaml.safe_load(yaml_data)

  return data