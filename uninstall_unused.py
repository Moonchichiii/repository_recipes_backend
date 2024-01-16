import subprocess

# Read the packages from requirements.txt
with open('requirements.txt', 'r') as f:
    required_packages = f.read().splitlines()

# Get the installed packages using pip freeze
installed_packages = subprocess.check_output(['pip', 'freeze']).decode().split('\n')

# Create a set of required package names
required_package_names = set(package.split('==')[0] for package in required_packages)

# Uninstall any installed packages not in the required list
for package in installed_packages:
    package_name = package.split('==')[0]
    if package_name not in required_package_names:
        subprocess.call(['pip', 'uninstall', '-y', package_name])