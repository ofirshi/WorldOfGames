FROM python:3
LABEL version="1.0"
RUN mkdir -p /app
COPY . /app/
WORKDIR /app
COPY MainScores.py /app/MainScores.py
COPY requirements.txt /app/requirements.txt
RUN apt-get -y remove \
    #apt-get -y update  \
    #&& apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip --force --user --no-warn-script-location
RUN pip install --no-cache-dir -r /app/requirements.txt --user --no-warn-script-location --use-feature=2020-resolver
EXPOSE 8777/tcp
VOLUME /app/
CMD [ "python3", "MainScores.py" ]