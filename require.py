import json

with open('Pipfile.lock', 'r') as f:
    reqs = f.read()

with open('requirements.txt', 'w') as f:
    f.writelines(f"{req_name}{value['version']}\n" for req_name, value in json.loads(reqs)['default'].items())
