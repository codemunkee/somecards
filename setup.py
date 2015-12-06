from distutils.core import setup

setup(
    name='somecards',
    version='0.0.1',
    packages=['somecards'],
    url='',
    license='',
    author='Russ Nealis',
    author_email='codemunkee@gmail.com',
    description='API for somecards App',
    install_requires=['Flask==0.10.1',
                      'Flask-SQLAlchemy==2.1',
                      'WTForms==2.0.2',
                      'Flask-WTF==0.12']
)
