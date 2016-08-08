from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import os

version = __import__('beehve').__version__


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]


def _reqs(*f):
    return [
        _pip_requirement(r) for r in (
            strip_comments(l) for l in open(
                os.path.join(os.getcwd(), 'requirements', *f)).readlines()
        ) if r]


def reqs(*f):
    return [req for subreq in _reqs(*f) for req in subreq]

install_requires = []
install_requires = reqs('default.txt')


# -*- Extras -*- 
extra = {}

def extras(*p):
    return reqs('extras', *p)

features = set([
    'postgres', 
])
extras_require = dict((x, extras(x + '.txt')) for x in features)
extra['extras_require'] = extras_require

# -*- %%% -*-

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

setup(
    name="beehve",
    version=version,
    url='http://github.com/powellc/beehve',
    license='BSD',
    platforms=['OS Independent'],
    description="An beehve for django applications.",
    author="Colin Powell",
    author_email='colin.powell@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'beehve': 'beehve',
        'beehve/templates': 'beehve/templates',
    },
    entry_points={
        'console_scripts': [
            'beehve = beehve.manage_beehve:main',
        ],
    },
    **extra
)
