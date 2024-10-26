swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'swagger',
            "route": '/swagger.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask Swagger",
        "description": "Flask Swagger Description",
        "contact": {
        "responsibleOrganization": "ME",
        "responsibleDeveloper": "Me",
        "email": "me@me.com",
        "url": "http://google.com/",
        },
        "termsOfService": "http://google.com/",
        "version": "1.0.0"
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "operationId": "getmyData"
}