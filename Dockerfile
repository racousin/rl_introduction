FROM ubuntu:20.04
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.7 python3-pip python3-dev
RUN pip3 -q install pip --upgrade
RUN apt-get install -y git
ENV TINI_VERSION v0.6.0
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN mkdir /app
RUN apt-get install -y ffmpeg zlib1g-dev libsdl2-dev xorg-dev swig cmake
COPY requirements.txt /app/requirements.txt
COPY setup.py /app/setup.py
COPY rl_introduction /app/rl_introduction
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -e .
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
