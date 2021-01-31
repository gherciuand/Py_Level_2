-- Table: public.tasks

-- DROP TABLE public.tasks;

CREATE TABLE public.tasks
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    title character varying(100) COLLATE pg_catalog."default",
    done boolean,
    date_created date,
    date_scheduled date,
    date_modified date,
    CONSTRAINT tasks_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.tasks
    OWNER to postgres;