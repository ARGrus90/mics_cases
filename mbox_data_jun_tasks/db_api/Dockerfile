FROM python:3.9
COPY web_api /web_api
WORKDIR /web_api
RUN pip install --no-cache-dir --upgrade -r /web_api/requirements.txt
CMD ["uvicorn", "main:app", "--host","0.0.0.0","--port", "8000"]
