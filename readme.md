## setup

### bash file

Create bash file in :
> /home/pi/startPiHatTicker.sh

```
#!/bin/dash

REPO_DIR=/home/pi/piHatTicker/

if [ ! -d $REPO_DIR ]; then
    echo Clone repo
    git clone https://github.com/Gus-The-Forklift-Driver/piHatTicker $REPO_DIR
fi


echo - go to repo
cd $REPO_DIR

echo - clone repo
git pull origin master

echo - run script
python3 $REPO_DIR/main.py
```


### service
create service (for automatic execution at startup) in 
>/etc/systemd/system/pihatticker.service

```
[Unit]
Description=piHatTicker service
After=syslog.target
After=network.target

[Service]
# Modify these two values    ^`^k   ^`^kand uncomment them if you have
# repos with lots of files and get to HTTP error 500 because of that
###
# LimitMEMLOCK=infinity
# LimitNOFILE=65535
RestartSec=2s
Type=simple
User=pi
Group=pi
WorkingDirectory=/home/pi
ExecStart=/home/pi/startPiHatTicker.sh
Restart=always
Environment=USER=pi
HOME=/home/pi

[Install]
WantedBy=multi-user.target

```

enable service :
> sudo systemctl enable comunic.service

then start it :
> sudo systemctl start comunic.service

(this is optional as it will start at next reboot)