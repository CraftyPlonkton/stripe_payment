FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir
RUN python3 manage.py migrate
RUN python3 manage.py loaddata fixtures.json
CMD ["python3", "manage.py", "runserver", "0:8000"]