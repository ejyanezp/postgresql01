CREATE TABLE IF NOT EXISTS public.employee
(
    id uuid NOT NULL,
    name character varying(40) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(40) COLLATE pg_catalog."default" NOT NULL,
    email character varying(40) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT employee_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.employee
    OWNER to postgres;
