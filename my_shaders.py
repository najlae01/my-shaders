bl_info= {
    "name": "Shader Library",
    "author": "Najlae",
    "version": (1, 0),
    "blender": (3, 2, 1),
    "location": "View3d > ToolShelf",
    "warning": "",
    "wiki_url": "www.fairyaura.com",
    "category": "Add Shader"
}

import bpy

class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Shader Library'

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Select a shader to be added", icon='SHADERFX')

        row = layout.row()
        row.operator("shader.diamond_operator")
        
        

# Create a custom operator for the diamond shader        
class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = "shader.diamond_operator"
    
    def execute(self, context):
        # creating a new shader (material) and calling it Diamond
        material_diamond = bpy.data.materials.new(name= "Diamond")
        
        # enabling use nodes
        material_diamond.use_nodes = True
        
        # removing the Principled Node
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        
        # Create a reference to material output
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        
        # set the location of the node
        material_output.location = (-400, 0)
        
        # Adding glass1 node
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        # seting the location of the node 
        glass1_node.location = (-600, 0)
        # seting the default color 
        glass1_node.inputs[0].default_value = (1, 0, 0, 1)
        # seting the default IOR value 
        glass1_node.inputs[2].default_value = 1.446
        # deselect the node
        glass1_node.select = False

        # Adding glass2 node
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        # seting the location of the node 
        glass2_node.location = (-600, -150)
        # seting the default color 
        glass2_node.inputs[0].default_value = (0, 1, 0, 1)
        # seting the default IOR value 
        glass2_node.inputs[2].default_value = 1.450
        # deselect the node
        glass2_node.select = False
        
        # Adding glass3 node
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        # seting the location of the node 
        glass3_node.location = (-600, -300)
        # seting the default color 
        glass3_node.inputs[0].default_value = (0, 0, 1, 1)
        # seting the default IOR value 
        glass3_node.inputs[2].default_value = 1.450
        # deselect the node
        glass3_node.select = False
        
        # Adding the add shader node and referencing it as add1_node
        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        # seting the location of the node 
        add1_node.location = (-400, -50)
        # setting the label
        add1_node.label = "Add 1"
        # minimize the node
        add1_node.hide = True
        #deselect the node
        add1_node.select = False
        
        # Adding the add shader node and referencing it as add2_node
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        # seting the location of the node 
        add2_node.location = (-100, 0)
        # setting the label
        add1_node.label = "Add 2"
        # minimize the node
        add2_node.hide = True
        # deselect the node
        add2_node.select = False
        
        # Adding glass4 node
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        # seting the location of the node 
        glass4_node.location = (-150, -150)
        # seting the default color 
        glass4_node.inputs[0].default_value = (1, 1, 1, 1)
        # seting the default IOR value 
        glass4_node.inputs[2].default_value = 1.450
        # deselect the node
        glass4_node.select = False
        
        # Adding glass4 node
        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        # seting the location of the node 
        glass4_node.location = (200, 0)
        # deselect the node
        glass4_node.select = False
        
        material_diamond.node_tree.links.new(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0], add1_node.inputs[1])
        
        material_diamond.node_tree.links.new(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass3_node.outputs[0], add2_node.inputs[1])
        
        material_diamond.node_tree.links.new(add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links.new(glass4_node.outputs[0], mix1_node.inputs[2])
        
        material_diamond.node_tree.links.new(mix1_node.outputs[0], material_output.inputs[0])
        
        
        bpy.context.object.active_material = material_diamond
        
        return {'FINISHED'}
        


def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(SHADER_OT_DIAMOND)


def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)


if __name__ == "__main__":
    register()
