# Sonarqube

The toolbox-Sonar image is built upon https://hub.docker.com/_/sonarqube

To install sonar-scanner to sonarqude, a package was downloaded from https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
and added to its path and then add it path environment.

Added one environment variable  ``` ENV ALLOW_EMPTY_PASSWORD='yes' ``` to fix runtime error.
