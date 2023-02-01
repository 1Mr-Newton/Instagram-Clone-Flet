from flet import *
from utils.selectable_container import SelectableContainer
from utils.base import BasePage as BP
import back

class LoggedOutScreen(UserControl):
  def __init__(self, pg):
    super().__init__()
    self.pg = pg
    
    

  def switch_page(self):
    self.pg.go('/login')
    back.back_ = '/'

  def build(self):
    return Column(
      controls=[
        BP(
          content=Column(
            spacing=0,
            # alignment=MainAxisAlignment.CENTER,
            horizontal_alignment='center',
            controls=[
              Container(
                height=240
              ),
              Image(
                src='assets/images/logo.png',
                width=200,
              ),
              Container(
                height=50
              ),
              CircleAvatar(
                foreground_image_url='https://images.unsplash.com/photo-1548449112-96a38a643324?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
                # ,
                radius=85//2,
              ),
              Container(
                height=10
              ),
              Text("mrnewton",
                color='black',
                font_family='SF Pro Semibold',
                size=17,
                weight='w600',
              ),
              Container(
                height=10
              ),
              
              Container(
                on_click=lambda e: self.switch_page(),
                height=44,
                width=307,
                border_radius=5,
                bgcolor='#3797EF',
                alignment=alignment.center,
                content= Text('Log in',
                color='white',
                font_family='SF Pro SemiBold',
                size=14,
                text_align='center'
                ),
              ),
              Container(
                height=30
              ),
              Container(
                on_click=lambda _: self.pg.go('/login'),
                content=Text('Switch accounts',
                color='#3797EF',
                font_family='SF Pro SemiBold',
                size=14,
                text_align='center'
                ),),
                Container(
                height=160
              ),
                Divider(
                  thickness=0.2
                ),
                Container(
                height=10
              ),
                Row(
                  spacing=0,
                  alignment='center',
                  controls=[
                    Text("Don't have an account?",
                      color='black',
                      font_family='SF Pro SemiBold',
                      size=12,
                      text_align='center',
                      opacity=0.4
                      ),Container(
                          width=6
                        ),
                    Container(
                      on_click = lambda _: self.pg.go('/signup'),
                      content=Text("Sign up.",
                      color='#262626',
                      font_family='SF Pro SemiBold',
                      size=14,
                      text_align='center',
                      ),
                    )
                  ]
                )
              

            ]
          )
        )
      ]
    )