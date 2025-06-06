from setuptools import find_packages, setup

package_name = 'my_py_pkg'

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
    maintainer_email='khadim@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "first_node=my_py_pkg.my_first_node:main",
            "first_oop_node=my_py_pkg.my_first_oop_node:main",
            "first_pub_node=my_py_pkg.my_first_publisher:main",
            "first_sub_node=my_py_pkg.my_first_subscriber:main",
            "second_pub_node=my_py_pkg.my_second_publisher:main"

        ],
    },
)
