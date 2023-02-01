from flet import UserControl,Container,alignment,Column, border
class SelectableContainer(UserControl):
  """A container that has a select ability"""
  def __init__(
    self,
    height=0,
    width=0, 
    bgcolor=None,
    size=25,stroke_width=2,
    border=None,
    animation=None,
    checked=False, 
    font_size=17, pressed=None,
    border_radius=0,
    on_select_bgcolor=None,
    on_select_text_color=None,
    on_select_border=None,
    on_select_border_radius = None,
    text_color=None,
    content=None,
    alignment=None,
    on_select_content=None,
    on_select_alignment=None,
    on_select_animation=None,
    on_select_width=None,
    on_select_height=None,
    on_selection=object
    ):
    super().__init__()
    self.height = height
    self.width = width
    self.alignment = alignment
    self.border_radius=border_radius
    self.bgcolor = bgcolor
    self.size = size
    self.border = border
    self.stroke_width = stroke_width
    self.animation=animation
    self.checked=checked
    self.font_size=font_size
    self.pressed  = pressed
    self.content = content
    self.on_selection = on_selection

    self.on_select_border = on_select_border
    self.on_select_bgcolor=on_select_bgcolor
    self.on_select_content = on_select_content
    if self.on_select_content == None:
      self.on_select_content = self.content
    # else:
    #   self.on_select_content = on_select_content  
    self.on_select_alignment = on_select_alignment
    self.on_select_text_color = on_select_text_color
    self.on_select_border_radius=on_select_border_radius
    self.on_select_animation = on_select_animation
    self.on_select_width = on_select_width
    self.on_select_height = on_select_height

    if self.on_select_width==None:
      self.on_select_width=self.width

    if self.on_select_height==None:
      self.on_select_height=self.height
    

    if self.on_select_border_radius==None:
      self.on_select_border_radius=self.border_radius
    

    if self.on_select_alignment==None:
      self.on_select_alignment=self.alignment
    
  def _checked(self):
      self.check_box = Container(
        animate=self.on_select_animation,
        width=self.on_select_width,
        height=self.on_select_height,
        border_radius=self.on_select_border_radius,
        bgcolor=self.on_select_bgcolor,
        border=self.on_select_border,
        content=self.on_select_content
        ),
      return self.check_box
  
  def _unchecked(self):
    self.check_box = Container(
      alignment=self.alignment,
      animate=self.animation,
      width=self.width,
      height=self.height,
      border_radius=self.border_radius,
      bgcolor=self.bgcolor,
      border = self.border,
      content=self.content,
      )
    return self.check_box

  def build(self):
    print(self.checked)
    if self.checked == True:  
      return Column(controls=[
        Container(
          on_click = lambda e: self.checked_check(e),
          content=self._checked(),
          )
      ])
      
    else:  
      return Column(
        controls=[
          Container(on_click = lambda e: self.checked_check(e),
            content=self._unchecked(),
          )
      ]
      )

  def checked_check(self,e):
    print(self.checked)
    if self.checked == False:
        self.checked = True


        self.check_box.border = self.on_select_border
        self.check_box.bgcolor = self.on_select_bgcolor
        self.check_box.content = self.on_select_content
        self.check_box.alignment=self.on_select_alignment
        self.check_box.animate=self.on_select_animation
        self.check_box.width=self.on_select_width
        self.check_box.height=self.on_select_height
        self.check_box.border_radius=self.on_select_border_radius
        self.update()
        self.on_selection()

        
    elif self.checked == True:
        self.checked = False
        self.check_box.border = self.border
        self.check_box.bgcolor = self.bgcolor
        self.check_box.content = self.content
        self.check_box.alignment=self.alignment
        self.check_box.animate=self.animation
        self.check_box.width=self.width
        self.check_box.height=self.height
        self.check_box.border_radius=self.border_radius        

        
        
        
        self.update()

        
        
  def is_checked(self):
      return self.checked


