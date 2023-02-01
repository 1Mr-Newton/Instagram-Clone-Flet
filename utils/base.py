from flet import *

class BasePage(UserControl):
  def __init__(self, content=None):
    super().__init__()
    self.content = content
  def build(self):
    return Column(
      controls=[
        Container(
          height=812,
          width=375,
          bgcolor='#F2F2F2',
          content=self.content
        )
      ]
    )