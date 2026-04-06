from controllers.controller import Controller
from models.user import User
from exceptions import NotFoundException

class UsersController(Controller):

   def sing_up(self, request, response):


      if request.method == 'POST':
         print(request.POST)
         return

         
      response.text = self.view.render_html('users/sing_up.html', 
      {'title': 'MVC Framework - регистрация'})

   