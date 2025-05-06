import yaml,sys

def check_form(path):
  with open(path,'r') as f:
    data = yaml.safe_load(f)

    if "name" not in data or "purpose" not in data:
      print("[ERROR] {path}: Missing Required Fields")
      return 1
    print("[OK] Application Correct, Proceed")
    return 0

if __name__=="__main__":
  for path in sys.argv[1:]:
    check_form(path)
