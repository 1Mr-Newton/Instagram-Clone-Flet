from flet import *
import back
from utils.selectable_container import SelectableContainer
from utils.navigation_bar import CustomNavigationBar
from utils.base import BasePage as BP
class HomeScreen(UserControl):
  def __init__(self, pg):
    super().__init__()
    self.pg = pg

  def change_page(self):
    self.page.go('')  
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
                padding=padding.only(top=45,left=10,right=12,bottom=2),
                content=Row(
                    alignment='spaceBetween',
                    controls=[
                    Container(
                      Image(src='assets/icons/camera.png')
                    ),
                    Container(
                      Image(src='assets/icons/logo2.png')
                    ),
                    Row(
                      controls=[
                      Container(
                        Image(src='assets/icons/igtv.png')
                      ),
                      Container(width=0),
                      Container(
                        Image(src='assets/icons/msn.png')
                      ),
                      ]
                    ),
                    
                  ]
                )
              ),
              Divider(height=0.2,thickness=0.4),
              Container(
                padding=padding.only(left=12),
                content=Row(
                  scroll='auto',
                  controls=[
                    Container(
                      margin=margin.only(right=5),
                      content=Column(
                      spacing=0,
                      controls=[
                        Container(
                          padding = 2.3,
                          height=62,
                          width=62,
                          border_radius=62/2,
                          gradient=LinearGradient(
                            colors=['red','yellow','purple','red','purple','yellow'],rotation=2
                          ),
                          content=Container(
                            height=58,
                            width=58,
                            bgcolor='white',
                            border_radius=56/2,
                            padding=2,
                            content=CircleAvatar(
                              background_image_url='https://images.unsplash.com/photo-1564564321837-a57b7070ac4f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80'
                            )

                          )
                        ),
                        Text('Your Story',color='#262626',font_family='SF Pro Medium',size=12,),
                      ]
                    ),                  
                    ),
                  
                  ]
                ),
              ),
              Divider(height=0.2,thickness=0.4),
              Column(
                scroll='auto',
                controls=[
                    Container(
                      padding=padding.only(right=14),
                      content=Row(
                        alignment='spaceBetween',
                        controls=[
                          Container(
                            alignment=alignment.center,
                            height=35,
                            clip_behavior= ClipBehavior.ANTI_ALIAS,
                            padding = padding.only(left=10,right=10),
                            content=Row(
                              vertical_alignment=CrossAxisAlignment.CENTER,
                              controls=[
                            CircleAvatar(background_image_url='https://images.unsplash.com/photo-1615109398623-88346a601842?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',radius=15),
                            Column(
                              alignment='center',
                            # height=44,
                              spacing=0,
                              controls=[
                              Row(
                                controls=[
                                  Text('mrnewton',color='#262626',font_family='SF Pro Semibold',size=13),
                                  Image('assets/icons/verified.png')
                                ]
                              ),
                        Text('Accra, Ghana',color='#262626',font_family='SF Pro Regular',size=12)
                            ]
                          )
                        ]
                      )
                    ),
                    Container(
                      content=Image(src='assets/icons/more.png')
                    )
                  ]
                )
              ),
            
              Container(
                height=375,
                width=375,
                content=Stack(
                  controls=[
                    Row(
                      height=375,
                      width=375,
                      scroll='auto',
                      controls=[
                        Container(
                          height=375,
                          width=375,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          content=Image(src='assets/posts/placeholder_image.png',fit=ImageFit.COVER),

                          ),
                        Container(
                          height=375,
                          width=375,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          content=Image(src='assets/posts/placeholder_image.png',fit=ImageFit.COVER),

                          ),
                        Container(
                          height=375,
                          width=375,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          content=Image(src='assets/posts/placeholder_image.png',fit=ImageFit.COVER),

                          ),
                    ]
                  ),
                  Container(
                    alignment=alignment.center,
                    right=15,
                    top = 12,
                    height=26,
                    width=34,
                    border_radius=13,
                    bgcolor='#B3121212',
                    content=Text(
                      '1/3',
                      font_family='SF Pro Regular',
                      size=12,
                      color='#f9f9f9'
                    )
                  ),
                  ]
                )
              ),
            
              # Container(height=1),
              Container(
                padding=padding.only(left=10,right=10,),
                width=375,
                content=Row(
                  width = 375,
                  alignment='spaceBetween',
                  controls=[
                    Row(
                      controls=[
                        Container(
                          content=Image(src='assets/icons/like.png')
                        ),
                        Container(
                          content=Image(src='assets/icons/comment.png')
                        ),
                        Container(
                          content=Image(src='assets/icons/share.png')
                        ),
                      ]
                    ),
                    Container(
                      content=Row(
                        
                        spacing=3,
                        controls=[
                          Image(src='assets/icons/selected_dot.png'),
                          Image(src='assets/icons/unselected_dot.png'),
                          Image(src='assets/icons/unselected_dot.png'),
                        ]
                      )
                    ),
                    
                    Container(
                      width=20
                    ),
                    Container(
                      content=Image(src='assets/icons/save.png'),
                    ),
                  ]
                )
              ),

              Container(
                padding=padding.only(left=10,right=10),
                width=375,
                content=Row(
                  spacing=0,
                  controls=[
                    CircleAvatar(
                      background_image_url='https://images.unsplash.com/photo-1615109398623-88346a601842?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',radius=8
                    ),
                    Container(width=8),
                    Text('Liked by ',color='#262626', font_family='SF Pro Regular',size=13),
                    Text('craig_love',color='#262626', font_family='SF Pro Semibold',size=13),
                    Text(' and ',color='#262626', font_family='SF Pro Regular',size=13),
                    Text('44,686 others',color='#262626', font_family='SF Pro Semibold',size=13),
                  ]
                ),
              ),
              
              
              Column(
                spacing=0,
                controls=[
                  Container(
                    width=375,
                    padding=padding.only(left=10,right=50),
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    content=Row(
                      alignment='center',
                      vertical_alignment='start',
                      spacing=0,
                      controls=[
                        Container(
                          Text('mrnewton', color='#262626', font_family='SF Pro Semibold', size=13),
                        ),
                        Container(width=5),
                        Container(

                          width=310,
                          clip_behavior=ClipBehavior.ANTI_ALIAS,
                          padding=padding.only(right=6),
                          content = Text('The game in Japan was amazing and I want to ', color='#262626', font_family='SF Pro Regular', size=13),)
                      ]
                    ),
                  ),
                  Container(
                    width=375,
                    padding=padding.only(left=10,right=50),
                    clip_behavior=ClipBehavior.ANTI_ALIAS,
                    content = Text('share some photos', color='#262626', font_family='SF Pro Regular', size=13),
                  ),
                ]
              ),


                ]
              ),
              

             
             CustomNavigationBar(self.switch_screen)
              
             ]
          ),
          ),
      ]
    )