Python:
pip freeze > requirements.txt


Linux:
docker system prune -a
docker login --username=ofirsh11
docker build . -f Dockerfile
TAG=$(docker images |head -2 | grep -v REPOSITORY |awk '{ print $3 }')
docker tag $TAG ofirsh11/worldoffames
docker push ofirsh11/worldoffames

#save
docker save worldoffames > worldoffames.tar
docker load --input worldoffames.tar

#run
docker run -d -it -p 8777:8777 -v /dev:/tmp --name worldoffames ofirsh11/worldoffames

docker run -d -it --name worldoffames ofirsh11/worldoffames

docker-compose up -d

Windows:
    Get-Content Dockerfile | docker build -


------------
GIT:
    echo " " > .gitignore
    echo "# WorldOfGames" >> README.md
    git init
    git commit -am "first commit"
    git add .
    git add *
    git add .gitignore
    git branch -M main
    git remote add origin https://github.com/ofirshi/WorldOfGames.git
    git push -u origin main


    git remote add origin https://github.com/ofirshi/WorldOfGames.git
    git branch -M main
    git push -u origin main