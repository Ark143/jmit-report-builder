from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().split("\n")

setup(
	name="jmit_report_builder",
	version="0.0.1",
	description="JMIT Report Builder - Crystal Report Clone for ERPNext v15",
	author="JMIT",
	author_email="info@jmit.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
