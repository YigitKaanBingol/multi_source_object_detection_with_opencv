
class Camera:
    def __init__(self, id: int, protocol:str,username: str, password: str, url:str):
        
        self.id = id
        self.protocol=protocol
        self.cam_username = username
        self.cam_password = password
        self.cam_url = url
        
        self.source=self.protocol+"://"+self.cam_username+":"+self.cam_password+"@"+self.cam_url
        