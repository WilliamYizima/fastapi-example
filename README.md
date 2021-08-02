# fast-api example

1. Create env

2. Run in bash:
```bash
make install
```
3. Run fastapi:
```bash
uvicorn main:app --reload
```

4. In this example:
- url test: http://127.0.0.1:8000/items/5?q=somequery
- parâmetro 5
- query q
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/openapi.json
- create docs

---

# Scope

- [] Database:
    - [] entrepreneur
    - [] message
    - [] status_message
    - [] segmentation
- [] entrepreneur:
    - id: id
    - name: str
    - phone_number: str
    - segmentation: str
    - historic: historic
- [] message:
    - id: id
    - created_at: date
    - name_template: str
    - name->segmantation: str
    - status_message: status_message
- [] segmantation:
    - id: id
    - name: str
    - updated_at: date
- [] status_message(enum):
    - created_at: date
    - updated_at: date
    - status:
        - not sended: str
        - sended: str
        - delivered: str
        - readed: str
- [] historic:
    - id: id
    - id_message: int
    - id_entrepreneur: int 

**Através da segmentação vai ser a flag para os fluxos**