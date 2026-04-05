# SentimentosAPI

API para análise de sentimentos em textos em Português.

## Funcionalidades

- **Análise de Sentimentos**: Utiliza o modelo `pysentimiento/bertweet-pt-sentiment` para classificar textos como POS (positivo), NEG (negativo) ou NEU (neutro).
- **Persistência de Dados**: Armazena as mensagens e suas análises em um banco de dados SQLite.
- **API REST**: Endpoints para criar e consultar mensagens.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/AdsonDionisio/sentimentosAPI.git
   cd sentimentosAPI
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Executando a Aplicação

Para iniciar o servidor em modo de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

## Docker

Para construir e executar a aplicação com Docker:

1. Clone o repositório:
   ```bash
   git clone https://github.com/AdsonDionisio/sentimentosAPI.git
   cd sentimentosAPI
   ```
2. Crie a imagem docker e execute o container
    ```bash
    # Build da imagem
    docker build -t sentimentosapi .

    # Executar o container
    docker run -d -p 8000:8000 --name sentimentos sentimentosapi
    ```

## Usar a ultima imagem Docker do Docker Hub

```bash
docker run -p 8000:8000 --name sentimentos adsondiego/sentimentosapi:latest
```

## Testar a API sem a analise de sentimento 

O código pode ser testado através do Swagger UI que é gerado automaticamente pelo FastAPI. Para acessá-lo, basta acessar no render o endereço https://sentimentosapi.onrender.com

Destacamos que a analise de sentimento não está sendo executada por falta de memoria no servidor gratuito do render. 


## Testes

### Criar uma Mensagem

```bash
curl -X POST "http://localhost:8000/message/" \
     -H "Content-Type: application/json" \
     -d '{"text": "Eu amo essa API!"}'
```

### Listar Mensagens

```bash
curl "http://localhost:8000/message/"
```

### Obter Mensagem por ID

```bash
curl "http://localhost:8000/message/1"
```
