import cv2
import threading
from django.core.signals import request_finished
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.dispatch import receiver


@receiver(request_finished)
def afterConnection(sender, **kwargs):
    Connection.alive = False


class Connection:
    alive = True


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.worker = threading.Thread(target=self.update, args=())
        (self.grabbed, self.frame) = self.video.read()
        self.worker.start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        Connection.alive = True
        while Connection.alive:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while Connection.alive:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def index(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
