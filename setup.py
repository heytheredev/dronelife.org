from setuptools import setup

setup(
    name='dronelife',
    version='0.1-alpha',
    description='The dronelife.org forums',
    url='http://github.com/hecanjog/dronelife.org',
    install_requires=[
        'flask', 
        'flask-appconfig', 
        'flask-sqlalchemy', 
        'psycopg2', 
        'alembic', 
        'flask-wtf',
        'flask-login',
        'flask-admin',
        'flask-bcrypt',
        'flask-cache',
        'docopt',
        'markdown',
        'mdx_linkify',
        'boto',
        'requests',
        'mailchimp',
        'arrow'
    ],
    scripts=['bin/dronelife'],
    zip_safe=False,
)
