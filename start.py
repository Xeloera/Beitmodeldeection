import subprocess

def install_packages(package_list_file):
    with open(package_list_file, "r") as f:
        packages = f.readlines()
    packages = [package.strip() for package in packages]

    for package in packages:
        subprocess.call(["pip", "install", package])

if __name__ == "__main__":
    install_packages("requirements.txt")
