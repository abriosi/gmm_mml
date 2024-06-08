from setuptools import setup

setup(name='gmm-mml',
      version='0.12',
      description='Unsupervised cluster selection for finite guassian mixture models',
      url='https://github.com/abriosi/gmm-mml/',
      author='abriosi',
      license='MIT',
      packages=['gmm_mml'],
      install_requires=[
          'numpy',
          'scipy',
          'scikit-learn',
      ],
      zip_safe=False)
