Сборка image:/n
docker build --platform linux/amd64 -t paulbaz87/p_app:v1 .

Запуск контейнера:
docker run -d -p 8000:8000 p_app:v1

Push на Dockerhub (в предсозданный репозиторий p_app):
docker login
docker push paulbaz87/p_app:v1

Push на Github:
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/PaulBaz87/otus_docker.git
git push -u origin main
