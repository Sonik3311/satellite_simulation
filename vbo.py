import numpy as np
from icosphere import icosphere
from simulator import SimulatorEngine
import configparser as cp
from simulationsettings import *

class VBO:
    def __init__(self, ctx):
        simargs = {
            "Gfactor" : G_FACTOR,
            "PlanetMass" : M,
            "PlanetRadius": R,
            "OrbitHeight" : r,
            "scale" : SCALE,
            "initPos" : POSITION,
            "initSpeed" : VELOCITY
        }
        self.simulator = SimulatorEngine(simargs)

        if SOLVER == "ODE":
            sol = self.simulator.solveODE
        elif SOLVER == "PHYS":
            sol = self.simulator.simulatePHYS

        self.vbos = {}
        self.vbos["cube"] = CubeVBO(ctx, None)
        self.vbos["sphere"] = SphereVBO(ctx, (3))
        self.vbos["trajectory"] = TrajectoryVBO(ctx, sol())
    
    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

class BaseVBO:
    def __init__(self, ctx, args):
        self.ctx = ctx
        self.vbo = self.get_vbo(args)
        self.format: str = None
        self.attribute: list = None
    
    def get_vertex_data(self,args): ...

    def get_vbo(self, args):
        vertex_data = self.get_vertex_data(args)
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    
    def destroy(self):
        self.vbo.release()

#Test cube model
class CubeVBO(BaseVBO):
    def __init__(self, ctx, args):
        super().__init__(ctx, args)
        self.format = '3f 3f'
        self.attribute = ['in_normal','in_position']
    
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self,args):                                 
        vertices = [(-1,-1, 1), (1,-1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1,-1), (-1,-1,-1), (1,-1,-1), (1, 1,-1)]
        
        
        indices = [(0,2,3), (0,1,2),
                   (1,7,2), (1,6,7),
                   (6,5,4), (4,7,6),
                   (3,4,5), (3,5,0),
                   (3,7,4), (3,2,7),
                   (0,6,1), (0,5,6)]
        
        normals = []
        for triangle in indices:
            v1 = np.array(vertices[triangle[0]])
            v2 = np.array(vertices[triangle[1]])
            v3 = np.array(vertices[triangle[2]])
            #print(v1)
            e1 = v2 - v1
            e2 = v3 - v1
            cp = np.cross(e2, e1)
            normal = cp / np.linalg.norm(cp)
            normals.append( (normal[0],normal[1],normal[2]) )
            normals.append( (normal[0],normal[1],normal[2]) )
            normals.append( (normal[0],normal[1],normal[2]) )
        
        normals = np.array(normals, dtype='f4')
        vertex_data = self.get_data(vertices, indices)
        vertex_data = np.hstack([normals, vertex_data])
        return vertex_data

class SphereVBO(BaseVBO):
    def __init__(self, ctx, args):
        super().__init__(ctx, args)
        self.format = '3f'
        self.attribute = ['in_position']
    
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')
    
    def get_vertex_data(self,args): 
        radius = args
        vertices, indices = icosphere(3)

        for i in range(len(vertices)):
            for j in range(3):
                vertices[i][j] = vertices[i][j] * radius

        vertex_data = self.get_data(vertices,indices)
        return vertex_data

class TrajectoryVBO(BaseVBO):   
    def __init__(self, ctx, args):
        super().__init__(ctx, args)
        self.format = '3f'
        self.attribute = ['in_position']
    
    @staticmethod
    def get_data(vertices, indices):
        return np.array(vertices, dtype='f4')
    
    def get_vertex_data(self,args): 
        #vertices = []
        indices  = []
        vertices, _ = args
        for i in range(len(vertices)-1):
            indices.append((i,i+1))
        vertex_data = self.get_data(vertices,indices)
        return vertex_data


                
    