Step_1
Сборка image на хосте с Windows (архитектура amd64):
docker build --platform linux/amd64 -t paulbaz87/p_app:v1 .

Сборка image на хосте с MacOS (архитектура arm64):
docker build  --platform linux/arm64 -t paulbaz87/p_app:v1 .

Step_2
Запуск контейнера:
docker run -d -p 8000:8000 paulbaz87/p_app:v1

Step_3
Доступ в приложение в контейнере:
http://localhost:8000/health/

Step_4
Push на Dockerhub (в предсозданный репозиторий p_app):
docker login
docker push paulbaz87/p_app:v1

Step_5
Push на Github:
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/PaulBaz87/otus_docker.git
git push -u origin main
