from controllers.controller import Controller
from models.article import Article


class ArticlesController(Controller):
    def index (self, request, response):
      articles = Article.find_all(Article)
      print(articles)
      response.text = self.view.render_html('articles/index.html', 
      {
        'title': 'MVC Framework - articles',
        'h1' : 'articles on site'
      })


    def view(self, request, response, id):
      article = Article.get_by_id(id, Article)
      response.text = self.view.render_html('articles/view.html', 
      {
        'title': f'MVC Framework - {article.name}',
        'h1' : f'Статья: {article.name}', 
        'article' : article
      })
