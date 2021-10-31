# Jupyter notebook

The image is build upon https://hub.docker.com/r/jupyter/base-notebook,

To prevent token/password requirement, a jupyter-notebook-config.py file with following configuration is added to its configuration,
   ```
  c = get_config()
  c.NotebookApp.ip = '*'
  c.NotebookApp.port = 8888
  c.NotebookApp.open_browser = True
  c.NotebookApp.token = ''
   ```
