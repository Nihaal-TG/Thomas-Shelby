if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BLACK-DEVILBOY/BLACKCATROBOT /BLACKCATROBOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /BLACKCATROBOT
fi
cd /BLACKCATROBOT
pip3 install -U -r requirements.txt
echo "Starting thomas shelby....🔥"
python3 bot.py
