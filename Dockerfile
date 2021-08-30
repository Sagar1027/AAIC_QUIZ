FROM python:3.7

ADD quiz.py quiz.json /

RUN pip install pip

CMD ["python","./quiz.py"]