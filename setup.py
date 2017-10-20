from setuptools import setup, find_packages

setup(name='wagtail-reports',
      version='0.0.2',
      description='Additional reporting functionality for Wagtail to enrich the editor experience.',
      url='http://github.com/vixdigital/wagtail-reports',
      author='VIX Digital',
      author_email='info@vix.digital',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'wagtail>=1.0',
      ],
      zip_safe=False)