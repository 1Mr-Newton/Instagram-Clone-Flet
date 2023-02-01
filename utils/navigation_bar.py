from flet import *

from utils.selectable_container import SelectableContainer
from utils.base import BasePage as BP
class CustomNavigationBar(UserControl):
  def __init__(self,switch_screen):
    super().__init__()
    self.switch_screen = switch_screen

    
  def build(self):
    return Column(
      controls=[
        # NavigationBar(
        #         height=77,
        #         selected_index=1,
        #         destinations=[
        #           NavigationDestination(icon=icons.EXPLORE, label="Explore"),
        #           NavigationDestination(icon=icons.COMMUTE, label="Commute"),
        #           NavigationDestination(
        #               icon=icons.BOOKMARK_BORDER,
        #               selected_icon=icons.BOOKMARK,
        #               label="Explore",
        #     ),
        # ]
        #       ),
        
        Column(
            height=79,
            spacing=10,
            controls=[
              Divider(thickness=0.4,height=0.4),
              Container(
                margin=margin.symmetric(horizontal=10),
                # bgcolor='red',
                padding=padding.only(left=12,right=12),
                content=Row(
                  alignment='spaceBetween',
                  width=350,
                  spacing = 0,
                  controls=[
                    Container(
                      on_click=lambda _: self.switch_screen('/home'),
                      content=Image(src='assets/icons/home.png')
                    ),
                    Container(
                      on_click=lambda _: self.switch_screen('/search'),
                      content=Image(src='assets/icons/search.png')
                    ),
                    Container(
                      on_click=lambda _: self.switch_screen('/events'),
                      content=Image(src='assets/icons/create_post.png')
                    ),
                    Container(
                      on_click=lambda _: self.switch_screen('/events'),
                      content=Image(src='assets/icons/heart.png')
                    ),
                    Container(
                      on_click=lambda _: self.switch_screen('/profile'),
                      content=CircleAvatar(
                        background_image_url='https://images.unsplash.com/photo-1591084728795-1149f32d9866?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTZ8fG1hbnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',radius=12,
                      )
                    ),
                  ]
                )
              ),
            
            ]
              ),
               
      ]
      )