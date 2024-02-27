import bpy

from bpy.types import Menu

class VIEW3D_MT_PIE_template(Menu):

    bl_label = "Select Mode"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator_enum("mesh.select_mode", "type")

def register():
    bpy.utils.register_class(VIEW3D_MT_PIE_template)

def unregister():
    bpy.utils.unregister_class(VIEW3D_MT_PIE_template)

if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="VIEW3D_MT_PIE_template")