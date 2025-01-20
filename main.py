import yaml
import csv
import json

from filter import apply_harn_filter, apply_filter, apply_env_filter
from harn_input_set_old import build_internal, build_extrernal
from setup_yaml import setup_stage


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

    project_name = 'rdc'
    project_column = 'harnProject'

    proj_list: list[dict] = apply_harn_filter(project_name, project_column, input_set_values)
    print(f"Count of proj_list: {len(proj_list)}")
    with open("proj_list.yaml", "w") as file:
        yaml.dump(proj_list, file, default_flow_style=False, sort_keys=False)

    counter = 0
    try:
        for input in proj_list:

            apiId: str = input['apiSpecAssetId']
            
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
        print(f"KeyError: {project_name} not found in the input_set")

    print("********* dev_b *********")
    print(json.dumps(dev_b, indent=4))
    print("********* dev_b_z *********")
    print(json.dumps(dev_z_b, indent=4))
    print("********* qa_a *********")
    print(json.dumps(qa_a, indent=4))
    print("********* qa_b *********")
    print(json.dumps(qa_b, indent=4))

    

    data = build_internal(dev_b, qa_a, qa_b)
    with open("input_set_internal.yaml", "w") as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

    # data = build_extrernal(dev_z_b, qa_z_a, qa_z_b)
    # with open("input_set_external.yaml", "w") as file:
    #     yaml.dump(data, file, default_flow_style=False, sort_keys=False)


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
