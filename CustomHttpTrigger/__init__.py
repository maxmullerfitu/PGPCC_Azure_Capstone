import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('PGPCC HTTP trigger function processed a request.')
    message = "This function is a part of PGPCC Capstone project. Execution successfull."
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. " + message)
    else:
        return func.HttpResponse(
             message + " Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
