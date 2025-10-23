--
-- PostgreSQL database dump
--

\restrict E722DM58GSCfoPDX1k8yCNrQiay6wCeCQBOHhi3ANPywhW9yqRloHF3PEf1Fl89

-- Dumped from database version 15.14
-- Dumped by pg_dump version 15.14

-- Started on 2025-10-20 21:35:16

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16564)
-- Name: palabras_clave; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.palabras_clave (
    id integer NOT NULL,
    palabra character varying(50) NOT NULL,
    porcentaje_identidad numeric(5,2),
    sinonimos text
);


ALTER TABLE public.palabras_clave OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16563)
-- Name: palabras_clave_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.palabras_clave_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.palabras_clave_id_seq OWNER TO postgres;

--
-- TOC entry 3325 (class 0 OID 0)
-- Dependencies: 214
-- Name: palabras_clave_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.palabras_clave_id_seq OWNED BY public.palabras_clave.id;


--
-- TOC entry 3173 (class 2604 OID 16567)
-- Name: palabras_clave id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.palabras_clave ALTER COLUMN id SET DEFAULT nextval('public.palabras_clave_id_seq'::regclass);


--
-- TOC entry 3319 (class 0 OID 16564)
-- Dependencies: 215
-- Data for Name: palabras_clave; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.palabras_clave (id, palabra, porcentaje_identidad, sinonimos) FROM stdin;
1	fotosíntesis	98.50	producción de energía, clorofila, luz solar
2	célula vegetal	97.00	citoplasma, núcleo, pared celular
3	clorofila	96.20	pigmento verde, fotosistema, energía solar
4	flor	94.70	pétalos, reproducción, planta
5	semilla	93.50	germinación, embrión, fruto
6	raíz	92.80	absorción, anclaje, rizoma
7	tallo	91.60	soporte, xilema, floema
8	hoja	90.90	estoma, cloroplasto, fotosíntesis
9	polinización	89.80	abeja, reproducción, floración
10	germinación	88.60	crecimiento, semilla, humedad
11	planta	87.40	organismo vegetal, flora
12	ecosistema	86.20	hábitat, biodiversidad, bioma
13	botánica	85.00	biología vegetal, taxonomía
14	floración	84.30	estación, primavera, reproducción
15	xilema	83.00	transporte, savia, conducción
\.


--
-- TOC entry 3326 (class 0 OID 0)
-- Dependencies: 214
-- Name: palabras_clave_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.palabras_clave_id_seq', 15, true);


--
-- TOC entry 3175 (class 2606 OID 16571)
-- Name: palabras_clave palabras_clave_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.palabras_clave
    ADD CONSTRAINT palabras_clave_pkey PRIMARY KEY (id);


-- Completed on 2025-10-20 21:35:17

--
-- PostgreSQL database dump complete
--

\unrestrict E722DM58GSCfoPDX1k8yCNrQiay6wCeCQBOHhi3ANPywhW9yqRloHF3PEf1Fl89

