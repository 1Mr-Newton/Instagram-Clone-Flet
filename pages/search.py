from flet import *
from utils.selectable_container import SelectableContainer
from utils.base import BasePage as BP
from utils.navigation_bar import CustomNavigationBar
import back
class SearchScreen(UserControl):
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
            controls=[
              Container(
                padding=padding.only(top=35,left=10,right=10,bottom=5),
                width=375,
                content=Row(
                  controls=[
                    Container(
                      width=327,
                      height=36,
                      border_radius=10,
                      bgcolor='#1A767680',
                      padding=padding.only(left=10,right=10),
                      content=Row(
                        controls=[
                          Image(src='assets/icons/search_icon.png'),
                          TextField(
                              border=InputBorder.NONE,
                              color='#262626',
                              height=40,
                              width=300,
                              hint_text='Search',
                              hint_style=TextStyle(
                                color='#99000000',
                                font_family='SF Pro Medium',
                                size=15
                                  ),),
                        ]
                      ),
                    ),
                    Container(content=Image(src='assets/icons/live.png'),),
                  ]
                ),
            ),
              
              Container(
                padding=padding.only(left=10,right=10),
                content=Row(
                  spacing=0,
                  scroll='auto',
                  controls=[
                    Container(
                      margin=margin.only(left=7),
                      alignment=alignment.center,
                      border_radius=6,
                      width=75,
                      height=32,
                      border=border.all(color='#333C3C43',width=1),
                      content=Text('IGTV',color='#262626',size=14,font_family='SF Pro Semibold'),
                    ),

                  ]
                )
              ),


              Container(
                height=600,
                content=GridView(
                  expand=1,
                  runs_count=5,
                  max_extent=150,
                  child_aspect_ratio=1.0,
                  spacing=5,
                  run_spacing=5,
                  controls=[
                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),



                    Image(
                      src=f"https://picsum.photos/150/150?1",
                      fit=ImageFit.NONE,
                      repeat=ImageRepeat.NO_REPEAT,
                      # border_radius=border_radius.all(10),
                  ),


                  
                  ]
              )

              ),
              CustomNavigationBar(self.switch_screen) 
            ]
          ),
          ),
      ]
    )