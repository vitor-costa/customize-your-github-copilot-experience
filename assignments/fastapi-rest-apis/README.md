# 📘 Assignment: APIs REST com FastAPI

## 🎯 Objective

Construa APIs REST usando o framework FastAPI e modelos Pydantic. Os estudantes aprenderão a definir rotas, validar dados de entrada, e implementar operações CRUD básicas para um recurso simples.

## 📝 Tasks

### 🛠️	Criar uma API REST básica

#### Description

Implemente um serviço HTTP em Python usando FastAPI que exponha endpoints para criar, ler, atualizar e excluir (CRUD) um recurso chamado "Item". Use Pydantic para validar os modelos de entrada/saída e mantenha os dados em uma estrutura em memória (por exemplo, um dicionário) para simplicidade.

#### Requirements
Completed program should:

- Definir um Pydantic model para o recurso Item (por exemplo: id: int, name: str, description: Optional[str])
- Implementar endpoints REST:
  - GET /items — lista todos os itens
  - GET /items/{id} — pega um item por id
  - POST /items — cria um novo item
  - PUT /items/{id} — atualiza um item existente
  - DELETE /items/{id} — remove um item
- Usar validação de entrada com Pydantic e retornar códigos HTTP apropriados (200/201/404/400)
- Documentação automática disponível em /docs (Swagger UI) e /redoc
- Incluir instruções de execução e dependências no repositório da tarefa

#### Example

Fluxo simplificado:

```
POST /items  { "name": "Caneca", "description": "Caneca vermelha" }
Response 201 { "id": 1, "name": "Caneca", "description": "Caneca vermelha" }

GET /items
Response 200 [ { "id": 1, "name": "Caneca", "description": "Caneca vermelha" } ]
```

---

## Como rodar (localmente)

1. Crie um ambiente virtual Python (recomendado)
2. Instale dependências:

```
pip install -r requirements.txt
```

3. Execute o servidor (modo desenvolvimento):

```
uvicorn starter-code:app --reload
```

4. Abra http://127.0.0.1:8000/docs para ver a documentação interativa.

---

## Entregáveis

- Código-fonte dentro desta pasta (`starter-code.py`)
- Um breve README com instruções (este arquivo)
