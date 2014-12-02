from setuptools import setup, find_packages


setup(
    name='django-orderedmodel',
    version='0.1.0',
    description='django-orderedmodel intends to help you create Django models which can be moved up/down (or left/right) with respect to each other.',
    long_description=open('README.md').read(),
    author='kirelagin',
    author_email='kirelagin@gmail.com',
    url='https://github.com/kirelagin/django-orderedmodel.git',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
