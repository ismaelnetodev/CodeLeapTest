# API de Posts - Django Rest Framework

Este projeto é uma API RESTful criada com Django e Django Rest Framework (DRF) para gerenciar posts no estilo de microblog.

## 🚀 **Tecnologias utilizadas**
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

## 📚 **Endpoints**
- **GET `/api/`**: Retorna a lista de posts.
- **POST `/api/`**: Cria um novo post.
- **PATCH `/api/{id}/`**: Atualiza parcialmente um post (somente `title` e `content`).
- **DELETE `/api/{id}/`**: Exclui um post.
