FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
# CMD ["sh"]
CMD ["python", "./jobs/manage.py", "runserver", "0.0.0.0:8000"]