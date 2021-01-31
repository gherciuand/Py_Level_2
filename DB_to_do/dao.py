import db


# list of FUNCTION --> business logic of my app

def createTask(title, done=False, date_created="current_date", date_scheduled="current_date + 7", date_modified="null"):
    db.executeSQL(
        f"""
        INSERT INTO public.tasks
        (title, done, date_created,date_scheduled, date_modified)
        VALUES
        ('{title}',{done}, {date_created},'{date_scheduled}',{date_modified});
        """
    )


def removeTask(id):
    db.executeSQL(
        f"""
        DELETE FROM public.tasks
        WHERE id = {id}
        """)


def updateTask(id, title=None, done=None, date_scheduled=None):
    if title != None and title != "":
        db.executeSQL(
            f"""
            UPDATE public.tasks
            SET title='{title}', date_modified=current_date
            WHERE id = {id};
            """
        )

    if done != None:
        db.executeSQL(
            f"""
            UPDATE public.tasks
            SET done={done}, date_modified=current_date
            WHERE id = {id};
            """
        )
    if date_scheduled != None:
        db.executeSQL(
            f"""
            UPDATE public.tasks
            SET date_scheduled='{date_scheduled}', date_modified=current_date
            WHERE id = {id};
            """
        )


def readTasks():
    tasks = db.executeSQL(
        f"""
            SELECT *  FROM public.tasks
	        order by id ASC;
	        """)
    return tasks
