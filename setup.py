import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.IlFeeWaiver',
      version='2.2.2',
      description=('Fee waiver'),
      long_description='> [!NOTE]  \r\n> This is a duplicate of [IllinoisLegalAidOnline/docassemble-FeeWaiver](https://github.com/IllinoisLegalAidOnline/docassemble-FeeWaiver), and it appeared to be significantly out of date when archived.\r\n\r\n# docassemble.IlFeeWaiver\r\n\r\nApplication for Fee Waiver\r\n\r\n## Author\r\n\r\nQuinten Steenhuis / Matt Newsted\r\n\r\nqsteenhuis@suffolk.edu, mnewsted@illinoislegalaid.org\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Quinten Steenhuis / Matt Newsted',
      author_email='qsteenhuis@suffolk.edu mnewsted@illinoislegalaid.org',
      license='The MIT License',
      url='http://www.illinoislegalaid.org',
      packages=find_namespace_packages(),
      install_requires=['docassemble.AssemblyLine @ git+https://github.com/SuffolkLITLab/docassemble-AssemblyLine.git@main', 'docassemble.EFSPIntegration @ git+https://github.com/SuffolkLITLab/docassemble-EFSPIntegration.git@main', 'docassemble.PovertyScale>=2024.0.0'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/IlFeeWaiver/', package='docassemble.IlFeeWaiver'),
     )

