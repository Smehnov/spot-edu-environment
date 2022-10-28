FROM gitpod/workspace-full:latest

RUN sudo apt-get -yqq update
RUN sudo apt-get install -yqq software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt-get -yqq update
RUN sudo apt-get install -yqq --no-install-recommends build-essential \
        ca-certificates \
        curl \
        git \
        ssh \
        libssl-dev \
        pkg-config \
        python3.8-full \
        python3.8-dev
RUN sudo apt-get clean

COPY requirements.txt requirements.txt
RUN sudo python3.8 -m pip install --upgrade pip
RUN sudo python3.8 -m pip install -r requirements.txt



RUN sudo mkdir -p /usr/local/apt-keys
RUN gpg --fetch-keys https://neilalexander.s3.dualstack.eu-west-2.amazonaws.com/deb/key.txt
RUN gpg --export 569130E8CA20FBC4CB3FDE555898470A764B32C9 | sudo tee /usr/local/apt-keys/yggdrasil-keyring.gpg > /dev/null

RUN echo 'deb [signed-by=/usr/local/apt-keys/yggdrasil-keyring.gpg] http://neilalexander.s3.dualstack.eu-west-2.amazonaws.com/deb/ debian yggdrasil' | sudo tee /etc/apt/sources.list.d/yggdrasil.list
RUN sudo apt-get update

RUN sudo apt-get install yggdrasil
COPY prepare_yggdrasil.py prepare_yggdrasil.py 
RUN sudo python3 prepare_yggdrasil.py
COPY start_yggdrasil.sh start_yggdrasil.sh 
RUN sudo chmod 777 ./start_yggdrasil.sh
ENTRYPOINT ['sudo ./start_yggdrasil.sh']
