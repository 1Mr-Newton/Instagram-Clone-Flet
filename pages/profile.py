from flet import *
from utils.navigation_bar import CustomNavigationBar
from utils.selectable_container import SelectableContainer
from utils.base import BasePage as BP
import back
import webbrowser
class ProfileScreen(UserControl):
  def __init__(self, pg):
    super().__init__()
    self.pg = pg

  def switch_screen(self,route):
    self.page.go(route)  
    back.back_ = '/events'
  def open_youtube(self,e):
    webbrowser.open('https://youtube.com/@1mrnewton')
  def build(self):
    return Column(
      controls=[
        BP(
          content=Column(
            alignment='spaceBetween',
            controls=[
              
              Container(
                content=Column(
                  controls=[

                    Container(
                      padding=padding.only(top=30,left=10,  right=20),
                      content=Row(
                        alignment='spaceBetween',
                        controls=[
                          Container(
                            padding=padding.only(left=130),
                            content=Text('mrnewton',color='#262626', size=14,font_family='SF Pro Semibold'),),
                          Container(
                            content=Image(src='assets/icons/menu.png')
                          )
                        ]
                      ),
                    ),

                    Container(
                      padding=padding.only(left=10,right=10,top=5,bottom=5),
                      width=370,
                      content=Row(
                        alignment='spaceBetween',
                        controls=[
                          Container(
                            height=96,
                            width=96,
                            border_radius=96//2,
                            border=border.all(color='#c7c7cc',width=2,),
                            padding=3,
                            content=CircleAvatar(
                              background_image_url='https://images.unsplash.com/photo-1615109398623-88346a601842?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80'
                            )
                          ),
                          Column(
                            spacing=0,
                            horizontal_alignment='center',
                            controls=[
                              Text('54',color='#262626',font_family='SF Pro Semibold',size=16),
                              Text('Post',color='#262626',font_family='SF Pro Regular',size=13),
                            ]
                          ),
                          Column(
                            spacing=0,
                            horizontal_alignment='center',
                            controls=[
                              Text('2.7M',color='#262626',font_family='SF Pro Semibold',size=16),
                              Text('Followers',color='#262626',font_family='SF Pro Regular',size=13),
                            ]
                          ),
                          Column(
                            spacing=0,
                            horizontal_alignment='center',
                            controls=[
                              Text('207',color='#262626',font_family='SF Pro Semibold',size=16),
                              Text('Following',color='#262626',font_family='SF Pro Regular',size=13),
                            ]
                          ),



                        ]

                      ),
                    ),
                  
                    Container(
                      padding=padding.only(left=10,right=10,top=5,bottom=5),
                      content=Column(
                        spacing=0,
                        controls=[
                          Text('Mr Newton',color='#262626',font_family='SF Pro Semibold',size=12),
                          Text('Please subscribe to my youtube channel',color='#262626',font_family='SF Pro Regular',size=12),
                          Container(
                            on_click= lambda e: self.open_youtube(e),
                            content=Text('https://youtube.com/@1mrnewton',color='#05386B',font_family='SF Pro Medium',size=12),
                            )

                        ]
                      )
                    ),
                  
                    Container(
                        content=Row(
                          alignment='center',
                          controls=[
                            Container(
                              alignment=alignment.center,
                              width=343,
                              height=29,
                              border_radius=6,
                              bgcolor='#ffffff',
                              border=border.all(color='#44262626',width=1),
                              content=Text('Edit Profile',font_family='SF Pro Semibold',size=14,color='#262626')
                            ),
                          ]
                        )
                    ),

                    Container(
                      padding=padding.only(left=10,right=10,top=5,bottom=5,),
                      content=Row(
                        scroll='auto',
                        controls=[
                          Column(
                            horizontal_alignment='center',
                            controls=[
                              Container(
                                height=64,
                                width=64,
                                border_radius=64//2,
                                border=border.all(color='#C7C7CC',width=1,),
                                content=Image(src='assets/icons/new_story.png')
                              ),
                              Text(
                                'New',font_family='SF Pro Regular',size=12,color='#262626'
                                ),
                              ]
                          ),
                          
                          Column(
                            horizontal_alignment='center',
                            controls=[
                              Container(
                                padding=2,
                                height=64,
                                width=64,
                                border_radius=64//2,
                                border=border.all(color='#C7C7CC',width=1,),
                                content=CircleAvatar(background_image_url='https://images.unsplash.com/photo-1615109398623-88346a601842?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80')
                              ),
                              Text(
                                'Friends',font_family='SF Pro Regular',size=12,color='#262626'
                                ),
                              ]
                          ),
                          
                        ]
                      ),
                    ),

                    Divider(thickness=0.4, height=0.4),

                    Container(
                      content=Column(
                        scroll='auto',
                        height=330,
                        controls=[
                          Tabs(
                            
                            selected_index=1,
                            animation_duration=300,
                            tabs=[
                              Tab(
                                tab_content=Container(
                                  alignment=alignment.center,
                                  height=30,
                                  width=155,
                                  content=Image(src='assets/icons/postgrid.png'),
                                  ),
                                content=Container(
                                  content=GridView(
                                      expand=1,
                                      runs_count=5,
                                      max_extent=150,
                                      child_aspect_ratio=1.0,
                                      spacing=2,
                                      run_spacing=2,
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
                                  ),
                                ),
                              ),
                              Tab(
                                tab_content=Container(
                                  alignment=alignment.center,
                                  height=30,
                                  width=155,
                                  content=Image(src='assets/icons/tagged_posts.png'),
                                  ),
                                content=Container(
                                  GridView(
                                      expand=1,
                                      runs_count=5,
                                      max_extent=150,
                                      child_aspect_ratio=1.0,
                                      spacing=2,
                                      run_spacing=2,
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
                                  ),
                                ),
                              ),
                            ],
                          ),
              
                        ]
                      )
                    )



                  ]
                ),


              ),


               CustomNavigationBar(self.switch_screen)
              ]),
      ),]
    )