import yaml
import csv
import json

import filter
from pipeline_input_set import template_init, stage_init, stage_update


def main():
    print("********* main *********")

    input_set_values: list[dict] = []
    with open("flex-input-set.csv", "r") as file:
        reader = csv.DictReader(file)
        input_set_values = list(reader)

    """
    filter -> harnessProject name:
     - treasurymanagementapis
     - rdc
    x_key -> harnProject, dev, qa, prod
    input_set -> input_set_values
    """
    print("********* pro_filter *********")

    # pro_filter = apply_filter("rdc", "harnProject", input_set_values)
    # with open("pro_filter.yaml", "w") as file:
    #     yaml.dump(pro_filter, file, default_flow_style=False, sort_keys=False)
    # # print(json.dumps(pro_filter, indent=4))
    # print(f"Count of pro_filter: {len(pro_filter)}")

    # for proj in pro_filter:
    #     msg = f"fgwInstanceName --> {proj['fgwInstanceName']}"
    #     print(msg)

    # print("********* fgw_instance *********")

    dev_b: dict = {}
    qa_a: dict = {}
    qa_b: dict = {}

    dev_z_b: dict = {}
    qa_z_a: dict = {}
    qa_z_b: dict = {}

    x_key = 'harnProject'
    x_value = 'rdc'

    proj_list: list[dict] = filter.input_data(x_key, x_value, input_set_values)
    print(f"Count of proj_list: {len(proj_list)}")
    with open("proj_list.yaml", "w") as file:
        yaml.dump(proj_list, file, default_flow_style=False, sort_keys=False)

    x_key = 'apiSpecAssetId'
    x_value = 'mkt-ras-proxy'

    asset_list: list[dict] = filter.input_data(x_key, x_value, proj_list)
    print(f"Count of asset_list: {len(asset_list)}")
    with open("asset_list.yaml", "w") as file:
        yaml.dump(asset_list, file, default_flow_style=False, sort_keys=False)

    x_key = 'apiSpecAssetVersion'
    x_value = 'v1'

    input_list: list[dict] = filter.input_data(x_key, x_value, asset_list)
    print(f"Count of input_list: {len(input_list)}")
    with open("input_list.yaml", "w") as file:
        yaml.dump(input_list, file, default_flow_style=False, sort_keys=False)

    counter = 0
    try:
        for input in input_list:

            project_name: str = input['harnProject']
            pipeline_name: str = input['apiSpecAssetId']
            
            target: str = input['fgwInstanceName']
            print(f"apiSpecAssetId --> {target}")

            if target.find('dev-b') != -1:
                dev_b.update(input)
                print(f"updated dev_b")
            elif target.find('dev-z-b') != -1:
                dev_z_b.update(input)
                print(f"updated dev_z_b")
            elif target.find('np-a') != -1:
                qa_a.update(input)
                print(f"updated qa_a")
            elif target.find('np-b') != -1:
                qa_b.update(input)
                print(f"updated qa_b")
            elif target.find('np-z-a') != -1:
                qa_z_a.update(input)
                print(f"updated qa_z_a")
            elif target.find('np-z-b') != -1:
                qa_z_b.update(input)
                print(f"updated qa_z_b")
            else:
                print(f"fgwInstanceName --> {target} not found")

            #proj_list.remove(input)
            
    except KeyError:
        print(f"KeyError: {target} not found in the input_set")

    input_set_internal = template_init(pipeline_name, project_name, "Internal")
    print(yaml.dump(input_set_internal, default_flow_style=False, sort_keys=False))

    input_set_external = template_init(pipeline_name, project_name, "External")
    print(yaml.dump(input_set_external, default_flow_style=False, sort_keys=False))

    print("********* dev_b *********")
    print(json.dumps(dev_b, indent=4))
    
    # check if dev_b is empty
    # if not, build the internal and external sets
    if dev_b:
        input_set_internal =  stage_update(input_set_internal, dev_b, "dev")
    else:
        input_set_internal = stage_init(input_set_internal, "dev")
    
    if qa_a:
        input_set_internal =  stage_update(input_set_internal, qa_a, "qaa")
    else:
        input_set_internal = stage_init(input_set_internal, "qaa")

    if qa_b:
        input_set_internal =  stage_update(input_set_internal, qa_b, "qab")
    else:
        input_set_internal = stage_init(input_set_internal, "qab")

    # ***** dmz *****
    
    if dev_z_b:
        input_set_internal =  stage_update(input_set_internal, dev_z_b, "devz")
    else:
        input_set_internal = stage_init(input_set_internal, "devz")

    if qa_z_a:
        input_set_external =  stage_update(input_set_internal, qa_z_a, "qaza")
    else:
        input_set_external = stage_init(input_set_internal, "qaza")

    if qa_z_b:
        input_set_external =  stage_update(input_set_internal, qa_z_b, "qazb")
    else:
        input_set_external = stage_init(input_set_internal, "qazb")



    print("********* input_set_internal *********")
    print(yaml.dump(input_set_internal, default_flow_style=False, sort_keys=False))

    print("********* input_set_external *********")
    print(yaml.dump(input_set_external, default_flow_style=False, sort_keys=False))


    # qa_filter = apply_env_filter("QA", "apEnvName", pro_filter)
    # with open("qa_filter.yaml", "w") as file:
    #     yaml.dump(qa_filter, file, default_flow_style=False, sort_keys=False)
    # # print(json.dumps(qa_filter, indent=4))
    # # print(f"Count of qa_filter: {len(qa_filter)}")

    # # counter = 0
    # # pipeline_set = build_input_set(dev_filter[0], qa_filter[0])
    # # counter += 1
    # # print(counter)
    # # with open("test.yaml", "w") as file:
    # #     yaml.dump(pipeline_set, file, default_flow_style=False, sort_keys=False)

    

    # print(f"Count of pro_filter: {len(pro_filter)}")
    # print(f"Count of dev_filter: {len(dev_filter)}")
    # print(f"Count of qa_filter: {len(qa_filter)}")


    # # setup_yaml_data = setup_yaml()

    # # updated_set = test_set(setup_yaml_data, dev_filter[0])
    # # print(json.dumps(updated_set, indent=4))
    




if __name__ == "__main__":
    main()
