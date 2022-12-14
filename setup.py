import sys
import subprocess

packages = ['pyglm', 'moderngl', 'numpy', 'icosphere']

for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

print("Done!")