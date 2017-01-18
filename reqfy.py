from sanic import Sanic
from sanic.response import HTTPResponse, json_dumps
from sanic.request import Request

app = Sanic()


def json(body, status=200, headers=None):
    return HTTPResponse(json_dumps(body, indent=4), headers=headers, status=status, content_type="application/json")


@app.route("/")
async def test(request: Request):
    return json({
        'method': request.method,
        'url': request.url,
        'query_string': request.query_string,
        'headers': dict(request.headers),
        "body": request.body,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
