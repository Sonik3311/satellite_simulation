from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.trajectory = None
        self.load()
    
    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(Sphere(app,pos=(0,0,0)))
        self.trajectory = Trajectory(app,pos=(0,0,0), color=(1,1,1))
    
    def render(self):
        self.render3D()
        self.renderLine()

    def render3D(self):
        for obj in self.objects:
            obj.render(None)
            self.app.ctx.polygon_offset = 1.0, 1.0
            obj.color = (0,0,0)
            obj.render(mgl.LINES)
            self.app.ctx.polygon_offset = 0, 0
            obj.color = (1,1,1)

    def renderLine(self):
        self.trajectory.render(mgl.LINE_STRIP)