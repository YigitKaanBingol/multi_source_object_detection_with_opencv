class CamThread:
    def __init__(self,camera,queue_cam) -> None:
        self.camera=camera
        self.queue_cam=queue_cam