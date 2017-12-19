#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 ORM

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from util import p

Base = declarative_base()


class User(Base):
    __tablename__ = 'puser'

    id = Column(String(20), primary_key=True)
    name = Column(String(20), nullable=False)


class Book(Base):

    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20),ForeignKey('user.id'))


engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(id='4', name='Tomy')
session.add(new_user)
session.commit()
session.close()

sess = DBSession()
user = sess.query(User).filter(User.id=='2').one()
p('type:', type(user))
p('id=%s name=%s' % (user.id, user.name))
sess.close()

