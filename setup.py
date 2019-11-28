from setuptools import setup
from setuptools import find_packages

install_requires = [
    'Keras',
    'recurrentshop'
]

setup(
      name='seq2seq',
      version='1.1.1',
      description='Sequence to Sequence Learning with Keras',
      author='Fariz Rahman',
      author_email='farizrahman4u@gmail.com',
      url='https://github.com/saigege/seq2seq',
      license='GNU GPL v2',
      install_requires=install_requires,
      packages=find_packages(),
      dependency_links=['git+git://github.com/datalogai/recurrentshop.git']
)
