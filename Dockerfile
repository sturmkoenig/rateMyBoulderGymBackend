FROM ubuntu:22.04
RUN apt-get update && \
  apt-get install --no-install-recommends -y gcc python3-pip pkg-config python3-dev build-essential libmysqlclient-dev neovim&& \
  apt-get clean && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["python3","src/main.py"]
