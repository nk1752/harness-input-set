from pipeline_input_set import template_init, stage_init, stage_update
import yaml

def main():
  input_set = template_init("test-input_set", "RPC", "External")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = stage_init(input_set, "dev")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = stage_init(input_set, "qaa")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = stage_init(input_set, "qab")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = stage_init(input_set, "proda")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = stage_init(input_set, "prodb")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  print(input_set_yaml)

if __name__ == "__main__":
  main()