"""Build"""
import rdo_package_utils.build

rdo_package_utils.build.buildAndInstall(['shotgun_api3'])
rdo_package_utils.build.buildAndUploadWheel()
