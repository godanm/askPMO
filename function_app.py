import azure.functions as func
import logging
from flask import Flask, jsonify, request

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="askPMO")
def askPMO(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.route(route="knowledgebasequery")
def knowledgebasequery(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    try:
        req_body = req.get_json()
        logging.info(str(req_body))
        response = knowledge_base_query(req_body)        
        return response
    except Exception as e:
        return jsonify(str(e)),500
