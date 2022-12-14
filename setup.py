import sys
import subprocess

packages = ['pyglm', 'moderngl', 'numpy', 'icosphere', 'matplotlib', 'scipy']
spackages = ['python']

for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

for package in spackages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--pre'])

print("Done!")