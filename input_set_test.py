import input_set_external
import input_set_internal
import yaml

def main():
  input_set = input_set_internal.template_init("test-input_set", "RPC")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = input_set_internal.stage_init(input_set, "dev")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = input_set_internal.stage_init(input_set, "qaa")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = input_set_internal.stage_init(input_set, "qab")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = input_set_internal.stage_init(input_set, "proda")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  #print(input_set_yaml)

  input_set = input_set_internal.stage_init(input_set, "prodb")
  input_set_yaml = yaml.dump(input_set, default_flow_style=False, sort_keys=False)
  print(input_set_yaml)

if __name__ == "__main__":
  main()