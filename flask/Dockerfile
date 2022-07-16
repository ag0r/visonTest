FROM python:3.10-slim
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt --no-deps
COPY . /app
ENTRYPOINT [ "python" ]
CMD ["api.py" ]
