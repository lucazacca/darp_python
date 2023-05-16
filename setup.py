import setuptools
setuptools.setup(name='darp_python',
version='0.1',
description='A package for multi-robot path planning',
url='#',
author='',
install_requires=['opencv-python==4.5.4.60', 'pygame==2.1.0', 'scipy==1.7.3', 
                  'jupyter==1.0.0', 'numba>=0.54.1', 'nose==1.3.7', 'parameterized==0.8.1', 'scikit-learn', 'Pillow'],
author_email='',
packages=setuptools.find_packages(),
zip_safe=False)