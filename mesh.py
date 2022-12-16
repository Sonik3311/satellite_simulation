from vao import VAO
import numpy as np

class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app)
    
    def destroy(self):
        self.vao.destroy()