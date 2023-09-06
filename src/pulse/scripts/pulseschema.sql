-- Table creation queries

-- Table1: public.sp500

CREATE TABLE IF NOT EXISTS public.sp500
(
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


-- Table: public.stockprices

CREATE TABLE IF NOT EXISTS public.stockprices
(
    symbol character varying COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    name character varying COLLATE pg_catalog."default",
    price double precision,
    changes_percentage double precision,
    change double precision,
    day_low double precision,
    day_high double precision,
    year_high double precision,
    year_low double precision,
    market_cap bigint,
    price_avg_50 double precision,
    price_avg_200 double precision,
    exchange character varying COLLATE pg_catalog."default",
    volume integer,
    avg_volume integer,
    open_price double precision,
    previous_close double precision,
    eps double precision,
    pe double precision,
    earnings_announcement timestamp without time zone,
    shares_outstanding bigint,
    CONSTRAINT sp500_stock_price_pkey PRIMARY KEY (symbol, "timestamp")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stockprices
    OWNER to postgres;