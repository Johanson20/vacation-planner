FROM python:3.9

ADD main.py .

RUN pip install --no-cache-dir googlemaps sklearn

CMD ["python", "main.py"]
