from setuptools import setup

setup(name='osvc_python',
      version='1.0.1',
      description='An unofficial Python wrapper on top of the Oracle Cloud Services (fka RightNow Technologies) REST API',
      url='http://github.com/rajangdavis/osvc_python',
      author='Rajan Davis',
      author_email='rajangdavis@gmail.com',
      license='MIT',
      packages=['osvc_python'],
      install_requires=[
          'requests',
          'futures'
      ],
      zip_safe=False)