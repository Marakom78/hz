    def map_properties_to_db_format(self):
        properties = self.__dict__
        mappedProperties = {}

        for property, value in properties.items():
            property = property[1:]
            mappedProperties[property] = value

        return mappedProperties

    def update(self, mappedProperties):
        columns2params = []
        columns2values = {}
        index = 1
        for column, value in mappedProperties.items():
            param = f"param{index}"
            param_ext = ':' + param
            print(param)
            columns2params.append(f"{column} = {param_ext}")
            columns2values[param] = value
            index += 1

        sql = f"UPDATE {self.__class__.get_table_name()}  SET  {','.join(columns2params)} WHERE id = {self._id}"

        db = Db()
        db.query(sql, columns2values, self.__class__)
        db.connection.commit()
        db.connection.close()

    def insert(self, mappedProperties):
        filteredProperties = dict(filter(lambda item: item[1] is not None and item[1] != '', mappedProperties.items()))
        columns = []
        paramsNames = []
        params2values = {}
        for  columnName, value in filteredProperties.items():
            columns.append('`' + columnName + '`')
            paramsName = ':'+ columnName
            paramsNames.append(paramsName)
            params2values[columnName] = value

        columnsViaSemicolon = ', '.join(columns)
        paramsNamesViaSemicolon = ', '.join(paramsNames)

        sql = 'INSERT INTO ' + self.__class__.get_table_name() + ' (' + columnsViaSemicolon + ' ) VALUES (' + paramsNamesViaSemicolon + ');'
        db = Db()
        db.query(sql, params2values, self.__class__)
        db.connection.commit()
        db.connection.close()