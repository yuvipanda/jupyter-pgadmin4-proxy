# jupyter-pgadmin4-proxy

**jupyter-pgadmin4-proxy** leverages jupyter-server-proxy to proxy Pgadmin4 applications inside a Jupyter server.

If you have a JupyterHub deployment, jupyter-pgadmin4-proxy can take advantage of JupyterHub's existing authenticator and spawner to launch Pgadmin4 applications in users' Jupyter environments.

## Credit

[@manics](https://github.com/manics) and [@psychemedia](https://github.com/psychemedia) did most of the
work here.

## Installation

### Pre-reqs

#### Install pgadmin4-server
[Download](https://rstudio.com/products/pgadmin4/download-server/) the corresponding package for your platform.

### Install jupyter-pgadmin4-proxy

Install the library:
```
pip install jupyter-pgadmin4-proxy
```

### Setup default credentials

We use pgadmin4 in server mode, since desktop-mode doesn't allow it to be run under a URL prefix
(a requirmenet for use with jupyter-server-proxy). This requires a default username and password.
You *need* to set it up manually in your container image (or other system) before users can
access pgadmin4.

```bash
PGADMIN_SETUP_EMAIL=<email> PGADMIN_SETUP_PASSWORD=<password> python3 $(python3 -c 'import site; print(site.getsitepackages()[0])')/pgadmin4/setup.py
```

This will setup the root user name in the session database under `~/.pgadmin4`
