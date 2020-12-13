FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY cookbook.py ./
COPY Main.py ./
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "cookbook.py" ]