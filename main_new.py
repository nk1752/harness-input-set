import yaml
import csv
from typing import List, Dict

import pipeline_internal
import pipeline_external
import filter

import logging
logging.basicConfig(level=logging.INFO)

def main():

    pipeline_internal.hello_world()
    pipeline_external.hello_world()

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

    logging.info("********* proj_list filter *********")
    proj_list: list[dict] = filter.input_data(x_key, project_name, input_set_values)
    logging.debug(f"Count of proj_list: {len(proj_list)}")
    with open("proj_list.yaml", "w") as file:
        yaml.dump(proj_list, file, default_flow_style=False, sort_keys=False)

    input_set_internal: list[dict] = []
    input_set_external: list[dict] = []

    # loop through the proj_list to process all apiSpecAssetId
    proj_counter = 0
    for proj in proj_list:
        proj_counter += 1
        logging.debug(f"proj_counter: {proj_counter}")
        x_key = "apiSpecAssetId"
        x_value = proj["apiSpecAssetId"]

        logging.info("********* asset_list filter *********")
        asset_list: list[dict] = filter.input_data(x_key, x_value, proj_list)
        logging.debug(f"Count of asset_list: {len(asset_list)}")
        # with open("asset_list.yaml", "w") as file:
        #     yaml.dump(asset_list, file, default_flow_style=False, sort_keys=False)

        # loop through the asset_list to process all apiSpecAssetVersion
        asset_counter = 0
        for asset in asset_list:
            asset_counter += 1
            logging.debug(f"asset_counter: {asset_counter}")
            x_key = "apiSpecAssetVersion"
            x_value = asset["apiSpecAssetVersion"]

            logging.info(f"asset filer: {x_key} value: {x_value}")

            logging.info("********* filter input_list for  apiSpecAssetVersion *********")
            version_list: list[dict] = filter.input_data(x_key, x_value, asset_list)
            print(f"Count of input_list: {len(version_list)}")
            # with open("input_list.yaml", "w") as file:
            #     yaml.dump(input_list, file, default_flow_style=False, sort_keys=False)

            for version in version_list:
                #print(f"version: {version}")
                # find all env for pipeline
                fgw_target = version["fgwInstanceName"]
                print(f"fgw_target: {fgw_target}")

                # copy the input to the respective dictionary base on flex instance name
                if fgw_target.find("dev-b") != -1:
                    dev_b.update(version)
                    print(f"updated dev_b")
                elif fgw_target.find("dev-z-b") != -1:
                    dev_z_b.update(version)
                    print(f"updated dev_z_b")
                elif fgw_target.find("np-a") != -1:
                    qa_a.update(version)
                    print(f"updated qa_a")
                elif fgw_target.find("np-b") != -1:
                    qa_b.update(version)
                    print(f"updated qa_b")
                elif fgw_target.find("np-z-a") != -1:
                    qa_z_a.update(version)
                    print(f"updated qa_z_a")
                elif fgw_target.find("np-z-b") != -1:
                    qa_z_b.update(version)
                    print(f"updated qa_z_b")
                elif fgw_target.find("prod-z-a") != -1:
                    qa_z_a.update(version)
                    print(f"updated prod-z-a")
                elif fgw_target.find("prod-z-b") != -1:
                    qa_z_b.update(version)
                    print(f"updated prod-z-b")
                else:
                    print(f"fgwInstanceName --> {fgw_target} not found")

        # pipeline name, identifier & project name
        pipeline_name: str = f"{version['apiSpecAssetId']}-{version['apiSpecAssetVersion']}"

        internal_set: dict = {}
        internal_set = pipeline_internal.add_header(pipeline_name, project_name)
        print(yaml.dump(internal_set, default_flow_style=False, sort_keys=False))

        if dev_b:
            dev_b_stage = pipeline_internal.add_stage(dev_b, "dev")
        else:
            dev_b_stage = pipeline_internal.init_stage("dev")
        if qa_a:
            qa_a_stage = pipeline_internal.add_stage(qa_a, "qaa")
        else:
            qa_a_stage = pipeline_internal.init_stage("qaa")
        if qa_b:
            qa_b_stage = pipeline_internal.add_stage(qa_b, "qab")
        else:
            qa_b_stage = pipeline_internal.init_stage("qab")
        if prod_a:
            prod_a_stage = pipeline_internal.add_stage(prod_a, "proda")
        else:
            prod_a_stage = pipeline_internal.init_stage("proda")
        if prod_b:
            prod_b_stage = pipeline_internal.add_stage(prod_b, "prodb")
        else:
            prod_b_stage = pipeline_internal.init_stage("prodb")

        

        external_set: dict = {}
        external_set = pipeline_external.add_header(pipeline_name, project_name)
        print(yaml.dump(external_set, default_flow_style=False, sort_keys=False))

        if dev_z_b:
            dev_z_b_stage = pipeline_internal.add_stage(dev_z_b, "devz")
        else:
            dev_z_b_stage = pipeline_internal.init_stage("devz")
        if qa_z_a:
            qa_z_a_stage = pipeline_internal.add_stage(qa_z_a, "qaza")
        else:
            qa_z_a_stage = pipeline_internal.init_stage("qaza")
        if qa_z_b:
            qa_z_b_stage = pipeline_internal.add_stage(qa_z_b, "qazb")
        else:
            qa_z_b_stage = pipeline_internal.init_stage("qazb")
        if prod_z_a:
            prod_z_a_stage = pipeline_internal.add_stage(prod_z_a, "prodza")
        else:
            prod_z_a_stage = pipeline_internal.init_stage("prodza")
        if prod_z_b:
            prod_z_b_stage = pipeline_internal.add_stage(prod_z_b, "prodzb")
        else:
            prod_z_b_stage = pipeline_internal.init_stage("prodzb")

        approval_qa = pipeline_internal.approval_init("qa")
        approval_prod = pipeline_internal.approval_init("prod")
        approval_closing = pipeline_internal.closing_approval_init()
        
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))
        internal_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(dev_b_stage)
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))
        internal_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(approval_qa)
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))
        internal_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(qa_a_stage)
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))
        internal_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(qa_b_stage)
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))
        internal_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(approval_prod)
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))
        internal_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(prod_a_stage)
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))
        internal_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(prod_b_stage)
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))
        internal_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(approval_closing)
        logging.debug(yaml.dump(internal_set,default_flow_style=False, sort_keys=False))

        approval_z_qa = pipeline_internal.approval_init("qaz")
        approval_z_prod = pipeline_internal.approval_init("prodz")
        
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))
        external_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(dev_z_b_stage)
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))
        external_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(approval_z_qa)
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))
        external_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(qa_z_a_stage)
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))
        external_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(qa_z_b_stage)
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))
        external_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(approval_z_prod)
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))
        external_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(prod_z_a_stage)
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))
        external_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(prod_z_b_stage)
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))
        external_set["inputSet"]["pipeline"]["template"]["templateInputs"]["stages"].append(approval_closing)
        logging.debug(yaml.dump(external_set,default_flow_style=False, sort_keys=False))                   

        print(f"internal_set completed")
        with open(f"{pipeline_name}.yaml", "w") as file:
            yaml.dump(internal_set, file, default_flow_style=False, sort_keys=False)

        print(f"external_set completed")
        with open(f"{pipeline_name}.yaml", "w") as file:
            yaml.dump(external_set, file, default_flow_style=False, sort_keys=False)
        


if __name__ == "__main__":
  main()