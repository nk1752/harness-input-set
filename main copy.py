import yaml
import csv
import json

from pipeline_input_set import template_init, stage_init, stage_update, filter


def main():
    print("********* main *********")

    input_set_values: list[dict] = []
    with open("flex-input-set.csv", "r") as file:
        reader = csv.DictReader(file)
        input_set_values = list(reader)
   
    dev_b: dict = {}
    qa_a: dict = {}
    qa_b: dict = {}
    prod_a: dict = {}
    prod_b: dict = {}

    dev_z_b: dict = {}
    qa_z_a: dict = {}
    qa_z_b: dict = {}
    prod_z_a: dict = {}
    prod_z_b: dict = {}

    x_key = 'harnProject'
    x_value = 'rdc'

    print("********* pro_filter *********")
    proj_list: list[dict] = filter(x_key, x_value, input_set_values)
    print(f"Count of proj_list: {len(proj_list)}")
    with open("proj_list.yaml", "w") as file:
        yaml.dump(proj_list, file, default_flow_style=False, sort_keys=False)

    x_key = 'apiSpecAssetId'
    x_value = 'mkt-ras-proxy'

    print("********* asset_list *********")
    asset_list: list[dict] = filter(x_key, x_value, proj_list)
    print(f"Count of asset_list: {len(asset_list)}")
    with open("asset_list.yaml", "w") as file:
        yaml.dump(asset_list, file, default_flow_style=False, sort_keys=False)

    # loop through the asset_list to process all apiSpecAssetVersion
    counter = 0
    for asset in asset_list:
        counter += 1
        x_key = 'apiSpecAssetVersion'
        x_value = asset['apiSpecAssetVersion']

        print("********* input_list *********")
        input_list: list[dict] = filter(x_key, x_value, asset_list)
        print(f"Count of input_list: {len(input_list)}")
        with open("input_list.yaml", "w") as file:
            yaml.dump(input_list, file, default_flow_style=False, sort_keys=False)

        input_set_internal: list[dict] = []
        input_set_external: list[dict] = []

        
        try:
            for input in input_list:

                project_name: str = input['harnProject']
                pipeline_name: str = input['apiSpecAssetId']

                internal_set: dict = {}
                external_set: dict = {}

                internal_set = template_init(pipeline_name, project_name, "Internal")
                external_set = template_init(pipeline_name, project_name, "External")
                
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
                elif target.find('prod-z-a') != -1:
                    qa_z_a.update(input)
                    print(f"updated prod-z-a")
                elif target.find('prod-z-b') != -1:
                    qa_z_b.update(input)
                    print(f"updated prod-z-b")
                else:
                    print(f"fgwInstanceName --> {target} not found")
                
        except KeyError:
            print(f"KeyError: {target} not found in the input_set")

             # # check if set is empty
        # if not, build the internal and external sets
        if dev_b:
            internal_set =  stage_update(internal_set, dev_b, "dev")
        else:
            internal_set = stage_init(internal_set, "dev")
        
        if qa_a:
            internal_set =  stage_update(internal_set, qa_a, "qaa")
        else:
            internal_set = stage_init(internal_set, "qaa")

        if qa_b:
            internal_set =  stage_update(internal_set, qa_b, "qab")
        else:
            internal_set = stage_init(internal_set, "qab")

        if prod_a:
            internal_set =  stage_update(internal_set, prod_a, "proda")
        else:
            internal_set = stage_init(internal_set, "proda")

        if prod_b:
            internal_set =  stage_update(internal_set, prod_b, "prodb")
        else:
            internal_set = stage_init(internal_set, "prodb")

        # ***** dmz *****
        
        if dev_z_b:
            external_set =  stage_update(external_set, dev_z_b, "devz")
        else:
            external_set = stage_init(external_set, "devz")

        if qa_z_a:
            external_set =  stage_update(external_set, qa_z_a, "qaza")
        else:
            external_set = stage_init(external_set, "qaza")

        if qa_z_b:
            external_set =  stage_update(external_set, qa_z_b, "qazb")
        else:
            external_set = stage_init(external_set, "qazb")

        if prod_z_a:
            external_set =  stage_update(external_set, prod_z_a, "prodza")
        else:
            external_set = stage_init(external_set, "prodza")

        if prod_z_b:
            external_set =  stage_update(external_set, prod_z_b, "prodzb")
        else:
            external_set = stage_init(external_set, "prodzb")

        print("********* input_set_internal *********")
        input_set_internal.append(internal_set)

        print("********* input_set_external *********")
        input_set_external.append(external_set)

    print(f"Count of input_set_internal: {len(input_set_internal)}")
    print(f"Count of input_set_external: {len(input_set_external)}")
    print(f"Count of counter: {counter}")

    with open("input_set_internal.yaml", "w") as file:
        yaml.dump(input_set_internal, file, default_flow_style=False, sort_keys=False)

    with open("input_set_external.yaml", "w") as file:
        yaml.dump(input_set_external, file, default_flow_style=False, sort_keys=False)


    # x_key = 'apiSpecAssetVersion'
    # x_value = 'v1'

    # print("********* input_list *********")
    # input_list: list[dict] = filter(x_key, x_value, asset_list)
    # print(f"Count of input_list: {len(input_list)}")
    # with open("input_list.yaml", "w") as file:
    #     yaml.dump(input_list, file, default_flow_style=False, sort_keys=False)

    # input_set_internal: dict = {}
    # input_set_external: dict = {}

    # counter = 0
    # try:
    #     for input in input_list:

    #         project_name: str = input['harnProject']
    #         pipeline_name: str = input['apiSpecAssetId']

    #         input_set_internal = template_init(pipeline_name, project_name, "Internal")
    #         print(yaml.dump(input_set_internal, default_flow_style=False, sort_keys=False))

    #         input_set_external = template_init(pipeline_name, project_name, "External")
    #         print(yaml.dump(input_set_external, default_flow_style=False, sort_keys=False))
            
    #         target: str = input['fgwInstanceName']
    #         print(f"apiSpecAssetId --> {target}")

    #         if target.find('dev-b') != -1:
    #             dev_b.update(input)
    #             print(f"updated dev_b")
    #         elif target.find('dev-z-b') != -1:
    #             dev_z_b.update(input)
    #             print(f"updated dev_z_b")
    #         elif target.find('np-a') != -1:
    #             qa_a.update(input)
    #             print(f"updated qa_a")
    #         elif target.find('np-b') != -1:
    #             qa_b.update(input)
    #             print(f"updated qa_b")
    #         elif target.find('np-z-a') != -1:
    #             qa_z_a.update(input)
    #             print(f"updated qa_z_a")
    #         elif target.find('np-z-b') != -1:
    #             qa_z_b.update(input)
    #             print(f"updated qa_z_b")
    #         elif target.find('prod-z-a') != -1:
    #             qa_z_a.update(input)
    #             print(f"updated prod-z-a")
    #         elif target.find('prod-z-b') != -1:
    #             qa_z_b.update(input)
    #             print(f"updated prod-z-b")
    #         else:
    #             print(f"fgwInstanceName --> {target} not found")

    #         #proj_list.remove(input)
            
    # except KeyError:
    #     print(f"KeyError: {target} not found in the input_set")


    # print("********* build pipeline *********")
   
    
    # # check if set is empty
    # # if not, build the internal and external sets
    # if dev_b:
    #     input_set_internal =  stage_update(input_set_internal, dev_b, "dev")
    # else:
    #     input_set_internal = stage_init(input_set_internal, "dev")
    
    # if qa_a:
    #     input_set_internal =  stage_update(input_set_internal, qa_a, "qaa")
    # else:
    #     input_set_internal = stage_init(input_set_internal, "qaa")

    # if qa_b:
    #     input_set_internal =  stage_update(input_set_internal, qa_b, "qab")
    # else:
    #     input_set_internal = stage_init(input_set_internal, "qab")

    # if prod_a:
    #     input_set_internal =  stage_update(input_set_internal, prod_a, "proda")
    # else:
    #     input_set_internal = stage_init(input_set_internal, "proda")

    # if prod_b:
    #     input_set_internal =  stage_update(input_set_internal, prod_b, "prodb")
    # else:
    #     input_set_internal = stage_init(input_set_internal, "prodb")

    # # ***** dmz *****
    
    # if dev_z_b:
    #     input_set_external =  stage_update(input_set_external, dev_z_b, "devz")
    # else:
    #     input_set_external = stage_init(input_set_external, "devz")

    # if qa_z_a:
    #     input_set_external =  stage_update(input_set_external, qa_z_a, "qaza")
    # else:
    #     input_set_external = stage_init(input_set_external, "qaza")

    # if qa_z_b:
    #     input_set_external =  stage_update(input_set_external, qa_z_b, "qazb")
    # else:
    #     input_set_external = stage_init(input_set_external, "qazb")

    # if prod_z_a:
    #     input_set_external =  stage_update(input_set_external, prod_z_a, "prodza")
    # else:
    #     input_set_external = stage_init(input_set_external, "prodza")

    # if prod_z_b:
    #     input_set_external =  stage_update(input_set_external, prod_z_b, "prodzb")
    # else:
    #     input_set_external = stage_init(input_set_external, "prodzb")


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
