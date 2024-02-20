FROM python:3
WORKDIR /root

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

COPY docker-test.py ./
CMD [ "python","/usr/src/app/docker-test.py"]
