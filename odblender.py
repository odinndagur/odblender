import bpy
from math import sqrt
import collections

Point = collections.namedtuple('Point',['x','y','z'],defaults=[0,0,0])

class Vector(Point):
    def __mul__(self,fac):
        return Vector(self.x * fac, self.y * fac, self.z * fac)
    
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

def select_all():
    if bpy.context.object:
        if bpy.context.object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
    # select all objects
    bpy.ops.object.select_all(action='SELECT')

def deselect_all():
    if bpy.context.object:
        if bpy.context.object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
    # select all objects
    bpy.ops.object.select_all(action='DESELECT')

def delete_all():
    if bpy.context.object:
        if bpy.context.object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
    # select all objects
    bpy.ops.object.select_all(action='SELECT')
    # delete all selected objects
    bpy.ops.object.delete()

def set_cursor(position:Point):
    bpy.context.scene.cursor.location = position

def reset_cursor():
    bpy.context.scene.cursor.location = (0,0,0)


def make_plane(
        w = 251,
        h = 251,
        scale = 1,
        startpos = Point(),
        xindex=0,
        yindex=0,
        heights = None,
        name = None,
    ):

    if not heights:
        heights = [[0]*h]*w #initialize heights with all zeroes
    plane_name = name if name else 'x{x}y{y}_plane_width{w}_height{h}_scale{scale}'.format(x=xindex,y=yindex,w=w,h=h,scale=scale)
    xmin = startpos.x + xindex * (w-1)
    ymin = startpos.y + yindex * (h-1)
    edges = []
    faces = []
    
    if(xindex == 9):
        xmin -= 1
    if(yindex == 9):
        ymin -= 1
    vertices = [((x-xmin)*scale,(y-ymin)*scale,heights[x][y]*scale) for x in range(xmin,xmin+w) for y in range(ymin,ymin+h)]
    vertexIndex = 0
    sz = int(sqrt(len(vertices)))
    for y in range(sz):
        for x in range(sz):
            if (x < sz - 1) and (y < sz - 1):
                # faces.append((vertexIndex,vertexIndex+width+1,vertexIndex+width)) #unity mode
                # faces.append((vertexIndex + width + 1, vertexIndex, vertexIndex+1)) #unity mode
                faces.append((vertexIndex+sz,vertexIndex+sz+1,vertexIndex)) #blender mode
                faces.append((vertexIndex+1, vertexIndex,vertexIndex + sz + 1)) #blender mode
                
            vertexIndex+=1


    new_mesh = bpy.data.meshes.new(plane_name)
    new_mesh.from_pydata(vertices, edges, faces)
    new_mesh.update()
    # make object from mesh
    new_object = bpy.data.objects.new(plane_name, new_mesh)
    # make collection
    new_collection = bpy.data.collections.get('new_collection')
    if not new_collection:
        new_collection = bpy.data.collections.new('new_collection')
        bpy.context.scene.collection.children.link(new_collection)
    new_collection.objects.link(new_object)
    new_object.select_set(True)
    #new_object.location.x -= xindex * scale * 3
    #new_object.location.y -= yindex * scale * 3
    new_object.location = (xindex*w*scale - scale*xindex,yindex*h*scale - scale*yindex,0)

def main():
    print('lol')

if __name__ == '__main__':
    main()



def islandsdem():
    print('islandsdem')
