### Two Models

- User
- Post

### User Model Relationship

`posts: Mapped[list[Post]] = relationship(back_populates="author")`

When `user.posts` is called it will return the list of Posts that user belongs


`relationship()` : It tells SQLAlchemy: "When I ask for related stuff, go fetch it for me automatically."

`back_populates` is just telling SQLAlchemy: "These two things are the same connection, seen from opposite ends and keep them synced."

### Post Model Relationship

`author: Mapped[User] = relationship(back_populates="posts")`

When `posts.author` is called it will return the user of the post.



### How the Two Models Work Together

```

┌──────────────┐                ┌──────────────┐
│    users     │                │    posts     │
├──────────────┤   1      many  ├──────────────┤
│ id (PK)      │◄───────────────│ user_id (FK) │
│ username     │                │ id (PK)      │
│ email        │                │ title        │
│ image_file   │                │ content      │
└──────────────┘                │ date_posted  │
                                └──────────────┘

```