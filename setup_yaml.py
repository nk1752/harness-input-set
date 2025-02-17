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


def setup_stage(identifier: str) -> dict:
    print(f"********* setup_stage *********")
    print(f"identifier: {identifier}")

    stage_data = {
        
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
                        "value": "Party"
                      },
                      {
                        "name": "fgwInstanceName",
                        "type": "String",
                        "value": "fgw-party-dev-z-b-small-1"
                      },
                      {
                        "name": "apiSpecAssetId",
                        "type": "String",
                        "value": " tmapi-rtp-send-proxy"
                      },
                      {
                        "name": "apClientId",
                        "type": "Secret",
                        "value": "account.partyCicdClientidNp"
                      },
                      {
                        "name": "apClientSecret",
                        "type": "Secret",
                        "value": "account.partyCicdClientsecretNp"
                      },
                      {
                        "name": "apEnvName",
                        "type": "String",
                        "value": "Dev"
                      },
                      {
                        "name": "apiSpecAssetVersion",
                        "type": "String",
                        "value": "1.0.0"
                      },
                      {
                        "name": "policy",
                        "type": "String",
                        "value": "sla"
                      },
                      {
                        "name": "slaTiersSingleTier",
                        "type": "String",
                        "value": "false"
                      },
                      {
                        "name": "slaTiersBasicMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersGoldMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersPlatinumMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersUnlimitedMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiEnv",
                        "type": "String",
                        "value": "dev"
                      },
                      {
                        "name": "apiVersion",
                        "type": "String",
                        "value": "v1"
                      },
                      {
                        "name": "apiLabel",
                        "type": "String",
                        "value": " tmapi-rtp-send-proxy-fgw-dev-b"
                      },
                      {
                        "name": "extClientProvider",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dnsGlobal",
                        "type": "String",
                        "value": "api.regionstest.com"
                      },
                      {
                        "name": "dnsLocal",
                        "type": "String",
                        "value": "api.regionstest.com"
                      },
                      {
                        "name": "implHost",
                        "type": "String",
                        "value": "tmapi-client-endpoints-dev.apps.np-b.openshift.rgbk.com"
                      },
                      {
                        "name": "implProtocol",
                        "type": "String",
                        "value": "https"
                      },
                      {
                        "name": "implPort",
                        "type": "String",
                        "value": "443"
                      },
                      {
                        "name": "implPath",
                        "type": "String",
                        "value": "/"
                      },
                      {
                        "name": "implAuthHeader",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implClientId",
                        "type": "Secret",
                        "value": "org.tmapiRtpSendProxyClientIdDev"
                      },
                      {
                        "name": "implClientSecret",
                        "type": "Secret",
                        "value": "org.tmapiRtpSendProxyClientSecretDev"
                      },
                      {
                        "name": "implRespTimeout",
                        "type": "String",
                        "value": "30000"
                      },
                      {
                        "name": "dataCenter",
                        "type": "String",
                        "value": "dc12"
                      },
                      {
                        "name": "fgwTimeout",
                        "type": "String",
                        "value": "30s"
                      },
                      {
                        "name": "openshiftProject",
                        "type": "String",
                        "value": "fgw-party-dev"
                      },
                      {
                        "name": "Hostname",
                        "type": "String",
                        "value": "\"\""
                      },
                      {
                        "name": "implTlsSecretGroup",
                        "type": "String",
                        "value": "tls-secret-group"
                      },
                      {
                        "name": "implTlsContext",
                        "type": "String",
                        "value": "tls-context"
                      }
                    ],
                    "when": {
                      "condition": "true"
                    }
                  }
                }
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
                          }
                        }
                      }
                    ]
                  }
                }
              }
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
                        "value": "Party"
                      },
                      {
                        "name": "fgwInstanceName",
                        "type": "String",
                        "value": "fgw-party-np-z-a-small-1"
                      },
                      {
                        "name": "apiSpecAssetId",
                        "type": "String",
                        "value": " tmapi-rtp-send-proxy"
                      },
                      {
                        "name": "apClientId",
                        "type": "Secret",
                        "value": "account.partyCicdClientidNp"
                      },
                      {
                        "name": "apClientSecret",
                        "type": "Secret",
                        "value": "account.partyCicdClientsecretNp"
                      },
                      {
                        "name": "apEnvName",
                        "type": "String",
                        "value": "QA"
                      },
                      {
                        "name": "apiSpecAssetVersion",
                        "type": "String",
                        "value": "1.0.0"
                      },
                      {
                        "name": "policy",
                        "type": "String",
                        "value": "sla"
                      },
                      {
                        "name": "slaTiersSingleTier",
                        "type": "String",
                        "value": "false"
                      },
                      {
                        "name": "slaTiersBasicMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersGoldMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersPlatinumMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersUnlimitedMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiEnv",
                        "type": "String",
                        "value": "qa"
                      },
                      {
                        "name": "apiVersion",
                        "type": "String",
                        "value": "v1"
                      },
                      {
                        "name": "apiLabel",
                        "type": "String",
                        "value": " tmapi-rtp-send-proxy-fgw-qa-a"
                      },
                      {
                        "name": "extClientProvider",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dnsGlobal",
                        "type": "String",
                        "value": "api.regionstest.com"
                      },
                      {
                        "name": "dnsLocal",
                        "type": "String",
                        "value": "api.regionstest.com"
                      },
                      {
                        "name": "implHost",
                        "type": "String",
                        "value": "tmapi-client-endpoints-qa.apps.np-b.openshift.rgbk.com"
                      },
                      {
                        "name": "implProtocol",
                        "type": "String",
                        "value": "https"
                      },
                      {
                        "name": "implPort",
                        "type": "String",
                        "value": "443"
                      },
                      {
                        "name": "implPath",
                        "type": "String",
                        "value": "/"
                      },
                      {
                        "name": "implAuthHeader",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implClientId",
                        "type": "Secret",
                        "value": "org.partyCicdClientidNp"
                      },
                      {
                        "name": "implClientSecret",
                        "type": "Secret",
                        "value": "org.partyCicdClientsecretNp"
                      },
                      {
                        "name": "implRespTimeout",
                        "type": "String",
                        "value": "30000"
                      },
                      {
                        "name": "dataCenter",
                        "type": "String",
                        "value": "roc"
                      },
                      {
                        "name": "fgwTimeout",
                        "type": "String",
                        "value": "30s"
                      },
                      {
                        "name": "openshiftProject",
                        "type": "String",
                        "value": "fgw-party-qa"
                      },
                      {
                        "name": "Hostname",
                        "type": "String",
                        "value": "\"\""
                      },
                      {
                        "name": "implTlsSecretGroup",
                        "type": "String",
                        "value": "tls-secret-group"
                      },
                      {
                        "name": "implTlsContext",
                        "type": "String",
                        "value": "tls-context"
                      }
                    ],
                    "when": {
                      "condition": "true"
                    }
                  }
                }
              }
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
                        "value": "Party"
                      },
                      {
                        "name": "fgwInstanceName",
                        "type": "String",
                        "value": "fgw-party-np-z-b-small-1"
                      },
                      {
                        "name": "apiSpecAssetId",
                        "type": "String",
                        "value": " tmapi-rtp-send-proxy"
                      },
                      {
                        "name": "apClientId",
                        "type": "Secret",
                        "value": "account.partyCicdClientidNp"
                      },
                      {
                        "name": "apClientSecret",
                        "type": "Secret",
                        "value": "account.partyCicdClientsecretNp"
                      },
                      {
                        "name": "apEnvName",
                        "type": "String",
                        "value": "QA"
                      },
                      {
                        "name": "apiSpecAssetVersion",
                        "type": "String",
                        "value": "1.0.0"
                      },
                      {
                        "name": "policy",
                        "type": "String",
                        "value": "sla"
                      },
                      {
                        "name": "slaTiersSingleTier",
                        "type": "String",
                        "value": "false"
                      },
                      {
                        "name": "slaTiersBasicMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersGoldMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersPlatinumMaxReq",
                        "type": "String",
                        "value": "100"
                      },
                      {
                        "name": "slaTiersUnlimitedMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiEnv",
                        "type": "String",
                        "value": "qa"
                      },
                      {
                        "name": "apiVersion",
                        "type": "String",
                        "value": "v1"
                      },
                      {
                        "name": "apiLabel",
                        "type": "String",
                        "value": " tmapi-rtp-send-proxy-fgw-qa-b"
                      },
                      {
                        "name": "extClientProvider",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dnsGlobal",
                        "type": "String",
                        "value": "api.regionstest.com"
                      },
                      {
                        "name": "dnsLocal",
                        "type": "String",
                        "value": "api.regionstest.com"
                      },
                      {
                        "name": "implHost",
                        "type": "String",
                        "value": "tmapi-client-endpoints-qa.apps.np-b.openshift.rgbk.com"
                      },
                      {
                        "name": "implProtocol",
                        "type": "String",
                        "value": "https"
                      },
                      {
                        "name": "implPort",
                        "type": "String",
                        "value": "443"
                      },
                      {
                        "name": "implPath",
                        "type": "String",
                        "value": "/"
                      },
                      {
                        "name": "implAuthHeader",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implClientId",
                        "type": "Secret",
                        "value": "org.tmapiRtpSendProxyClientIdDev"
                      },
                      {
                        "name": "implClientSecret",
                        "type": "Secret",
                        "value": "org.tmapiRtpSendProxyClientSecretDev"
                      },
                      {
                        "name": "implRespTimeout",
                        "type": "String",
                        "value": "30000"
                      },
                      {
                        "name": "dataCenter",
                        "type": "String",
                        "value": "dc12"
                      },
                      {
                        "name": "fgwTimeout",
                        "type": "String",
                        "value": "30s"
                      },
                      {
                        "name": "openshiftProject",
                        "type": "String",
                        "value": "fgw-party-qa"
                      },
                      {
                        "name": "Hostname",
                        "type": "String",
                        "value": "\"\""
                      },
                      {
                        "name": "implTlsSecretGroup",
                        "type": "String",
                        "value": "tls-secret-group"
                      },
                      {
                        "name": "implTlsContext",
                        "type": "String",
                        "value": "tls-context"
                      }
                    ],
                    "when": {
                      "condition": "true"
                    }
                  }
                }
              }
            },
            {
              "stage": {
                "identifier": "GoNoGo_Approval",
                "type": "Approval",
                "spec": {
                  "execution": {
                    "steps": [
                      {
                        "step": {
                          "identifier": "GoNoGo_Approval",
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
            },
            {
              "stage": {
                "identifier": "prodza",
                "template": {
                  "templateInputs": {
                    "type": "Deployment",
                    "variables": [
                      {
                        "name": "apBusinessGroupName",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "fgwInstanceName",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiSpecAssetId",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apClientId",
                        "type": "Secret",
                        "value": ""
                      },
                      {
                        "name": "apClientSecret",
                        "type": "Secret",
                        "value": ""
                      },
                      {
                        "name": "apEnvName",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiSpecAssetVersion",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "policy",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersSingleTier",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersBasicMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersGoldMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersPlatinumMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersUnlimitedMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiEnv",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiVersion",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiLabel",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "extClientProvider",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dnsGlobal",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dnsLocal",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implHost",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implProtocol",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implPort",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implPath",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implAuthHeader",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implClientId",
                        "type": "Secret",
                        "value": ""
                      },
                      {
                        "name": "implClientSecret",
                        "type": "Secret",
                        "value": ""
                      },
                      {
                        "name": "implRespTimeout",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dataCenter",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "fgwTimeout",
                        "type": "String",
                        "value": "30s"
                      },
                      {
                        "name": "openshiftProject",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "Hostname",
                        "type": "String",
                        "value": "\"\""
                      },
                      {
                        "name": "implTlsSecretGroup",
                        "type": "String",
                        "value": "tls-secret-group"
                      },
                      {
                        "name": "implTlsContext",
                        "type": "String",
                        "value": "tls-context"
                      }
                    ],
                    "when": {
                      "condition": false
                    }
                  }
                }
              }
            },
            {
              "stage": {
                "identifier": "prodzb",
                "template": {
                  "templateInputs": {
                    "type": "Deployment",
                    "variables": [
                      {
                        "name": "apBusinessGroupName",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "fgwInstanceName",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiSpecAssetId",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apClientId",
                        "type": "Secret",
                        "value": ""
                      },
                      {
                        "name": "apClientSecret",
                        "type": "Secret",
                        "value": ""
                      },
                      {
                        "name": "apEnvName",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiSpecAssetVersion",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "policy",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersSingleTier",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersBasicMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersGoldMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersPlatinumMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "slaTiersUnlimitedMaxReq",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiEnv",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiVersion",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "apiLabel",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "extClientProvider",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dnsGlobal",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dnsLocal",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implHost",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implProtocol",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implPort",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implPath",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implAuthHeader",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "implClientId",
                        "type": "Secret",
                        "value": ""
                      },
                      {
                        "name": "implClientSecret",
                        "type": "Secret",
                        "value": ""
                      },
                      {
                        "name": "implRespTimeout",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "dataCenter",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "fgwTimeout",
                        "type": "String",
                        "value": "30s"
                      },
                      {
                        "name": "openshiftProject",
                        "type": "String",
                        "value": ""
                      },
                      {
                        "name": "Hostname",
                        "type": "String",
                        "value": "\"\""
                      },
                      {
                        "name": "implTlsSecretGroup",
                        "type": "String",
                        "value": "tls-secret-group"
                      },
                      {
                        "name": "implTlsContext",
                        "type": "String",
                        "value": "tls-context"
                      }
                    ],
                    "when": {
                      "condition": false
                    }
                  }
                }
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
                          }
                        }
                      }
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
}
    
    return stage_data
