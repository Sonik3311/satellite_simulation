import moderngl as mgl
import numpy as np
import glm
from time import time
import struct

class BaseModel:
    def __init__(self, app, vao_name, pos=(0,0,0)):
        self.app = app
        self.position = pos
        self.m_model = self.get_model_matrix()
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera
    
    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()

        m_model = glm.translate(m_model, self.position)
        return m_model
    
    def render(self,mode):
        self.update()
        self.vao.render(mode)

class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', pos=(0,0,0), color=(1,0,1)):
        super().__init__(app,vao_name,pos)
        self.color = color
        #print(self.color)
        self.on_init()
    
    def on_init(self):
        #self.program['camPos'].write(self.camera.position)
        self.program['color'].write(glm.vec3(self.color))
        #matrix view projection
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
    
    def update(self):
        self.program['color'].write(glm.vec3(self.color))
        #self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

class Sphere(BaseModel):
    def __init__(self, app, vao_name='sphere', pos=(0,0,0), color=(1,0,1)):
        super().__init__(app,vao_name,pos)
        self.color = color
        #print(self.color)
        self.on_init()

    def on_init(self):
        #self.program['camPos'].write(self.camera.position)
        self.program['color'].write(glm.vec3(self.color))
        #matrix view projection
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
    
    def update(self):
        self.program['color'].write(glm.vec3(self.color))
        #self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)


class Trajectory(BaseModel):
    def __init__(self, app, vao_name='trajectory', pos=(0,0,0), color=(1,0,1)):
        super().__init__(app,vao_name,pos)
        self.color = color
        self.time = 0
        self.on_init()

    def on_init(self):
        #self.program['camPos'].write(self.camera.position)
        self.program['color'].write(glm.vec3(self.color))
        #matrix view projection
        #self.program['time'].write(struct.pack('!f', self.time))
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
    
    def update(self):
        #self.program['color'].write(glm.vec3(self.color))
        #self.program['camPos'].write(self.camera.position)
        #print(int(time())%100)
        #self.program['time'].write(struct.pack('!f', self.time))
        #self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        self.time += 0.000001



