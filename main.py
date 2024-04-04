import lambda_function


class Context:
    pass


ctxt = Context()
# Contrato de entrada
event = {
    'id': '50fe515a-409e-4602-afb6-4d3aabc48040'
}

result = lambda_function.lambda_handler(event, ctxt)
print(result)
