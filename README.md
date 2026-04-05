# sentimentosAPI
## Sentimentos API é uma API que faz análise de sentimentos

### Como rodar

Pode ser rodado diretamente com o uvicorn 

```bash
git clone https://github.com/AdsonDionisio/sentimentosAPI.git
cd sentimentosAPI
pip install -r requirements.txt
uvicorn app.main:app
```

## Como rodar com Docker

```bash
git clone https://github.com/AdsonDionisio/sentimentosAPI.git
cd sentimentosAPI
docker build -t sentimentosapi .
docker run -p 8000:8000 --name sentimentos sentimentosapi
```

## Como rodar a ultima imagem do dockerhub

```bash
docker run -p 8000:8000 --name sentimentos adsondiego/sentimentosapi:latest
```

## Como testar o código

O código pode ser testado através do Swagger UI que é gerado automaticamente pelo FastAPI. Para acessá-lo, basta acessar no render o endereço https://sentimentosapi.onrender.com/docs

Destacamos que a analise de sentimento não está sendo executada por falta de memoria no servidor gratuito do render.