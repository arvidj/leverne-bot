FROM python

ADD danne.json lb.txt requirements.txt util.py bot.py /bot/

WORKDIR /bot

RUN pip install -r ./requirements.txt

ENV MONGO_HOST mongo
CMD ["python", "./bot.py"]
