FROM ubuntu:20.04
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update
RUN apt-get install -y wget python3-pip libarchive-zip-perl libimage-exiftool-perl unzip
#RUN apt-get intsall -y apt install python3-pip
COPY requirements.txt requirements.txt
COPY install.sh install.sh
RUN ["/bin/bash", "-c", "wget https://github.com/exiftool/exiftool/archive/refs/tags/12.23.zip"]
RUN ["/bin/bash","-c","pip install -r requirements.txt"]
RUN ["/bin/bash","-c","unzip 12.23.zip"]
RUN ["/bin/bash","-c","echo 'HCMUS-CTF{CVE_22204_1s_v3ry_1nt3r3st1ng}' > /tmp/flag.txt"]
EXPOSE 5000
COPY . .
CMD flask run --host=0.0.0.0

