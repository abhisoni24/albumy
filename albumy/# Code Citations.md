# Code Citations

## License: MIT
https://github.com/greyli/albumy/tree/dfb591fd50bcd54431dacde54dad5579287556b6/albumy/blueprints/main.py

```
= request.args.get('page', 1, type=int)
    per_page = current_app.config['ALBUMY_COMMENT_PER_PAGE']
    pagination = Comment.query.with_parent(photo).order_by(Comment.timestamp.asc()).paginate(page, per_page)
```


## License: MIT
https://github.com/Chryron/albumy/tree/6b643d3a659b04957b51586122755c56acf5cf7f/albumy/blueprints/main.py

```
Comment.query.with_parent(photo).order_by(Comment.timestamp.asc()).paginate(page, per_page)
    comments = pagination.items

    comment_form = CommentForm()
    description_form = DescriptionForm()
    tag_form = TagForm()

    description_form.description.data = photo.description
```

