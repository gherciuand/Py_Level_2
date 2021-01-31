INSERT INTO public.tasks(
	 title, done, date_created, date_scheduled, date_modified)
	VALUES
	( 'task 2', false, current_date, '2021-02-01', null),
	( 'task 3', true, '2021-01-01', '2021-01-15', null),
	( 'task 4', false, current_date, '2021-02-01', null),
	( 'task 5', true, '2021-01-25', '2021-01-27', null),
	( 'task 6', false, current_date, '2021-08-31', null),
	( 'task 7', true, current_date, '2021-02-01', null);
#4#
SELECT *
	FROM public.tascks
	where done=true and date_scheduled='2021-02-26';
#5#
SELECT *
	FROM public.tascks
	where done=false and date_scheduled>current_date;
#6#
SELECT *
	FROM public.tascks
	where done=true and date_scheduled<current_date;
#7#
SELECT *
	FROM public.tascks
	where done=false and date_scheduled = current_date;
#8#
DELETE FROM public.tascks
	WHERE done=true and date_created < current_date-7;
#9#
UPDATE public.tascks
	SET done=true
	WHERE done=false and date_scheduled < current_date;
#10#
SELECT count(title)
	FROM public.tascks
	where done=true;