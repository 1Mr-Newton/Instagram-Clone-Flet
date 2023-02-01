from flet import *
from views import views_handler

def main(page: Page):

  def route_change(route):
    page.views.clear()
    page.views.append(
      views_handler(page)[page.route]
    )

  

  page.fonts = {
    "SF Pro Bold":"fonts/SFProText-Bold.ttf",
    "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
    "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
    "SF Pro Light":"fonts/SFProText-Light.ttf",
    "SF Pro Medium":"fonts/SFProText-Medium.ttf",
    "SF Pro Regular":"fonts/SFProText-Regular.ttf",
    "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
    "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
  }
  
  # page.navigation_bar = NavigationBar(
  #       destinations=[
  #           NavigationDestination(icon=icons.EXPLORE, label="Explore"),
  #           NavigationDestination(icon=icons.COMMUTE, label="Commute"),
  #           NavigationDestination(
  #               icon=icons.BOOKMARK_BORDER,
  #               selected_icon=icons.BOOKMARK,
  #               label="Explore",
  #           ),
  #       ]
  #   )


  page.on_route_change = route_change
  page.go('/')
  # page.go('/login')
  # page.go('/profile')
  



app(target=main,  assets_dir="assets")