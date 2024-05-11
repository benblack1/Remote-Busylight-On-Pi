import os
import subprocess
import pkg_resources


def check_requirements(source):
    # Get the directory that this script is in
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Check if requirements.txt file exists
    with open(os.path.join(script_dir, 'requirements.txt'), 'r') as file:
        all_requirements = file.read().splitlines()

    # Filter the requirements based on the source
    requirements = [req.split(':')[1] for req in all_requirements if req.startswith(source)]

    # Get the list of currently installed packages
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s" % i.key for i in installed_packages])

    # Check if each required package is installed
    for requirement in requirements:
        if requirement not in installed_packages_list:
            print(f"Requirement not satisfied: {requirement}")
            return False

    print("All requirements are satisfied.")
    return True

def install_requirements(source):
    try:
        print("Checking requirements...")
        if not check_requirements(source):
            print("Installing requirements...")
            # Get the directory that this script is in
            script_dir = os.path.dirname(os.path.realpath(__file__))
            # Filter the requirements based on the source
            with open(os.path.join(script_dir, 'requirements.txt'), 'r') as file:
                all_requirements = file.read().splitlines()
            requirements = [req.split(':')[1] for req in all_requirements if req.startswith(source)]
            # Install each requirement using pip and suppress the output
            for requirement in requirements:
                subprocess.check_call(['pip', 'install', requirement], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            print("Requirements installed successfully.")
        else:
            print("No installation necessary.")
    
    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    except subprocess.CalledProcessError:
        print("Failed to install requirements.")