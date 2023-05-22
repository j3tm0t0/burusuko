# burusuko
python module for Bluesky Social
minimum API is defined.

## usage
```python:test.py
import os
import burusuko

burusuko.id = os.getenv("HANDLE")
burusuko.app_password = os.getenv("APP_PASSWORD")

print(burusuko.create_record(text="hello burusuko"))

for post in burusuko.get_author_feed(burusuko.id, limit=1):
  record = post["post"]["record"]
  print(record["createdAt"], record["text"])
```

```
$ export HANDLE="xxxxxxx@bsky.social"
$ export APP_PASSWORD="xxxxxxxxxxxxxxxx" # create one from Settings > App paswords menu
$ python test.py
{'uri': 'at://did:plc:rw3rpuxdvnlzvaxaewrku77y/app.bsky.feed.post/3jwc7yx6e6e22', 'cid': 'bafyreihx3xb6fpc6tlr5hpuhyuafieuhq4hv4sdaib4rxq4n7n5cktkf24'}
2023-05-22T14:24:52Z hello burusuko
```

## Reference
- [SwiftでBlueskyに投稿を行う](https://qiita.com/masaru-honma/items/ef27553c51cbdfb2ebca)
- [Bluesky/AT Protocol: cURL API Interaction Cheatsheet](https://gist.github.com/pojntfx/72403066a96593c1ba8fd5df2b531f2d)
