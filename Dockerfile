FROM python:3.8-slim
WORKDIR /opt/app
RUN pip install --upgrade pip
RUN python -m pip install Flask
COPY . .
CMD ["python", "app/p_app.py"]