from time import sleep

from obswebsocket import obsws, requests  # noqa: E402

def recording(time):
    host = "localhost"
    port = 4444

    ws = obsws(host, port)
    ws.connect()
    ws.call(requests.StartRecording())
    sleep(time)
    ws.call(requests.StopRecording())

    ws.disconnect()