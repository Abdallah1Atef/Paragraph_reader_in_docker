FROM python:alpine
WORKDIR /cloudassignment
COPY . /cloudassignment/
RUN pip install nltk
CMD [ "python","t2.py" ]
