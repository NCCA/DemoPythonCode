# let's create a sphere
import maya.cmds as cmds

# let's delete all objects
cmds.select(all=True)
cmds.delete()
#let's create a new torus
cmds.torus(r=4, hr=0.5, name='Torus1')
cmds.move(0, 0, 0, 'Torus1')
cmds.scale(0.5, 0.5, 0.5, 'Torus1')
cmds.rotate(0, '45deg', 0, 'Torus1')

