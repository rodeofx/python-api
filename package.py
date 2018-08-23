name = "shotgun_api3"

shotgunSoftwareVersion = "3.0.37"
rodeoVersion = "1.6.0"
version = "-rdo-".join([shotgunSoftwareVersion, rodeoVersion])

authors = ["shotgundev@rodeofx.com"]

description = """Fork of the python api of shotgun."""

requires = ['python-2.4+<3']

private_build_requires = ['rdo_package_utils']

variants = []

uuid = "9E411E66-9F35-49BC-AC2E-E9DC6D50D109"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/")

