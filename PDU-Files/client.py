
from typing import Dict
from quic import ChatQuicConnection, QuicStreamEvent
import pdu


async def chat_client_proto(scope:Dict, conn:ChatQuicConnection):
    
    print('Hello The Client Has Connected...')
    while True:
        msg = input("Enter Message: ")
        datagram = pdu.Datagram(pdu.MSG_TYPE_DATA, msg)
        
        new_stream_id = conn.new_stream()

        qs = QuicStreamEvent(new_stream_id, datagram.to_bytes(), False)
        await conn.send(qs)
        message:QuicStreamEvent = await conn.receive()
        dgram_resp = pdu.Datagram.from_bytes(message.data)
        print('[cli] received message: ', dgram_resp.msg)
