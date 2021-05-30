# ctf-challenges

## Challenge: Just other CVE

## Description

Give me a zip file, I will tell you all about it, including the flag in /etc/flag.txt/

## Hint 

1. Do you know CVE-2021-22204
2. I think blog of vakzz bug hunter is very interesting


```sh
git clone https://github.com/hongson97/ctf-challenges.git
cd ctf-challenges
./install.sh
```

Replace `"http://192.168.184.132:5000/uploader"` in `templates/upload.html` with your `ip:port`.

Run with: 
```sh
flask run --host=0.0.0.0
```
