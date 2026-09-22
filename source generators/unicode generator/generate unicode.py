from pathlib import Path
import yaml, builtins

def yaml_to_python(yaml_name, yaml_dict, pwd):
    if not any(isinstance(val, dict) for key, val in yaml_dict.items()):
        # no nesting required, it can be a plain .py file
        (pwd / (yaml_name + '.py')).write_text('\n'.join(f'{key} = {val!r}' for key, val in yaml_dict.items()))
        return
 
    # prepare for nesting
    (pwd / yaml_name).mkdir(parents=True, exist_ok=True)
    
    (pwd / yaml_name / '__init__.py').write_text('\n'.join(f'from . import {file.stem}' for file in (pwd / yaml_name).iterdir()))
    
    for key, val in yaml_dict.items():
        if isinstance(val, dict):
            with open(pwd / yaml_name / '__init__.py', 'a') as file:
                file.write(f'from . import {key}\n')
            yaml_to_python(key, val, pwd / yaml_name)
        else:
            with open(pwd / yaml_name / '__init__.py', 'a') as file:
                file.write(f'{key} = {val!r}\n')

pwd = Path()

for file in pwd.iterdir():
    if file.suffix != '.yaml':
        continue
    yaml_to_python(file.stem, yaml.safe_load(open(file)), pwd / 'unicode')

(pwd / 'unicode').mkdir(parents=True, exist_ok=True)
(pwd / 'unicode/__init__.py').write_text('\n'.join(f'from .{file.stem} import *' for file in pwd.iterdir() if file.suffix == '.yaml'))

# correct quirks yourself
