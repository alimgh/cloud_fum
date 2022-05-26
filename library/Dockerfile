FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUMBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /app
RUN cd /app
EXPOSE 8001