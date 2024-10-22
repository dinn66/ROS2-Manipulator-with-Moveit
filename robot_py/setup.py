from setuptools import find_packages, setup

package_name = 'robot_py'

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
    maintainer='inderneil',
    maintainer_email='inderneil@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = robot_py.simple_publisher:main',
            'simple_subscriber = robot_py.simple_subscriber:main',
            'simple_parameter = robot_py.simple_parameter:main',
            'simple_service_server = robot_py.simple_service_server:main',
            'simple_service_client = robot_py.simple_service_client:main',
            'simple_action_server = robot_py.simple_action_server:main',
            'simple_action_client = robot_py.simple_action_client:main'
        ],
    },
)
