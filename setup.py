##########################################################################################
# Copyright (c) 2016 - 2018 Nordic Semiconductor ASA. All Rights Reserved.
# 
# The information contained herein is confidential property of Nordic Semiconductor ASA.
# The use, copying, transfer or disclosure of such information is prohibited except by
# express written agreement with Nordic Semiconductor ASA.
##########################################################################################

import setuptools



setuptools.setup(
      name='hostflash',
      version='0.0.1',
      description='hostflash',
      author='The CTF Team',
      author_email='jorgen.kvalvaag@nordicsemi.no',
      license='Nordic Internal',

      packages=setuptools.find_packages(),
      entry_points={
            'console_scripts': [
                  'hostflash_server = hostflash.recv:main',
                  'hostflash = hostflash.send:main'
            ]
      },
      zip_safe=False
)
