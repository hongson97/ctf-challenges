
wget https://github.com/exiftool/exiftool/archive/refs/tags/12.23.zip
sudo apt install unzip
sudo apt install python3
sudo apt-get install python3-venv
sudo apt-get install -y libarchive-zip-perl
unzip 12.23.zip
rm 12.23.zip
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
