import os
import subprocess
import shutil


def add_module(module, module_to_use, ignore_list):
    if module not in ignore_list:
        use_module = input(f"Use module : {module}? (y/n): ").lower().startswith("y")
        if use_module:
            module_to_use.append(module)

    return


def print_limit(title):
    print()
    print()
    print(f"----------------- {title} -----------------")
    print()
    print()

    return


def update():
    print_limit("Base layers")
    result = subprocess.run(
        ["git", "clone", "https://github.com/CNES/datalabs-docker-images.git"],
        capture_output=True,
        text=True,
    )
    os.makedirs(".base_layer")

    shutil.copyfile(
        "datalabs-docker-images/base-notebook/environment.yml",
        ".base_layer/base-notebook-environment.yml",
    )
    shutil.copyfile(
        "datalabs-docker-images/base-notebook/apt.txt",
        ".base_layer/base-notebook-apt.txt",
    )
    if {{cookiecutter.use_pangeo_notebook}}:
        shutil.copyfile(
            "datalabs-docker-images/pangeo-notebook/environment.yml",
            ".base_layer/pangeo-notebook-environment.yml",
        )
        shutil.copyfile(
            "datalabs-docker-images/pangeo-notebook/apt.txt",
            ".base_layer/pangeo-notebook-apt.txt",
        )
    if {{cookiecutter.use_pytorch_notebook}}:
        shutil.copyfile(
            "datalabs-docker-images/pytorch-notebook/environment.yml",
            ".base_layer/pytorch-notebook-environment.yml",
        )
        shutil.copyfile(
            "datalabs-docker-images/pytorch-notebook/apt.txt",
            ".base_layer/pytorch-notebook-apt.txt",
        )

    result = subprocess.run(
        ["rm", "-rf", "datalabs-docker-images"], capture_output=True, text=True
    )


print("cookiecutter: POST GEN PROJECT")


print_limit("Modules")
result = subprocess.run(
    ["git", "clone", "https://github.com/CNES/datalabs-common-modules.git"],
    capture_output=True,
    text=True,
)

module_to_use = ["branding", "nbproxy", "vnc", "vscode"]
ignore_list = module_to_use.copy()
ignore_list.append(".git")

modules = [f.name for f in os.scandir("datalabs-common-modules") if f.is_dir()]
for module in modules:
    add_module(module, module_to_use, ignore_list)

with open("module.txt", "w") as f:
    for module in module_to_use:
        f.write(f"{module}\n")

result = subprocess.run(["rm", "-rf", "common_modules"], capture_output=True, text=True)
result = subprocess.run(
    ["rm", "-rf", "datalabs-common-modules"], capture_output=True, text=True
)


os.chmod("generate-packages-list.py", 0o700)
os.chmod("get_version.sh", 0o700)
os.chmod("merge-apt.sh", 0o700)
os.chmod("run_tests.sh", 0o700)
os.chmod("run_tests.sh", 0o700)
os.chmod("update_base_layer.py", 0o700)


update()
