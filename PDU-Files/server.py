from typing import Coroutine, Dict
from quic import ChatQuicConnection, QuicStreamEvent
import pdu

async def chat_server_proto(scope: Dict, conn: ChatQuicConnection):
    async def receive_and_respond():
        while True:
            # Receive message from any connected client
            message: QuicStreamEvent = await conn.receive()
            
            # Decode the received datagram
            dgram_in = pdu.Datagram.from_bytes(message.data)
            print("[svr] received message:", dgram_in.msg)
            
            stream_id = message.stream_id
            
            # Take response message from user via console input
            response_msg = input("Enter response message: ")
            
            # Create a response datagram with the user input message
            dgram_out = pdu.Datagram(pdu.MSG_TYPE_DATA_ACK, response_msg)
            
            # Encode the response datagram
            rsp_msg = dgram_out.to_bytes()
            
            # Create a stream event for sending the response
            rsp_event = QuicStreamEvent(stream_id, rsp_msg, False)
            
            # Send the response to the client
            await conn.send(rsp_event)

    await receive_and_respond()
