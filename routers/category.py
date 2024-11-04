from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update
from backend.db_depends import get_db
from schemas import CreateCategory
from models.category import Category

from slugify import slugify


router = APIRouter(prefix='/category', tags=['Категории'])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_category(db: Annotated[Session, Depends(get_db)]):
    categories = await db.scalars(select(Category).where(Category.is_active == True))
    return categories.all()


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_category(db: Annotated[Session, Depends(get_db)],
                          create_category: CreateCategory):
    await db.execute(insert(Category).values(
        name=create_category.name,
        parent_id=create_category.parent_id,
        slug=slugify(create_category.name)))
    await db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}
    


@router.put('/{category_slug}/update')
async def update_category(category_slug: str, db: Annotated[Session, Depends(get_db)],
                          update_category: CreateCategory):
    category = await db.scalar(select(Category).where(Category.slug == category_slug))
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Category {category_slug} not found')
    await db.execute(update(Category).where(Category.slug == category_slug).values(name=update_category.name,
                                                                             slug=slugify(update_category.name),
                                                                             parent_id=update_category.parent_id))
    await db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Category update is successful'}


@router.delete('/{category_slug}/delete')
async def delete_category(category_slug: str, db: Annotated[Session, Depends(get_db)]):
    category = await db.scalar(select(Category).where(Category.slug == category_slug))
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Category {category_slug} not found')
    await db.execute(update(Category).where(Category.slug == category_slug).values(is_active=False))
    await db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Category delete is successful'}
