FROM python:3
LABEL version="1.0"
RUN mkdir -p /tmp
COPY . /tmp/
WORKDIR /tmp
COPY MainScores.py /tmp/MainScores.py
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update -y \
    #&& apt-get install -y --no-install-recommends gcc \
    && apt-get remove \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip --force --user --no-warn-script-location
RUN pip install --no-cache-dir -r /tmp/requirements.txt --user --no-warn-script-location --use-feature=2020-resolver
EXPOSE 8777/tcp
VOLUME /tmp/
CMD [ "python3", "MainScores.py" ]
