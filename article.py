    @staticmethod
    def create(fields, img_file, author):
        if not fields['title']:
            raise InvalidArgumentException('не передано название статьи')

        if not fields['text']:
            raise InvalidArgumentException('не передан текст статьи')

        if __class__.check_file_size(img_file, MAX_FILE_SIZE)[0] == False :
            raise InvalidArgumentException('Слишком большой файл! Должно быть не более 5МБ')


        article = Article()
        article._title = fields['title']
        article._text = fields['text']
        article._author_id = author.get_id()

        if img_file.filename:
            file_path = 'uploads/' +  img_file.filename
            article._img = file_path
            os.makedirs('/uploads', exist_ok=True)
            with open(file_path, 'wb') as f:
                while True:
                    chunk = img_file.file.read(8192)  # Читаем файл по частям
                    if not chunk:
                        break
                    f.write(chunk)

        article.save()
        return article




    @staticmethod
    def check_file_size(file_item, max_size):
        """
        Проверка размера файла без загрузки всего файла в память.
        Читает файл по частям и суммирует их размер.
        """
        total_size = 0
        chunk_size = 8192  # Читаем по 8KB

        # Сохраняем текущую позицию, чтобы потом вернуться
        current_pos = file_item.file.tell()

        try:
            # Перемещаемся в начало файла
            file_item.file.seek(0)

            # Читаем файл по частям и суммируем размер
            while True:
                chunk = file_item.file.read(chunk_size)
                if not chunk:
                    break
                total_size += len(chunk)

                # Если уже превысили лимит, можно прервать проверку
                if total_size > max_size:
                    break
        finally:
            # Возвращаемся на исходную позицию для последующего чтения
            file_item.file.seek(current_pos)
        print(total_size)
        return total_size <= max_size, total_size