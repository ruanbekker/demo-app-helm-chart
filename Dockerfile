FROM python:3.9

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5000

ENV PYTHONPATH=/app/src
RUN pytest -v src/tests/

CMD ["python", "src/main.py"]

