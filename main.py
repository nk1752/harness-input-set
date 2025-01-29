import yaml
import csv
import json

from pipeline_input_set import template_init, stage_init, stage_update, filter, header_init


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

    x_key = "harnProject"
    project_name  = "rdc"

    print("********* pro_filter *********")
    proj_list: list[dict] = filter(x_key, project_name, input_set_values)
    print(f"Count of proj_list: {len(proj_list)}")
    with open("proj_list.yaml", "w") as file:
        yaml.dump(proj_list, file, default_flow_style=False, sort_keys=False)

    input_set_internal: list[dict] = []
    input_set_external: list[dict] = []

    # loop through the proj_list to process all apiSpecAssetId
    proj_counter = 0
    for proj in proj_list:
        proj_counter += 1
        print(f"proj_counter: {proj_counter}")
        x_key = "apiSpecAssetId"
        x_value = proj["apiSpecAssetId"]

        print("********* asset_list *********")
        asset_list: list[dict] = filter(x_key, x_value, proj_list)
        print(f"Count of asset_list: {len(asset_list)}")
        # with open("asset_list.yaml", "w") as file:
        #     yaml.dump(asset_list, file, default_flow_style=False, sort_keys=False)

        

        # loop through the asset_list to process all apiSpecAssetVersion
        asset_counter = 0
        for asset in asset_list:
            asset_counter += 1
            print(f"asset_counter: {asset_counter}")
            x_key = "apiSpecAssetVersion"
            x_value = asset["apiSpecAssetVersion"]

            print("********* filter input_list for  apiSpecAssetVersion *********")
            input_list: list[dict] = filter(x_key, x_value, asset_list)
            print(f"Count of input_list: {len(input_list)}")
            # with open("input_list.yaml", "w") as file:
            #     yaml.dump(input_list, file, default_flow_style=False, sort_keys=False)

            internal_set: dict = {}
            external_set: dict = {}

            # pipeline name, identifier & project name
            pipeline_name: str = asset["apiSpecAssetId"]

            # initialize the internal and external sets for current pipeline
            internal_set = header_init(pipeline_name, project_name)
            external_set = header_init(pipeline_name, project_name)

            # find all env for pipeline
            input_counter = 0
            try:
                for input in input_list:
                    input_counter += 1
                    print(f"input_counter: {input_counter}")
                    project_name: str = input["harnProject"]

                    # print internal_set and external_set count
                    print(f"Count of internal_set: {len(internal_set)}")
                    print(f"Count of external_set: {len(external_set)}")

                    target: str = input["fgwInstanceName"]
                    print(f"apiSpecAssetId --> {target}")

                    # copy the input to the respective dictionary base on flex instance name
                    if target.find("dev-b") != -1:
                        dev_b.update(input)
                        print(f"updated dev_b")
                    elif target.find("dev-z-b") != -1:
                        dev_z_b.update(input)
                        print(f"updated dev_z_b")
                    elif target.find("np-a") != -1:
                        qa_a.update(input)
                        print(f"updated qa_a")
                    elif target.find("np-b") != -1:
                        qa_b.update(input)
                        print(f"updated qa_b")
                    elif target.find("np-z-a") != -1:
                        qa_z_a.update(input)
                        print(f"updated qa_z_a")
                    elif target.find("np-z-b") != -1:
                        qa_z_b.update(input)
                        print(f"updated qa_z_b")
                    elif target.find("prod-z-a") != -1:
                        qa_z_a.update(input)
                        print(f"updated prod-z-a")
                    elif target.find("prod-z-b") != -1:
                        qa_z_b.update(input)
                        print(f"updated prod-z-b")
                    else:
                        print(f"fgwInstanceName --> {target} not found")

            except KeyError:
                print(f"KeyError: {target} not found in the input_set")

                # # check if set is empty
            # if not, build the internal and external sets
            if dev_b:
                internal_set = stage_update(internal_set, dev_b, "dev")
            else:
                internal_set = stage_init(internal_set, "dev")

            if qa_a:
                internal_set = stage_update(internal_set, qa_a, "qaa")
            else:
                internal_set = stage_init(internal_set, "qaa")

            if qa_b:
                internal_set = stage_update(internal_set, qa_b, "qab")
            else:
                internal_set = stage_init(internal_set, "qab")

            if prod_a:
                internal_set = stage_update(internal_set, prod_a, "proda")
            else:
                internal_set = stage_init(internal_set, "proda")

            if prod_b:
                internal_set = stage_update(internal_set, prod_b, "prodb")
            else:
                internal_set = stage_init(internal_set, "prodb")

            # ***** dmz *****

            if dev_z_b:
                external_set = stage_update(external_set, dev_z_b, "devz")
            else:
                external_set = stage_init(external_set, "devz")

            if qa_z_a:
                external_set = stage_update(external_set, qa_z_a, "qaza")
            else:
                external_set = stage_init(external_set, "qaza")

            if qa_z_b:
                external_set = stage_update(external_set, qa_z_b, "qazb")
            else:
                external_set = stage_init(external_set, "qazb")

            if prod_z_a:
                external_set = stage_update(external_set, prod_z_a, "prodza")
            else:
                external_set = stage_init(external_set, "prodza")

            if prod_z_b:
                external_set = stage_update(external_set, prod_z_b, "prodzb")
            else:
                external_set = stage_init(external_set, "prodzb")

        print("********* input_set_internal *********")
        input_set_internal.append(internal_set)

        print("********* input_set_external *********")
        input_set_external.append(external_set)

        print(f"Count of input_set_internal: {len(input_set_internal)}")
        print(f"Count of input_set_external: {len(input_set_external)}")
        

        with open("input_set_internal.yaml", "w") as file:
            yaml.dump(input_set_internal, file, default_flow_style=False, sort_keys=False)

        with open("input_set_external.yaml", "w") as file:
            yaml.dump(input_set_external, file, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    main()
