#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core import decorators
from core.utilities.functions import user_reply_object
from core.utilities.functions import user_object
from core.database.repository.user import UserRepository
from core.database.repository.task_db import TaskRepository
from core.utilities.message import message, reply_message



@decorators.owner.init
@decorators.delete.init
def init(update,context):
    user = user_object(update)
    nickname = "@"+ user.username
    lUser = UserRepository().getByUsername(nickname)
    data_Task = [(lUser['tg_id'], context.args[0])]
    TaskRepository().insTask(data_Task)
    message(update,context, "Task correttamente inserito!")

def listTasks(update, context):
    user = user_object(update)
    nickname = "@"+ user.username
    lUser = UserRepository().getByUsername(nickname)
    data_Task = [(lUser['tg_id'])]
    myTasks = TaskRepository().listTask(data_Task)
    print(myTasks)
    reply_message(update,context, myTasks)