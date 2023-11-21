import setuptools
  
setuptools.setup( 
    name='my_package', 
    version='0.1', 
    description='A sample Python package', 
    author='Yujiang Wu', 
    author_email='wuyujiangacademy@yahoo.com', 
    packages=setuptools.find_packages(), 
    install_requires=[ 
        'numpy', 
        'pandas', 
    ], 
) 