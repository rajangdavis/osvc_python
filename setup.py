from setuptools import setup

setup(name='osc_python',
      version='0.1.1',
      description='An unofficial Python ORM on top of the Oracle Cloud Services (fka RightNow Technologies) REST API',
      url='http://github.com/rajangdavis/osc_python',
      author='Rajan Davis',
      author_email='rajangdavis@gmail.com',
      license='MIT',
      packages=['osc_python'],
      install_requires=[
          'requests',
          'python-dateutil'
      ],
      zip_safe=False)