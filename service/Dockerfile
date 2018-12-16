FROM python:3.6-alpine

WORKDIR /app

# install dependencies for app
COPY requirements.py /app/requirements.txt
RUN pip install -r /app/requirements.txt

# copy source code 
COPY wordgen.py /app/wordgen.py
COPY api.py /app/api.py

# copy data
COPY data/words.txt /app/data/words.txt

# expose ports
EXPOSE 5000
EXPOSE 8080

# run app
CMD ["python", "-u", "api.py"]



