-- Table creation queries

-- Table1: public.sp500

CREATE TABLE IF NOT EXISTS public.sp500
(
    id integer,
    symbol character varying COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default",
    sector character varying COLLATE pg_catalog."default",
    "subSector" character varying COLLATE pg_catalog."default",
    "headQuarter" character varying COLLATE pg_catalog."default",
    "dateFirstAdded" character varying COLLATE pg_catalog."default",
    cik character varying COLLATE pg_catalog."default",
    founded character varying COLLATE pg_catalog."default",
    CONSTRAINT sp500_pkey PRIMARY KEY (symbol)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sp500
    OWNER to postgres;


-- Table2: public.nasdaq

CREATE TABLE IF NOT EXISTS public.nasdaq
(
    id integer,
    symbol character varying COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default",
    sector character varying COLLATE pg_catalog."default",
    "subSector" character varying COLLATE pg_catalog."default",
    "headQuarter" character varying COLLATE pg_catalog."default",
    "dateFirstAdded" character varying COLLATE pg_catalog."default",
    cik character varying COLLATE pg_catalog."default",
    founded character varying COLLATE pg_catalog."default",
    CONSTRAINT nasdaq_pkey PRIMARY KEY (symbol)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.nasdaq
    OWNER to postgres;


-- Table3: public.dowjones

CREATE TABLE IF NOT EXISTS public.dowjones
(
    id integer,
    symbol character varying COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default",
    sector character varying COLLATE pg_catalog."default",
    "subSector" character varying COLLATE pg_catalog."default",
    "headQuarter" character varying COLLATE pg_catalog."default",
    "dateFirstAdded" character varying COLLATE pg_catalog."default",
    cik character varying COLLATE pg_catalog."default",
    founded character varying COLLATE pg_catalog."default",
    CONSTRAINT dowjones_pkey PRIMARY KEY (symbol)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.dowjones
    OWNER to postgres;