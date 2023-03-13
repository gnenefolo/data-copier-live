FROM  python:3.7

RUN apt install git

WORKDIR /app
RUN git clone https://github.com/gnenefolo/data-copier-live.git

WORKDIR /app/data-copier-live
RUN pip install -r requirements.txt

CMD ["python", "app.py", "dev"]