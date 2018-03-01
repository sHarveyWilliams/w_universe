--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.11
-- Dumped by pg_dump version 9.5.11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: wu_database; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE wu_database WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'ru_RU.UTF-8' LC_CTYPE = 'ru_RU.UTF-8';


ALTER DATABASE wu_database OWNER TO postgres;

\connect wu_database

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: criteria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE criteria (
    id integer NOT NULL,
    supplier integer NOT NULL,
    cost double precision,
    quality double precision,
    coincidence double precision,
    reliability double precision,
    delivery double precision,
    delivery_rapidity double precision
);


ALTER TABLE criteria OWNER TO postgres;

--
-- Name: criteria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE criteria_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE criteria_id_seq OWNER TO postgres;

--
-- Name: criteria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE criteria_id_seq OWNED BY criteria.id;


--
-- Name: needablegood; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE needablegood (
    id_n integer NOT NULL,
    production integer NOT NULL
);


ALTER TABLE needablegood OWNER TO postgres;

--
-- Name: needablegood_id_n_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE needablegood_id_n_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE needablegood_id_n_seq OWNER TO postgres;

--
-- Name: needablegood_id_n_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE needablegood_id_n_seq OWNED BY needablegood.id_n;


--
-- Name: production; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE production (
    id_a integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE production OWNER TO postgres;

--
-- Name: production_id_a_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE production_id_a_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE production_id_a_seq OWNER TO postgres;

--
-- Name: production_id_a_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE production_id_a_seq OWNED BY production.id_a;


--
-- Name: rangeofgood; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE rangeofgood (
    id integer NOT NULL,
    supplier integer NOT NULL,
    production integer NOT NULL,
    cost double precision,
    "time" time without time zone
);


ALTER TABLE rangeofgood OWNER TO postgres;

--
-- Name: rangeofgood_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE rangeofgood_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE rangeofgood_id_seq OWNER TO postgres;

--
-- Name: rangeofgood_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE rangeofgood_id_seq OWNED BY rangeofgood.id;


--
-- Name: reliability; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE reliability (
    id integer NOT NULL,
    supplier integer NOT NULL,
    completed_ord integer,
    all_orders integer,
    cust_rate double precision
);


ALTER TABLE reliability OWNER TO postgres;

--
-- Name: reliability_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE reliability_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE reliability_id_seq OWNER TO postgres;

--
-- Name: reliability_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE reliability_id_seq OWNED BY reliability.id;


--
-- Name: supplier; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE supplier (
    id_p integer NOT NULL,
    name text NOT NULL,
    phone text NOT NULL,
    email text NOT NULL,
    addres text NOT NULL
);


ALTER TABLE supplier OWNER TO postgres;

--
-- Name: supplier_id_p_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE supplier_id_p_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE supplier_id_p_seq OWNER TO postgres;

--
-- Name: supplier_id_p_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE supplier_id_p_seq OWNED BY supplier.id_p;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY criteria ALTER COLUMN id SET DEFAULT nextval('criteria_id_seq'::regclass);


--
-- Name: id_n; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY needablegood ALTER COLUMN id_n SET DEFAULT nextval('needablegood_id_n_seq'::regclass);


--
-- Name: id_a; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY production ALTER COLUMN id_a SET DEFAULT nextval('production_id_a_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY rangeofgood ALTER COLUMN id SET DEFAULT nextval('rangeofgood_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reliability ALTER COLUMN id SET DEFAULT nextval('reliability_id_seq'::regclass);


--
-- Name: id_p; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY supplier ALTER COLUMN id_p SET DEFAULT nextval('supplier_id_p_seq'::regclass);


--
-- Data for Name: criteria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY criteria (id, supplier, cost, quality, coincidence, reliability, delivery, delivery_rapidity) FROM stdin;
\.


--
-- Name: criteria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('criteria_id_seq', 1, false);


--
-- Data for Name: needablegood; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY needablegood (id_n, production) FROM stdin;
\.


--
-- Name: needablegood_id_n_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('needablegood_id_n_seq', 1, false);


--
-- Data for Name: production; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY production (id_a, name) FROM stdin;
\.


--
-- Name: production_id_a_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('production_id_a_seq', 1, false);


--
-- Data for Name: rangeofgood; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY rangeofgood (id, supplier, production, cost, "time") FROM stdin;
\.


--
-- Name: rangeofgood_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('rangeofgood_id_seq', 1, false);


--
-- Data for Name: reliability; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY reliability (id, supplier, completed_ord, all_orders, cust_rate) FROM stdin;
\.


--
-- Name: reliability_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('reliability_id_seq', 1, false);


--
-- Data for Name: supplier; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY supplier (id_p, name, phone, email, addres) FROM stdin;
0	Мираторг	89211241242	brom@gmail.com	ul Krasnaya
1	ПензКолбасы	89211241241	penzcolb@gmail.com	ul Presnenskaya
\.


--
-- Name: supplier_id_p_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('supplier_id_p_seq', 1, false);


--
-- Name: pk_criteria; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY criteria
    ADD CONSTRAINT pk_criteria PRIMARY KEY (id);


--
-- Name: pk_needablegood; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY needablegood
    ADD CONSTRAINT pk_needablegood PRIMARY KEY (id_n);


--
-- Name: pk_production; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY production
    ADD CONSTRAINT pk_production PRIMARY KEY (id_a);


--
-- Name: pk_rangeofgood; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY rangeofgood
    ADD CONSTRAINT pk_rangeofgood PRIMARY KEY (id);


--
-- Name: pk_reliability; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reliability
    ADD CONSTRAINT pk_reliability PRIMARY KEY (id);


--
-- Name: pk_supplier; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY supplier
    ADD CONSTRAINT pk_supplier PRIMARY KEY (id_p);


--
-- Name: idx_criteria__supplier; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_criteria__supplier ON criteria USING btree (supplier);


--
-- Name: idx_needablegood__production; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_needablegood__production ON needablegood USING btree (production);


--
-- Name: idx_rangeofgood__production; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_rangeofgood__production ON rangeofgood USING btree (production);


--
-- Name: idx_rangeofgood__supplier; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_rangeofgood__supplier ON rangeofgood USING btree (supplier);


--
-- Name: idx_reliability__supplier; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_reliability__supplier ON reliability USING btree (supplier);


--
-- Name: fk_criteria__supplier; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY criteria
    ADD CONSTRAINT fk_criteria__supplier FOREIGN KEY (supplier) REFERENCES supplier(id_p);


--
-- Name: fk_needablegood__production; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY needablegood
    ADD CONSTRAINT fk_needablegood__production FOREIGN KEY (production) REFERENCES production(id_a);


--
-- Name: fk_rangeofgood__production; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY rangeofgood
    ADD CONSTRAINT fk_rangeofgood__production FOREIGN KEY (production) REFERENCES production(id_a);


--
-- Name: fk_rangeofgood__supplier; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY rangeofgood
    ADD CONSTRAINT fk_rangeofgood__supplier FOREIGN KEY (supplier) REFERENCES supplier(id_p);


--
-- Name: fk_reliability__supplier; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reliability
    ADD CONSTRAINT fk_reliability__supplier FOREIGN KEY (supplier) REFERENCES supplier(id_p);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

