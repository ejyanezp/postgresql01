import lambda_function


class Context:
    pass


ctxt = Context()
# Contrato de entrada
event = {
    "id": "7e7ac567-29dd-4888-9371-0db94e37b297"
}

result = lambda_function.lambda_handler(event, ctxt)
print(result)
