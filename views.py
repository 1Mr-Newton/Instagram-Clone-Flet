from flet import *
from pages.home import HomeScreen
from pages.login import LoginScreen
from pages.signup import SignupScreen
from pages.logged_out import LoggedOutScreen
from pages.search import SearchScreen
from pages.events import EventsScreen
from pages.profile import ProfileScreen


def views_handler(page):
  return {
    '/':View(
        route='/',
        controls=[
          LoggedOutScreen(page)
        ]
      ),
    '/login':View(
        route='/login',
        controls=[
          LoginScreen(page)
        ]
      ),
    '/signup':View(
        route='/signup',
        controls=[
          SignupScreen(page)
        ]
      ),
    '/home':View(
        route='/home',
        controls=[
          HomeScreen(page)
        ]
      ),
    '/search':View(
        route='/search',
        controls=[
          SearchScreen(page)
        ]
      ),
    '/events':View(
        route='/events',
        controls=[
          EventsScreen(page)
        ]
      ),
    '/profile':View(
        route='/profile',
        controls=[
          ProfileScreen(page)
        ]
      ),
  }