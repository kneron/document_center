# Kneron Docker Hub Service

*2023/06/28*

Here is the Kneron docker hub service usage

## Docker login

1. Ask Admin (Jenna WU jenna@kneron.us) create kneron docker account
2. Setup Daemon.json in your local machine. In `/etc/docker/daemon.json`, add the server's url in `insecure-registries` to allow http connection.

     ```json
     {
         "insecure-registries": [
            "services.kneron.com:5000"
         ]
     }
     ```
3. Restart docker, check if it successfully set by `docker info` 

     ```shell
     sudo systemctl daemon-reload
     sudo systemctl restart docker
     ```
4. Log in kneron docker
     ```shell
     docker login services.kneron.com:5000
     ```
     enter username and password  
5. Docker push command

     ```shell
     docker tag image_ID services.kneron.com:5000/myimage:versionID  
     docker push services.kneron.com:5000/myimage:versionID
     ```
6. Docker pull command

     ```shell
     docker pull services.kneron.com:5000/myimage:versionID
     ```

## Reference

* https://www.blackvoid.club/private-docker-registry-with-portainer/
* https://gitlab.kneron.tw/PF/kneron_dockerhub_service/-/blob/main/tutorial/readme.md
