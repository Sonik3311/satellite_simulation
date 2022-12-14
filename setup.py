import sys
import subprocess


packages = ['glm', 'moderngl', 'numpy', 'icosphere']
# implement pip as a subprocess:


for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


# process output with an API in the subprocess module:
#reqs = subprocess.check_output([sys.executable, '-m', 'pip',
#'freeze'])
#installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print("Done!")