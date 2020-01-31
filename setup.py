from setuptools import find_packages, setup

with open('README.md') as f:
  readme = f.read()

setup(
  name='npuzzle',
  version='0.1',
  description=readme,
  author='mtrazzi & kcosta',
  url='https://github.com/kcosta/N-Puzzle',
  packages=find_packages(exclude=('tests', 'docs'))
)
