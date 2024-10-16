FROM python:3.11

WORKDIR /app

COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "fastapi", "dev", "app/main.py" , "--host", "0.0.0.0", "--port", "8000"]
