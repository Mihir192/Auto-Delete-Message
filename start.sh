echo "Cloning Repo...."
git clone https://github.com/Mihir192/mdisk-search-bot.git /mdisk-search-bot
cd /mdisk-search-bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
