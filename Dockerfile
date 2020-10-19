FROM python:3
LABEL version="1.0" \
    NAME="webserver"
RUN mkdir -p /app
COPY . /app/
WORKDIR /app
COPY MainScores.py /app/MainScores.py
COPY requirements.txt /app/requirements.txt
#RUN apt-get -y update && \
#    apt-get -qq -y install  libxpm4 libxrender1 libgtk2.0-0 libnss3\ 
#       libgconf-2-4  libpango1.0-0 libxss1 libxtst6 fonts-liberation\ 
#       libappindicator1 xdg-utils --no-install-recommends
#RUN apt-get -y install \
#               xvfb gtk2-engines-pixbuf \
#               xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable \
#               imagemagick x11-apps zip --no-install-recommends
RUN apt-get -y remove \
    #apt-get -y update  \
    #&& apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip --force --no-warn-script-location --no-cache-dir
RUN pip install --no-cache-dir -r /app/requirements.txt --no-warn-script-location --use-feature=2020-resolver
EXPOSE 8777/tcp
VOLUME /app/
CMD [ "python3", "MainScores.py" ]
#ENTRYPOINT ["/app/MainScores.py"]