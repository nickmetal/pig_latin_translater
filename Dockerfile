FROM python3.7:alpine

LABEL Name=aiohttp-example Version=0.0.1
EXPOSE 8000

WORKDIR /opt/app
ADD . /opt/app

# Using pip:
# TODO add make reqst installation cmd
RUN python -m pip install -r requirements.txt

# TODO add make run cmd
CMD ["python", "app.py"]
