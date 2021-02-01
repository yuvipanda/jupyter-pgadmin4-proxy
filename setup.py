import setuptools

setuptools.setup(
    name="jupyter-pgadmin4-proxy",
    version='1.1',
    url="https://github.com/yuvipanda/jupyter-pgadmin4-proxy",
    author="manics, psychimedia & Yuvi Panda",
    description="Jupyter extension to proxy pgadmin4",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy',
        'pgadmin4',
        'gunicorn'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'pgadmin4 = jupyter_pgadmin4_proxy:setup_pgadmin4'
        ]
    },
    package_data={
        'jupyter_pgadmin4_proxy': ['icons/pgadmin4.svg'],
    },
)
