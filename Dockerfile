FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN python3 manage.py migrate
RUN python3 manage.py loaddata fixtures.json
RUN python3 manage.py collectstatic
CMD ["python3", "manage.py", "runserver", "0:8000", "--insecure"]
