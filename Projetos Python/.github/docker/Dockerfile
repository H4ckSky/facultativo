FROM python:3

WORKDIR C:\Users\lhuan\OneDrive\Documentos\GitHub\facultativo\Projetos Python\.github\docker

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]