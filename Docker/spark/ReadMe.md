# toolbox-spark
Spark is built directly using https://hub.docker.com/r/bitnami/spark.

In this project, to facilitate easily deploying multiple worker, an official package was used, [Bitnami Apache Spark Chart GitHub repository](https://github.com/bitnami/charts/tree/master/bitnami/spark), referenced from the "How to deploy Apache Spark in Kubernetes?" section in [bitnami/spark](https://hub.docker.com/r/bitnami/spark) image page. Values in the value.yaml are modified to change its port. To use this package, helm has to be installed, then run with
    ```
    helm install spark ./spark
    ```
