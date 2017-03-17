from setuptools import setup

setup(
    name='django-migrate-sql-comments',
    description='A Django app providing a management command to generate SQL to add comments to your DB from the model data',
    packages=['sqlcomment'],
    platforms='any',
)
