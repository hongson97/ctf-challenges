
wget https://github.com/exiftool/exiftool/archive/refs/tags/12.23.zip
sudo apt install unzip
sudo apt install python3
sudo apt-get install -y libarchive-zip-perl
unzip 12.23.zip
rm 12.23.zip
pip3 install -r requirements.txt
echo "HCMUS-CTF{CVE_22204_1s_v3ry_1nt3r3st1ng}" > /tmp/flag.txt
