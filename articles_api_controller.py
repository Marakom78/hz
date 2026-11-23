import json
from controllers.controller import Controller
from models.article import Article
from models.user import User
from exceptions import NotFoundException

class ArticlesApiController(Controller):
    def view(self, request, response, id):

        article = Article.get_by_id(id)
        print(article)
        if article is None:
             raise NotFoundException('Статья не найдена')

        article_dict = article.to_dict()

        response.text = self.view.display_json({'article' : article_dict })


