FROM python:3

WORKDIR C:\Users\lhuan\OneDrive\Documentos\GitHub\facultativo\.github\docker

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
CMD [ "fastapi", "dev", "main.py", "--port", "80" ]