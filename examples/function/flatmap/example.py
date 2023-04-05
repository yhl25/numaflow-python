from typing import List

from pynumaflow.function import Messages, Message, Datum, UserDefinedFunctionServicer


def my_handler(keys: List[str], datum: Datum) -> Messages:
    val = datum.value
    _ = datum.event_time
    _ = datum.watermark
    print("keys are... ")
    for k in keys:
        print("key - ", k)
    strs = val.decode("utf-8").split(",")
    messages = Messages()
    for s in strs:
        messages.append(Message.to_vtx(keys, str.encode(s)))
    return messages


if __name__ == "__main__":
    print("flat map udf was invoked")
    grpc_server = UserDefinedFunctionServicer(map_handler=my_handler)
    grpc_server.start()
