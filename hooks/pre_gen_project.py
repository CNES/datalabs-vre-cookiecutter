import re
import sys

SLUG_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
project_slug = '{{ cookiecutter.project_slug }}'

if not re.match(SLUG_REGEX, project_slug):
    print(f'ERROR: {project_slug} is not a valid VRE name!')
    sys.exit(1)

if '{{ cookiecutter.use_pytorch_notebook }}' == 'True' and '{{ cookiecutter.use_pangeo_notebook }}' == 'False':
    print(f'ERROR: pytorch_notebook need pangeo_notebook!')
    sys.exit(1)
    
    