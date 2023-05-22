import os
import json
import urllib.request
import datetime
from pprint import pprint

id = None
app_password = None
session = None

endPoint = "https://bsky.social/xrpc/"

methods = {
    "createSession": "com.atproto.server.createSession",
    "createRecord": "com.atproto.repo.createRecord",
    "getAuthorFeed": "app.bsky.feed.getAuthorFeed",
}


def create_session(id, app_password):
    data = {"identifier": id, "password": app_password}
    headers = {"content-type": "application/json"}

    url = endPoint + methods["createSession"]
    req = urllib.request.Request(
        url,
        data=bytes(json.dumps(data), encoding="utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            return json.loads(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(e)
        return None


def create_record(text, session=None, createdAt=datetime.datetime.now()):
    if session is None:
        session = create_session(id, app_password)
    data = {
        "repo": session["did"],
        "collection": "app.bsky.feed.post",
        "record": {
            "text": text,
            "createdAt": createdAt.isoformat(timespec="seconds") + "Z",
        },
    }
    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {session['accessJwt']}",
    }
    url = endPoint + methods["createRecord"]
    req = urllib.request.Request(
        url,
        data=bytes(json.dumps(data), encoding="utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            return json.loads(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(e)
        return None


def get_author_feed(handle, session=None, limit=100):
    if session is None:
        session = create_session(id, app_password)
    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {session['accessJwt']}",
    }
    url = f"{endPoint + methods['getAuthorFeed']}?actor={handle}&limit={limit}"
    req = urllib.request.Request(
        url,
        headers=headers,
    )
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            return json.loads(body.decode("utf-8")).get("feed", [])
    except urllib.error.HTTPError as e:
        print(e)
        return None


if __name__ == "__main__":
    id = os.getenv("HANDLE")
    app_password = os.getenv("APP_PASSWORD")
    print(create_record("hello burusuko"))
    for post in get_author_feed(id, limit=3):
        pprint(post)
