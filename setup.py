from setuptools import setup, find_packages
# import versioneer

setup(
    name="avogadro-plugin",
    version="0.1",
    install_requires=[],
    include_package_data=True,
    packages=find_packages(),
    scripts=['avogadro-plugin-python-run'],
    entry_points={
        'console_scripts': [
            'avogadro-plugin-python-install=avogadro_plugin.install:install',
            'avogadro-plugin-python-run-command=avogadro_plugin.run:run',
        ]
    },
)
