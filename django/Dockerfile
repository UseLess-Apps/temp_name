FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt update && apt upgrade
RUN pip install -r requirements.txt
# COPY . .

EXPOSE 8000
# CMD ["sh"]
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]