import cv2
class Animate(object):
    def __init__(self, img, size, fps):
        self.img = img
        self.size = size
        self.fps = fps
    def Video(self, filename, type1=cv2.VideoWriter_fourcc(*'DIVX')):
        out = cv2.VideoWriter(filename,type1,self.fps,self.size)
        for img in self.img:
            img1 = cv2.imread(img)
            out.write(img1)
        out.release()