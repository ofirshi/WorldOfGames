# WorldOfGames

Python:
pip install -r requirements.txt --user


#run
docker volume create app
docker run -d -it -p 8777:8777 -v "$(pwd)":/app --name worldoffames ofirsh11/worldoffames


docker-compose up -d
