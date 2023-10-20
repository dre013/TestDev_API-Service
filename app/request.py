import requests as rq


def request_function(questions_num: int):
    req = rq.get(f'https://jservice.io/api/random?count={questions_num}')
    response = req.json()
    return response
