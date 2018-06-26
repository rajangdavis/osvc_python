from setuptools import setup

setup(name='osvc_python',
      version='1.0.0',
      description='An unofficial Python ORM on top of the Oracle Cloud Services (fka RightNow Technologies) REST API',
      url='http://github.com/rajangdavis/osvc_python',
      author='Rajan Davis',
      author_email='rajangdavis@gmail.com',
      license='MIT',
      packages=['osvc_python'],
      install_requires=[
          'requests',
          'python-dateutil'
      ],
      zip_safe=False)