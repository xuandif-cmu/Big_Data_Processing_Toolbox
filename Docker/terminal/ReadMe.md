# Terminal App
The application can be run from GKE using its pod ID, e.g.
  ```
  kubectl exec -it toolbox-terminal-[pod-id] -- bin/sh
  ```
and type 1-4 to direct to different application options, or press any other keys to terminate the toolbox application.

Code:
It added one line to keep the container running,
  ```
  CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
  ```
reference from post:
https://stackoverflow.com/questions/31870222/how-can-i-keep-a-container-running-on-kubernetes
