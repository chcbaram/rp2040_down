from setuptools import setup, find_packages


setup_requires = [
    ]

install_requires = [
    'pyserial',
    ]

setup(
    name="rp2040down",
    version="1.0.0",
    packages=find_packages(),
    author="baram",
    author_email="chcbaram@gmail.com",
    description="RP2040 Download Tools",
    keywords="",
    url="https://github.com/chcbaram/rp2040_down",
    install_requires=install_requires,
    
    package_data={'rp2040down/tools': ['*']},
    include_package_data=True,

    entry_points={
      "console_scripts":[
        "rp2040down=rp2040down:main",
        ],
    },
)