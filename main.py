import pygame as pg
import moderngl as mgl
import sys

from scene import Scene
from camera import Camera
from mesh import Mesh


class Engine:
    def __init__(self, win_size=(1600,900)):
        #init pygame window
       
        pg.init()
        self.WIN_SIZE = win_size
        #prepare pygame to be render surface for OGL
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)
        
        pg.display.set_mode(self.WIN_SIZE, flags = pg.OPENGL | pg.DOUBLEBUF)

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.clock = pg.time.Clock()

        #init OGL
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        self.ctx.line_width = 3
        
        #misc variables
        self.time = 0
        self.delta_time = 0

        #camera
        self.camera = Camera(self)
        #mesh
        self.mesh = Mesh(self)
        #render scene
        self.scene = Scene(self) 

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
    
    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        self.scene.render() 
        pg.display.flip()
    
    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.clock.tick(120) # cap framerate at 120
            self.delta_time = self.clock.tick(120)

if __name__ == "__main__":
    app = Engine()
    app.run()