import os
import burusuko

burusuko.id = os.getenv("HANDLE")
burusuko.app_password = os.getenv("APP_PASSWORD")

print(burusuko.create_record(text="hello burusuko"))

for post in burusuko.get_author_feed(burusuko.id, limit=1):
    record = post["post"]["record"]
    print(record["createdAt"], record["text"])
