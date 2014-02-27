import optionchain

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=optionchain.__app_name__,
    version=optionchain.__version__,
    description=optionchain.__description__,
    author=optionchain.__author__,
    author_email=optionchain.__author_email__,
    packages=['optionchain'],
    install_requires=['requests==2.0.1', 'pandas'],
    url=optionchain.__app_url__,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'License :: Freeware',
    ),
    download_url=optionchain.__download_url__,
)