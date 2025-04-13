from setuptools import find_packages, setup

package_name = 'my_service_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khadim',
    maintainer_email='kramoth@udm.ac.mu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "add_two_int_server_node=my_service_pkg.my_first_service_server:main",
            "add_two_int_client_no_oop_node=my_service_pkg.service_client_no_oop:main",
            "add_two_int_client_oop_node=my_service_pkg.service_client_oop:main"
        ],
    },
)
