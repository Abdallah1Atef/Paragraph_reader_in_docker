FROM ubuntu
WORKDIR /t2
COPY  t2.py .
RUN pip install nltk
CMD [ "ubuntu","t2.py" ]
