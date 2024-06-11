import json
MSG_TYPE_DATA = 0x00
MSG_TYPE_ACK = 0x01
MSG_TYPE_DATA_ACK = MSG_TYPE_DATA | MSG_TYPE_ACK

class Datagram:
    def __init__(self, mtype: int, msg: str, sz: int = 0):
        self.mtype = mtype
        self.msg = msg
        self.sz = len(self.msg)
        
    def to_json(self):
        return json.dumps(self.__dict__)    
    
    @staticmethod
    def from_json(json_str):
        return Datagram(**json.loads(json_str))
    
    def to_bytes(self):
        # Ensure that self.msg is encoded to bytes
        return bytes([self.mtype]) + self.msg.encode('utf-8')
    
    @staticmethod
    def from_bytes(json_bytes):
        mtype = json_bytes[0]
        msg = json_bytes[1:]
        return Datagram(mtype, msg.decode('utf-8'))
