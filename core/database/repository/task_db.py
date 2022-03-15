#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.database.db_connect import Connection
from pypika import Query, Table

tasks = Table("tasks")


class TaskRepository(Connection):
    def insTask(self, args=None):
        q = "INSERT IGNORE INTO tasks (tskUsrTg_Id, taskscol) VALUES (%s,%s)"
        return self._insert(q, args)
    def listTask(self, args=None):
        q = "SELECT * FROM tasks WHERE tskUsrTg_Id = %s"
        #query = Query.from_(tasks).select("*").where(tasks.tskUsrTg_Id == "%s")
        #q = query.get_sql(quote_char=None)
        return self._selectAll(q, args)