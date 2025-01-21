from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from uuid import UUID

from app.api.crud_post.router import router
from app.db.postgres import get_db
from app.model.post import Post
from app.schema.post.post import PostRead, PostCreate
from sqlalchemy import select

@router.post("/create", response_model=PostRead)
async def create_post(post_data: PostCreate, session: AsyncSession = Depends(get_db)):
    new_post = Post(
        title=post_data.title,
        description=post_data.description
    )
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    return new_post

@router.get("/all", response_model=list[PostRead])
async def get_all_posts(session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(Post))
    posts = result.scalars().all()
    return posts

@router.get("/{post_id}", response_model=PostRead)
async def get_post(post_id: UUID, session: AsyncSession = Depends(get_db)):
    post = await session.scalar(select(Post).where(Post.id == post_id))
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=PostRead)
async def update_post(post_id: UUID, post_data: PostCreate, session: AsyncSession = Depends(get_db)):
    db_post = await session.scalar(select(Post).where(Post.id == post_id))
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    db_post.title = post_data.title
    db_post.description = post_data.description
    await session.commit()
    await session.refresh(db_post)
    return db_post


@router.delete("/{post_id}", response_model=PostRead)
async def delete_post(post_id: UUID, session: AsyncSession = Depends(get_db)):
    post = await session.scalar(select(Post).where(Post.id == post_id))
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    await session.delete(post)
    await session.commit()
    return post
