from flet import *
from utils.navigation_bar import CustomNavigationBar
from utils.selectable_container import SelectableContainer
from utils.base import BasePage as BP
import back
class EventsScreen(UserControl):
  def __init__(self, pg):
    super().__init__()
    self.pg = pg

  def switch_screen(self,route):
    self.page.go(route)  
    back.back_ = '/events'
    
  def build(self):
    return Column(
      controls=[
        BP(
          content=Column(
            alignment='spaceBetween',
            controls=[
              Container(
                alignment=alignment.center,
                height=600,
                clip_behavior=ClipBehavior.ANTI_ALIAS,
                content=Tabs(
                  
                height=500,
                selected_index=1,
                animation_duration=300,
                tabs=[
                  Tab(
                    tab_content=Container(
                      alignment=alignment.center,
                      height=30,
                      width=155,
                      content=Text(
                        'Following',
                        color='black',
                        font_family='SF Pro Semibold',
                        size=16,
                      ),
                      ),
                    content=Container(
                      padding=padding.only(left=12,right=12,top=20,),
                      content=Column(
                      controls=[
                        Row(
                          controls=[
                            Text(
                              'Follow Requests',
                              color='black',
                              font_family='SF Pro Semibold',
                              size=16,
                              ),
                          ]
                        ),
                        Divider(height=0.4,thickness=0.4),
                        Row(
                          controls=[
                            Text(
                              'New',
                              color='black',
                              font_family='SF Pro Semibold',
                              size=16,
                              ),
                          ]
                        ),
                      ]
                    ),
                    ),
                ),
                  Tab(
                    tab_content=Container(
                      alignment=alignment.center,
                      height=30,
                      width=155,
                      content=Text(
                        'You',
                        color='black',
                        font_family='SF Pro Semibold',
                        size=16,
                        ),
                      ),
                    icon=icons.SETTINGS,
                        # Divider(height=0.4,thickness=0.4),
                    content=Container(
                      padding=padding.only(left=12,right=12,top=20,),
                      content=Column(
                      controls=[
                        Row(
                          controls=[
                            Text(
                              'Follow Requests',
                              color='black',
                              font_family='SF Pro Semibold',
                              size=16,
                              ),
                          ]
                        ),
                        Divider(height=0.4,thickness=0.4),
                        Row(
                          controls=[
                            Text(
                              'New',
                              color='black',
                              font_family='SF Pro Semibold',
                              size=16,
                              ),
                          ]
                        ),
                      ]
                    ),
                    ),
                ),
                ],
                expand=1,
              ),
              ),
            CustomNavigationBar(self.switch_screen)
              ]),
      ),]
    )