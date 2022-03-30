FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ivan-bank
WORKDIR /ivan-bank
COPY requirements.txt /ivan-bank
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /ivan-bank
EXPOSE 3366
CMD [ "python", "main.py" ]