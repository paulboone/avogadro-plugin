from distutils.version import LooseVersion

import subprocess
import sys

def install():
    python_required = "3.5"

    ###
    ### Check python version
    python_version = sys.version
    if LooseVersion(python_version) < LooseVersion(python_required):
        print("The available version of python %s is less than what is required (%s)" \
                % (python_version, python_required))
        sys.exit(64)

    ###
    ### create venv and install requirements
    print("Creating plugin-specific virtual environment...")
    subprocess.run(['python3','-m','venv','./venv'], check=True)
    print("Installing any requirements via pip...")
    subprocess.run(". ./venv/bin/activate && pip install -r ./requirements.txt", shell=True, check=True)
    print("Everything looks ok!")
