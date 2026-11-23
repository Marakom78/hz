    def add(self, request, response):
        # if self.user is None:
        #     raise UnauthorizedException('Необходимо авторизоваться')
        user = User.get_by_id(1)
        try:
            input_stream = request.environ.get('wsgi.input')
            content_length = int(request.environ.get('CONTENT_LENGTH', 0))
            body = input_stream.read(content_length) if content_length else b""
            data = json.loads(body.decode('utf-8'))
            fields = data['articles'][0] 

            article =Article.create(fields, None, user)
            if isinstance( article, Article):
                response.text = self.view.display_json({
                    'result' : 'OK',
                    'articles' : [article.to_dict()] });
            else:
                response.text = self.view.display_json({
                    'result' : 'Error'
                    });
        except InvalidArgumentException as e:
            response.text = self.view.render_html('articles/add.html', {'title' : 'Добавление статьи', 'article_data' : fields, 'error' : e})