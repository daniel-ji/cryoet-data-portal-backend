--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2 (Debian 14.2-1.pgdg110+1)
-- Dumped by pg_dump version 14.2 (Debian 14.2-1.pgdg110+1)

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

ALTER TABLE IF EXISTS ONLY public.tomograms DROP CONSTRAINT IF EXISTS tomograms_type_fkey;
ALTER TABLE IF EXISTS ONLY public.tomograms DROP CONSTRAINT IF EXISTS tomograms_tomogram_voxel_spacing_id_fkey;
ALTER TABLE IF EXISTS ONLY public.tomogram_voxel_spacings DROP CONSTRAINT IF EXISTS tomogram_voxel_spacing_run_id_fkey;
ALTER TABLE IF EXISTS ONLY public.tomogram_authors DROP CONSTRAINT IF EXISTS tomogram_authors_tomogram_id_fkey;
ALTER TABLE IF EXISTS ONLY public.tiltseries DROP CONSTRAINT IF EXISTS tiltseries_run_id_fkey;
ALTER TABLE IF EXISTS ONLY public.runs DROP CONSTRAINT IF EXISTS runs_dataset_id_fkey;
ALTER TABLE IF EXISTS ONLY public.dataset_funding DROP CONSTRAINT IF EXISTS dataset_funding_dataset_id_fkey;
ALTER TABLE IF EXISTS ONLY public.dataset_authors DROP CONSTRAINT IF EXISTS dataset_authors_dataset_id_fkey;
ALTER TABLE IF EXISTS ONLY public.annotations DROP CONSTRAINT IF EXISTS annotations_tomogram_voxel_spacing_id_fkey;
ALTER TABLE IF EXISTS ONLY public.annotation_files DROP CONSTRAINT IF EXISTS annotation_files_annotation_id_fkey;
ALTER TABLE IF EXISTS ONLY public.annotation_authors DROP CONSTRAINT IF EXISTS annotation_authors_annotation_id_fkey;
DROP INDEX IF EXISTS public.tomograms_tomogram_voxel_spacing_id;
DROP INDEX IF EXISTS public.tomogram_voxel_spacing_run;
DROP INDEX IF EXISTS public.tiltseries_run;
DROP INDEX IF EXISTS public.dataset_funding_dataset;
DROP INDEX IF EXISTS public.dataset_authors_dataset;
DROP INDEX IF EXISTS public.annotations_tomogram_voxel_spacing;
DROP INDEX IF EXISTS public.annotation_files_annotation_id;
ALTER TABLE IF EXISTS ONLY public.tomograms DROP CONSTRAINT IF EXISTS tomograms_pkey;
ALTER TABLE IF EXISTS ONLY public.tomogram_voxel_spacings DROP CONSTRAINT IF EXISTS tomogram_voxel_spacing_pkey;
ALTER TABLE IF EXISTS ONLY public.tomogram_type DROP CONSTRAINT IF EXISTS tomogram_type_pkey;
ALTER TABLE IF EXISTS ONLY public.tomogram_authors DROP CONSTRAINT IF EXISTS tomogram_authors_tomogram_id_name_key;
ALTER TABLE IF EXISTS ONLY public.tomogram_authors DROP CONSTRAINT IF EXISTS tomogram_authors_pkey;
ALTER TABLE IF EXISTS ONLY public.tiltseries DROP CONSTRAINT IF EXISTS tiltseries_pkey;
ALTER TABLE IF EXISTS ONLY public.runs DROP CONSTRAINT IF EXISTS runs_pkey;
ALTER TABLE IF EXISTS ONLY public.runs DROP CONSTRAINT IF EXISTS runs_dataset_id_name_key;
ALTER TABLE IF EXISTS ONLY public.datasets DROP CONSTRAINT IF EXISTS datasets_pkey;
ALTER TABLE IF EXISTS ONLY public.dataset_funding DROP CONSTRAINT IF EXISTS dataset_funding_pkey;
ALTER TABLE IF EXISTS ONLY public.dataset_authors DROP CONSTRAINT IF EXISTS dataset_authors_pkey;
ALTER TABLE IF EXISTS ONLY public.annotations DROP CONSTRAINT IF EXISTS annotations_pkey;
ALTER TABLE IF EXISTS ONLY public.annotation_files DROP CONSTRAINT IF EXISTS annotation_files_shape_type_annotation_id_format_key;
ALTER TABLE IF EXISTS ONLY public.annotation_files DROP CONSTRAINT IF EXISTS annotation_files_pkey;
ALTER TABLE IF EXISTS ONLY public.annotation_authors DROP CONSTRAINT IF EXISTS annotation_authors_pkey;
ALTER TABLE IF EXISTS ONLY public.annotation_authors DROP CONSTRAINT IF EXISTS annotation_authors_annotation_id_name_key;
ALTER TABLE IF EXISTS public.tomograms ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.tomogram_voxel_spacings ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.tomogram_authors ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.tiltseries ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.runs ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.dataset_funding ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.dataset_authors ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.annotations ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.annotation_files ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.annotation_authors ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE IF EXISTS public.tomograms_id_seq;
DROP TABLE IF EXISTS public.tomograms;
DROP SEQUENCE IF EXISTS public.tomogram_voxel_spacing_id_seq;
DROP TABLE IF EXISTS public.tomogram_voxel_spacings;
DROP TABLE IF EXISTS public.tomogram_type;
DROP SEQUENCE IF EXISTS public.tomogram_authors_id_seq;
DROP TABLE IF EXISTS public.tomogram_authors;
DROP SEQUENCE IF EXISTS public.tiltseries_id_seq;
DROP TABLE IF EXISTS public.tiltseries;
DROP SEQUENCE IF EXISTS public.runs_id_seq;
DROP TABLE IF EXISTS public.runs;
DROP TABLE IF EXISTS public.datasets;
DROP SEQUENCE IF EXISTS public.dataset_funding_id_seq;
DROP TABLE IF EXISTS public.dataset_funding;
DROP SEQUENCE IF EXISTS public.dataset_authors_id_seq;
DROP TABLE IF EXISTS public.dataset_authors;
DROP SEQUENCE IF EXISTS public.annotations_id_seq;
DROP TABLE IF EXISTS public.annotations;
DROP SEQUENCE IF EXISTS public.annotation_files_id_seq;
DROP TABLE IF EXISTS public.annotation_files;
DROP SEQUENCE IF EXISTS public.annotation_authors_id_seq;
DROP TABLE IF EXISTS public.annotation_authors;
DROP SCHEMA IF EXISTS public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: annotation_authors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.annotation_authors (
    id integer NOT NULL,
    annotation_id integer NOT NULL,
    name character varying NOT NULL,
    orcid character varying,
    corresponding_author_status boolean,
    primary_annotator_status boolean,
    email character varying,
    affiliation_name character varying,
    affiliation_address character varying,
    affiliation_identifier character varying,
    author_list_order integer,
    primary_author_status integer
);


--
-- Name: TABLE annotation_authors; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.annotation_authors IS 'Authors for an annotation';


--
-- Name: COLUMN annotation_authors.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.id IS 'Numeric identifier for this annotation author (this may change!)';


--
-- Name: COLUMN annotation_authors.annotation_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.annotation_id IS 'Reference to the annotation this author contributed to';


--
-- Name: COLUMN annotation_authors.name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.name IS 'Full name of an annotation author (e.g. Jane Doe).';


--
-- Name: COLUMN annotation_authors.orcid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.orcid IS 'A unique, persistent identifier for researchers, provided by ORCID.';


--
-- Name: COLUMN annotation_authors.corresponding_author_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.corresponding_author_status IS 'Indicating whether an annotator is the corresponding author (YES or NO)';


--
-- Name: COLUMN annotation_authors.primary_annotator_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.primary_annotator_status IS 'Indicating whether an annotator is the main person executing the annotation, especially on manual annotation (YES or NO)';


--
-- Name: COLUMN annotation_authors.email; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.email IS 'Email address for this author';


--
-- Name: COLUMN annotation_authors.affiliation_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.affiliation_name IS 'Name of the institution an annotator is affiliated with. Sometimes, one annotator may have multiple affiliations.';


--
-- Name: COLUMN annotation_authors.affiliation_address; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.affiliation_address IS 'Address of the institution an annotator is affiliated with.';


--
-- Name: COLUMN annotation_authors.affiliation_identifier; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.affiliation_identifier IS 'A unique identifier assigned to the affiliated institution by The Research Organization Registry (ROR).';


--
-- Name: COLUMN annotation_authors.author_list_order; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_authors.author_list_order IS 'The order in which the author appears in the publication';


--
-- Name: annotation_authors_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.annotation_authors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: annotation_authors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.annotation_authors_id_seq OWNED BY public.annotation_authors.id;


--
-- Name: annotation_files; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.annotation_files (
    id integer NOT NULL,
    annotation_id integer NOT NULL,
    shape_type character varying NOT NULL,
    format character varying NOT NULL,
    https_path character varying NOT NULL,
    s3_path character varying NOT NULL,
    is_visualization_default boolean DEFAULT false
);


--
-- Name: TABLE annotation_files; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.annotation_files IS 'Information about associated files for a given annotation';


--
-- Name: COLUMN annotation_files.shape_type; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_files.shape_type IS 'The type of the annotation';


--
-- Name: COLUMN annotation_files.format; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_files.format IS 'Format of the annotation object file';


--
-- Name: COLUMN annotation_files.https_path; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_files.https_path IS 'https path of the annotation file';


--
-- Name: COLUMN annotation_files.s3_path; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_files.s3_path IS 's3 path of the annotation file';


--
-- Name: COLUMN annotation_files.is_visualization_default; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotation_files.is_visualization_default IS 'Data curator’s subjective choice of default annotation to display in visualization for an object';


--
-- Name: annotation_files_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.annotation_files_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: annotation_files_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.annotation_files_id_seq OWNED BY public.annotation_files.id;


--
-- Name: annotations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.annotations (
    id integer NOT NULL,
    s3_metadata_path character varying NOT NULL,
    https_metadata_path character varying NOT NULL,
    deposition_date date NOT NULL,
    release_date date NOT NULL,
    last_modified_date date,
    annotation_publication character varying,
    annotation_method character varying NOT NULL,
    ground_truth_status boolean NOT NULL,
    object_name character varying NOT NULL,
    object_id character varying NOT NULL,
    object_description character varying,
    object_state character varying,
    object_count integer NOT NULL,
    confidence_precision numeric,
    confidence_recall numeric,
    ground_truth_used character varying,
    tomogram_voxel_spacing_id integer,
    annotation_software character varying,
    is_curator_recommended boolean DEFAULT false,
    deposition_id integer,
    method_type character varying
);


--
-- Name: TABLE annotations; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.annotations IS 'Inoformation about annotations for a given run';


--
-- Name: COLUMN annotations.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.id IS 'Numeric identifier (May change!)';


--
-- Name: COLUMN annotations.s3_metadata_path; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.s3_metadata_path IS 's3 path for the metadata json file for this annotation';


--
-- Name: COLUMN annotations.https_metadata_path; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.https_metadata_path IS 'https path for the metadata json file for this annotation';


--
-- Name: COLUMN annotations.deposition_date; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.deposition_date IS 'Date when an annotation set is initially received by the Data Portal.';


--
-- Name: COLUMN annotations.release_date; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.release_date IS 'Date when annotation data is made public by the Data Portal.';


--
-- Name: COLUMN annotations.last_modified_date; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.last_modified_date IS 'Date when an annotation was last modified in the Data Portal';


--
-- Name: COLUMN annotations.annotation_publication; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.annotation_publication IS 'DOIs for publications that describe the dataset. Use a comma to separate multiple DOIs.';


--
-- Name: COLUMN annotations.annotation_method; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.annotation_method IS 'Describe how the annotation is made (e.g. Manual, crYoLO, Positive Unlabeled Learning, template matching)';


--
-- Name: COLUMN annotations.ground_truth_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.ground_truth_status IS 'Whether an annotation is considered ground truth, as determined by the annotator.';


--
-- Name: COLUMN annotations.object_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.object_name IS 'Name of the object being annotated (e.g. ribosome, nuclear pore complex, actin filament, membrane)';


--
-- Name: COLUMN annotations.object_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.object_id IS 'Gene Ontology Cellular Component identifier for the annotation object';


--
-- Name: COLUMN annotations.object_description; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.object_description IS 'A textual description of the annotation object, can be a longer description to include additional information not covered by the Annotation object name and state.';


--
-- Name: COLUMN annotations.object_state; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.object_state IS 'Molecule state annotated (e.g. open, closed)';


--
-- Name: COLUMN annotations.object_count; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.object_count IS 'Number of objects identified';


--
-- Name: COLUMN annotations.confidence_precision; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.confidence_precision IS 'Describe the confidence level of the annotation. Precision is defined as the % of annotation objects being true positive';


--
-- Name: COLUMN annotations.confidence_recall; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.confidence_recall IS 'Describe the confidence level of the annotation. Recall is defined as the % of true positives being annotated correctly';


--
-- Name: COLUMN annotations.ground_truth_used; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.ground_truth_used IS 'Annotation filename used as ground truth for precision and recall';


--
-- Name: COLUMN annotations.is_curator_recommended; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.annotations.is_curator_recommended IS 'Data curator’s subjective choice as the best annotation of the same annotation object ID';


--
-- Name: annotations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.annotations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: annotations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.annotations_id_seq OWNED BY public.annotations.id;


--
-- Name: dataset_authors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dataset_authors (
    id integer NOT NULL,
    name character varying NOT NULL,
    orcid character varying,
    corresponding_author_status boolean,
    email character varying,
    affiliation_name character varying,
    affiliation_address character varying,
    affiliation_identifier character varying,
    dataset_id integer NOT NULL,
    primary_author_status boolean,
    author_list_order integer
);


--
-- Name: TABLE dataset_authors; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.dataset_authors IS 'Authors of a dataset';


--
-- Name: COLUMN dataset_authors.name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_authors.name IS 'Full name of a dataset author (e.g. Jane Doe).';


--
-- Name: COLUMN dataset_authors.orcid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_authors.orcid IS 'A unique, persistent identifier for researchers, provided by ORCID.';


--
-- Name: COLUMN dataset_authors.corresponding_author_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_authors.corresponding_author_status IS 'Indicating whether an author is the corresponding author';


--
-- Name: COLUMN dataset_authors.email; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_authors.email IS 'Email address for each author';


--
-- Name: COLUMN dataset_authors.affiliation_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_authors.affiliation_name IS 'Name of the institutions an author is affiliated with. Comma separated';


--
-- Name: COLUMN dataset_authors.affiliation_address; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_authors.affiliation_address IS 'Address of the institution an author is affiliated with.';


--
-- Name: COLUMN dataset_authors.affiliation_identifier; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_authors.affiliation_identifier IS 'A unique identifier assigned to the affiliated institution by The Research Organization Registry (ROR).';


--
-- Name: COLUMN dataset_authors.author_list_order; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_authors.author_list_order IS 'The order in which the author appears in the publication';


--
-- Name: dataset_authors_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dataset_authors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dataset_authors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dataset_authors_id_seq OWNED BY public.dataset_authors.id;


--
-- Name: dataset_funding; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.dataset_funding (
    id integer NOT NULL,
    dataset_id integer NOT NULL,
    funding_agency_name character varying NOT NULL,
    grant_id character varying
);


--
-- Name: TABLE dataset_funding; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.dataset_funding IS 'Funding sources for a dataset';


--
-- Name: COLUMN dataset_funding.funding_agency_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_funding.funding_agency_name IS 'Name of the funding agency.';


--
-- Name: COLUMN dataset_funding.grant_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.dataset_funding.grant_id IS 'Grant identifier provided by the funding agency.';


--
-- Name: dataset_funding_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.dataset_funding_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: dataset_funding_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.dataset_funding_id_seq OWNED BY public.dataset_funding.id;


--
-- Name: datasets; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.datasets (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    deposition_date date NOT NULL,
    release_date date NOT NULL,
    last_modified_date date,
    related_database_entries character varying,
    related_database_links character varying,
    dataset_publications character varying,
    dataset_citations character varying,
    sample_type character varying NOT NULL,
    organism_name character varying,
    organism_taxid character varying,
    tissue_name character varying,
    tissue_id character varying,
    cell_name character varying,
    cell_type_id character varying,
    cell_strain_name character varying,
    cell_strain_id character varying,
    sample_preparation character varying,
    grid_preparation character varying,
    other_setup character varying,
    s3_prefix character varying NOT NULL,
    https_prefix character varying NOT NULL,
    key_photo_url character varying,
    key_photo_thumbnail_url character varying,
    cell_component_name character varying,
    cell_component_id character varying
);


--
-- Name: TABLE datasets; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.datasets IS 'Dataset Metadata';


--
-- Name: COLUMN datasets.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.id IS 'An identifier for a CryoET dataset, assigned by the Data Portal. Used to identify the dataset as the directory name in data tree';


--
-- Name: COLUMN datasets.title; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.title IS 'Title of a CryoET dataset';


--
-- Name: COLUMN datasets.description; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.description IS 'A short description of a CryoET dataset, similar to an abstract for a journal article or dataset.';


--
-- Name: COLUMN datasets.deposition_date; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.deposition_date IS 'Date when a dataset is initially received by the Data Portal.';


--
-- Name: COLUMN datasets.release_date; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.release_date IS 'Date when a dataset is made available on the Data Portal.';


--
-- Name: COLUMN datasets.last_modified_date; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.last_modified_date IS 'Date when a released dataset is last modified.';


--
-- Name: COLUMN datasets.related_database_entries; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.related_database_entries IS 'If a CryoET dataset is also deposited into another database, enter the database identifier here (e.g. EMPIAR-11445). Use a comma to separate multiple identifiers.';


--
-- Name: COLUMN datasets.related_database_links; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.related_database_links IS 'If a CryoET dataset is also deposited into another database, e.g. EMPAIR, enter the database identifier here (e.g.https://www.ebi.ac.uk/empiar/EMPIAR-12345/).  Use a comma to separate multiple links.';


--
-- Name: COLUMN datasets.dataset_publications; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.dataset_publications IS 'DOIs for publications that describe the dataset. Use a comma to separate multiple DOIs.';


--
-- Name: COLUMN datasets.dataset_citations; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.dataset_citations IS 'DOIs for publications that cite the dataset. Use a comma to separate multiple DOIs.';


--
-- Name: COLUMN datasets.sample_type; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.sample_type IS 'Type of samples used in a CryoET study. (cell, tissue, organism, intact organelle, in-vitro mixture, in-silico synthetic data, other)';


--
-- Name: COLUMN datasets.organism_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.organism_name IS 'Name of the organism from which a biological sample used in a CryoET study is derived from, e.g. homo sapiens';


--
-- Name: COLUMN datasets.organism_taxid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.organism_taxid IS 'NCBI taxonomy identifier for the organism, e.g. 9606';


--
-- Name: COLUMN datasets.tissue_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.tissue_name IS 'Name of the tissue from which a biological sample used in a CryoET study is derived from.';


--
-- Name: COLUMN datasets.tissue_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.tissue_id IS 'UBERON identifier for the tissue';


--
-- Name: COLUMN datasets.cell_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.cell_name IS 'Name of the cell from which a biological sample used in a CryoET study is derived from.';


--
-- Name: COLUMN datasets.cell_type_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.cell_type_id IS 'Cell Ontology identifier for the cell type';


--
-- Name: COLUMN datasets.cell_strain_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.cell_strain_name IS 'Cell line or strain for the sample.';


--
-- Name: COLUMN datasets.cell_strain_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.cell_strain_id IS 'NCBI Identifier for the cell line or strain';


--
-- Name: COLUMN datasets.sample_preparation; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.sample_preparation IS 'Describe how the sample was prepared.';


--
-- Name: COLUMN datasets.grid_preparation; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.grid_preparation IS 'Describe Cryo-ET grid preparation.';


--
-- Name: COLUMN datasets.other_setup; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.other_setup IS 'Describe other setup not covered by sample preparation or grid preparation that may make this dataset unique in  the same publication';


--
-- Name: COLUMN datasets.s3_prefix; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.s3_prefix IS 'The S3 public bucket path where this dataset is contained';


--
-- Name: COLUMN datasets.https_prefix; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.https_prefix IS 'The https directory path where this dataset is contained';


--
-- Name: COLUMN datasets.key_photo_url; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.key_photo_url IS 'URL for the dataset preview image.';


--
-- Name: COLUMN datasets.key_photo_thumbnail_url; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.key_photo_thumbnail_url IS 'URL for the thumbnail of preview image.';


--
-- Name: COLUMN datasets.cell_component_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.cell_component_name IS 'Name of the cellular component';


--
-- Name: COLUMN datasets.cell_component_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.datasets.cell_component_id IS 'If this dataset only focuses on a specific part of a cell, include the subset here';


--
-- Name: runs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.runs (
    id integer NOT NULL,
    dataset_id integer NOT NULL,
    name character varying NOT NULL,
    s3_prefix character varying NOT NULL,
    https_prefix character varying NOT NULL
);


--
-- Name: TABLE runs; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.runs IS 'Data related to an experiment run';


--
-- Name: COLUMN runs.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.runs.id IS 'Numeric identifier (May change!)';


--
-- Name: COLUMN runs.dataset_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.runs.dataset_id IS 'Reference to the dataset this run is a part of';


--
-- Name: COLUMN runs.name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.runs.name IS 'Short name for the tilt series';


--
-- Name: COLUMN runs.s3_prefix; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.runs.s3_prefix IS 'The S3 public bucket path where this dataset is contained';


--
-- Name: COLUMN runs.https_prefix; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.runs.https_prefix IS 'The https directory path where this dataset is contained';


--
-- Name: runs_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.runs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: runs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.runs_id_seq OWNED BY public.runs.id;


--
-- Name: tiltseries; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tiltseries (
    id integer NOT NULL,
    run_id integer NOT NULL,
    s3_mrc_bin1 character varying NOT NULL,
    s3_omezarr_dir character varying NOT NULL,
    https_mrc_bin1 character varying NOT NULL,
    https_omezarr_dir character varying NOT NULL,
    s3_collection_metadata character varying,
    https_collection_metadata character varying,
    s3_angle_list character varying,
    https_angle_list character varying,
    s3_alignment_file character varying,
    https_alignment_file character varying,
    acceleration_voltage integer NOT NULL,
    spherical_aberration_constant numeric NOT NULL,
    microscope_manufacturer character varying NOT NULL,
    microscope_model character varying NOT NULL,
    microscope_energy_filter character varying NOT NULL,
    microscope_phase_plate character varying,
    microscope_image_corrector character varying,
    microscope_additional_info character varying,
    camera_manufacturer character varying NOT NULL,
    camera_model character varying NOT NULL,
    tilt_min numeric NOT NULL,
    tilt_max numeric NOT NULL,
    tilt_range numeric NOT NULL,
    tilt_step numeric NOT NULL,
    tilting_scheme character varying NOT NULL,
    tilt_axis numeric NOT NULL,
    total_flux numeric NOT NULL,
    data_acquisition_software character varying NOT NULL,
    related_empiar_entry character varying,
    binning_from_frames numeric,
    tilt_series_quality integer NOT NULL,
    is_aligned boolean DEFAULT false NOT NULL,
    pixel_spacing numeric,
    aligned_tiltseries_binning integer,
    frames_count integer DEFAULT 0
);


--
-- Name: TABLE tiltseries; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.tiltseries IS 'Tilt Series Metadata';


--
-- Name: COLUMN tiltseries.acceleration_voltage; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.acceleration_voltage IS 'Electron Microscope Accelerator voltage in volts';


--
-- Name: COLUMN tiltseries.spherical_aberration_constant; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.spherical_aberration_constant IS 'Spherical Aberration Constant of the objective lens in millimeters';


--
-- Name: COLUMN tiltseries.microscope_manufacturer; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.microscope_manufacturer IS 'Name of the microscope manufacturer';


--
-- Name: COLUMN tiltseries.microscope_model; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.microscope_model IS 'Microscope model name';


--
-- Name: COLUMN tiltseries.microscope_energy_filter; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.microscope_energy_filter IS 'Energy filter setup used';


--
-- Name: COLUMN tiltseries.microscope_phase_plate; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.microscope_phase_plate IS 'Phase plate configuration';


--
-- Name: COLUMN tiltseries.microscope_image_corrector; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.microscope_image_corrector IS 'Image corrector setup';


--
-- Name: COLUMN tiltseries.microscope_additional_info; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.microscope_additional_info IS 'Other microscope optical setup information, in addition to energy filter, phase plate and image corrector';


--
-- Name: COLUMN tiltseries.camera_manufacturer; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.camera_manufacturer IS 'Name of the camera manufacturer';


--
-- Name: COLUMN tiltseries.camera_model; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.camera_model IS 'Camera model name';


--
-- Name: COLUMN tiltseries.tilt_min; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.tilt_min IS 'Minimal tilt angle in degrees';


--
-- Name: COLUMN tiltseries.tilt_max; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.tilt_max IS 'Maximal tilt angle in degrees';


--
-- Name: COLUMN tiltseries.tilt_range; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.tilt_range IS 'The difference between tilt_min and tilt_max';


--
-- Name: COLUMN tiltseries.tilting_scheme; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.tilting_scheme IS 'The order of stage tilting during acquisition of the data';


--
-- Name: COLUMN tiltseries.tilt_axis; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.tilt_axis IS 'Rotation angle in degrees';


--
-- Name: COLUMN tiltseries.total_flux; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.total_flux IS 'Number of Electrons reaching the specimen in a square Angstrom area for the entire tilt series';


--
-- Name: COLUMN tiltseries.data_acquisition_software; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.data_acquisition_software IS 'Software used to collect data';


--
-- Name: COLUMN tiltseries.related_empiar_entry; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.related_empiar_entry IS 'If a tilt series is deposited into EMPIAR, enter the EMPIAR dataset identifier';


--
-- Name: COLUMN tiltseries.binning_from_frames; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.binning_from_frames IS 'Describes the binning factor from frames to tilt series file';


--
-- Name: COLUMN tiltseries.tilt_series_quality; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.tilt_series_quality IS 'Author assessment of tilt series quality within the dataset (1-5, 5 is best)';


--
-- Name: COLUMN tiltseries.is_aligned; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.is_aligned IS 'Tilt series is aligned';


--
-- Name: COLUMN tiltseries.pixel_spacing; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.pixel_spacing IS 'Pixel spacing equal in both axes in angstrom';


--
-- Name: COLUMN tiltseries.aligned_tiltseries_binning; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.aligned_tiltseries_binning IS 'The binning factor between the unaligned tilt series and the aligned tiltseries.';


--
-- Name: COLUMN tiltseries.frames_count; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tiltseries.frames_count IS 'Number of frames associated to the tilt series';


--
-- Name: tiltseries_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tiltseries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tiltseries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tiltseries_id_seq OWNED BY public.tiltseries.id;


--
-- Name: tomogram_authors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tomogram_authors (
    id integer NOT NULL,
    tomogram_id integer NOT NULL,
    author_list_order integer NOT NULL,
    name character varying NOT NULL,
    orcid character varying,
    corresponding_author_status boolean,
    primary_author_status boolean,
    email character varying,
    affiliation_name character varying,
    affiliation_address character varying,
    affiliation_identifier character varying
);


--
-- Name: TABLE tomogram_authors; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.tomogram_authors IS 'Authors for a tomogram';


--
-- Name: COLUMN tomogram_authors.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.id IS 'Numeric identifier for this tomogram author (this may change!)';


--
-- Name: COLUMN tomogram_authors.tomogram_id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.tomogram_id IS 'Reference to the tomogram this author contributed to';


--
-- Name: COLUMN tomogram_authors.author_list_order; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.author_list_order IS 'The order in which the author appears in the publication';


--
-- Name: COLUMN tomogram_authors.name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.name IS 'Full name of an tomogram author (e.g. Jane Doe).';


--
-- Name: COLUMN tomogram_authors.orcid; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.orcid IS 'A unique, persistent identifier for researchers, provided by ORCID.';


--
-- Name: COLUMN tomogram_authors.corresponding_author_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.corresponding_author_status IS 'Indicating whether an author is the corresponding author (YES or NO)';


--
-- Name: COLUMN tomogram_authors.primary_author_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.primary_author_status IS 'Indicating whether an author is the main person creating the tomogram (YES or NO)';


--
-- Name: COLUMN tomogram_authors.email; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.email IS 'Email address for this author';


--
-- Name: COLUMN tomogram_authors.affiliation_name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.affiliation_name IS 'Name of the institution an annotator is affiliated with. Sometimes, one annotator may have multiple affiliations.';


--
-- Name: COLUMN tomogram_authors.affiliation_address; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.affiliation_address IS 'Address of the institution an annotator is affiliated with.';


--
-- Name: COLUMN tomogram_authors.affiliation_identifier; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomogram_authors.affiliation_identifier IS 'A unique identifier assigned to the affiliated institution by The Research Organization Registry (ROR).';


--
-- Name: tomogram_authors_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tomogram_authors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tomogram_authors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tomogram_authors_id_seq OWNED BY public.tomogram_authors.id;


--
-- Name: tomogram_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tomogram_type (
    value text NOT NULL,
    description text
);


--
-- Name: TABLE tomogram_type; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.tomogram_type IS 'The type of tomograms';


--
-- Name: tomogram_voxel_spacings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tomogram_voxel_spacings (
    id integer NOT NULL,
    run_id integer NOT NULL,
    voxel_spacing numeric NOT NULL,
    s3_prefix character varying,
    https_prefix character varying
);


--
-- Name: TABLE tomogram_voxel_spacings; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.tomogram_voxel_spacings IS 'The tomograms for each run are grouped by their voxel spacing';


--
-- Name: tomogram_voxel_spacing_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tomogram_voxel_spacing_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tomogram_voxel_spacing_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tomogram_voxel_spacing_id_seq OWNED BY public.tomogram_voxel_spacings.id;


--
-- Name: tomograms; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tomograms (
    id integer NOT NULL,
    name character varying NOT NULL,
    size_x integer NOT NULL,
    size_y integer NOT NULL,
    size_z integer NOT NULL,
    voxel_spacing numeric NOT NULL,
    fiducial_alignment_status character varying NOT NULL,
    reconstruction_method character varying NOT NULL,
    reconstruction_software character varying NOT NULL,
    processing character varying NOT NULL,
    processing_software character varying,
    tomogram_version character varying NOT NULL,
    is_canonical boolean,
    s3_omezarr_dir character varying NOT NULL,
    https_omezarr_dir character varying NOT NULL,
    s3_mrc_scale0 character varying NOT NULL,
    https_mrc_scale0 character varying NOT NULL,
    scale0_dimensions character varying NOT NULL,
    scale1_dimensions character varying NOT NULL,
    scale2_dimensions character varying NOT NULL,
    ctf_corrected boolean,
    tomogram_voxel_spacing_id integer,
    offset_x integer DEFAULT 0 NOT NULL,
    offset_y integer DEFAULT 0 NOT NULL,
    offset_z integer DEFAULT 0 NOT NULL,
    affine_transformation_matrix numeric[],
    key_photo_url character varying,
    key_photo_thumbnail_url character varying,
    neuroglancer_config character varying,
    type text,
    deposition_id integer
);


--
-- Name: TABLE tomograms; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.tomograms IS 'information about the tomograms in the CryoET Data Portal';


--
-- Name: COLUMN tomograms.id; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.id IS 'Numeric identifier for this tomogram (this may change!)';


--
-- Name: COLUMN tomograms.name; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.name IS 'Short name for this tomogram';


--
-- Name: COLUMN tomograms.size_x; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.size_x IS 'Number of pixels in the 3D data fast axis';


--
-- Name: COLUMN tomograms.size_y; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.size_y IS 'Number of pixels in the 3D data medium axis';


--
-- Name: COLUMN tomograms.size_z; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.size_z IS 'Number of pixels in the 3D data slow axis.  This is the image projection direction at zero stage tilt';


--
-- Name: COLUMN tomograms.voxel_spacing; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.voxel_spacing IS 'Voxel spacing equal in all three axes in angstroms';


--
-- Name: COLUMN tomograms.fiducial_alignment_status; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.fiducial_alignment_status IS 'Fiducial Alignment status: True = aligned with fiducial False = aligned without fiducial';


--
-- Name: COLUMN tomograms.reconstruction_method; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.reconstruction_method IS 'Describe reconstruction method (Weighted backprojection, SART, SIRT)';


--
-- Name: COLUMN tomograms.reconstruction_software; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.reconstruction_software IS 'Name of software used for reconstruction';


--
-- Name: COLUMN tomograms.processing; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.processing IS 'Describe additional processing used to derive the tomogram';


--
-- Name: COLUMN tomograms.processing_software; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.processing_software IS 'Processing software used to derive the tomogram';


--
-- Name: COLUMN tomograms.tomogram_version; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.tomogram_version IS 'Version of tomogram using the same software and post-processing. Version of tomogram using the same software and post-processing. This will be presented as the latest version';


--
-- Name: COLUMN tomograms.is_canonical; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.is_canonical IS 'Is this tomogram considered the canonical tomogram for the run experiment? True=Yes';


--
-- Name: COLUMN tomograms.s3_omezarr_dir; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.s3_omezarr_dir IS 'S3 path to the this multiscale omezarr tomogram';


--
-- Name: COLUMN tomograms.https_omezarr_dir; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.https_omezarr_dir IS 'HTTPS path to the this multiscale omezarr tomogram';


--
-- Name: COLUMN tomograms.s3_mrc_scale0; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.s3_mrc_scale0 IS 'S3 path to this tomogram in MRC format (no scaling)';


--
-- Name: COLUMN tomograms.https_mrc_scale0; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.https_mrc_scale0 IS 'https path to this tomogram in MRC format (no scaling)';


--
-- Name: COLUMN tomograms.scale0_dimensions; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.scale0_dimensions IS 'comma separated x,y,z dimensions of the unscaled tomogram';


--
-- Name: COLUMN tomograms.scale1_dimensions; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.scale1_dimensions IS 'comma separated x,y,z dimensions of the scale1 tomogram';


--
-- Name: COLUMN tomograms.scale2_dimensions; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.scale2_dimensions IS 'comma separated x,y,z dimensions of the scale2 tomogram';


--
-- Name: COLUMN tomograms.offset_x; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.offset_x IS 'x offset data relative to the canonical tomogram in pixels';


--
-- Name: COLUMN tomograms.offset_y; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.offset_y IS 'y offset data relative to the canonical tomogram in pixels';


--
-- Name: COLUMN tomograms.offset_z; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.offset_z IS 'z offset data relative to the canonical tomogram in pixels';


--
-- Name: COLUMN tomograms.affine_transformation_matrix; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.affine_transformation_matrix IS 'The flip or rotation transformation of this author submitted tomogram is indicated here';


--
-- Name: COLUMN tomograms.key_photo_url; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.key_photo_url IS 'URL for the key photo';


--
-- Name: COLUMN tomograms.key_photo_thumbnail_url; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.key_photo_thumbnail_url IS 'URL for the thumbnail of key photo';


--
-- Name: COLUMN tomograms.neuroglancer_config; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN public.tomograms.neuroglancer_config IS 'the compact json of neuroglancer config';


--
-- Name: tomograms_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tomograms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tomograms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tomograms_id_seq OWNED BY public.tomograms.id;


--
-- Name: annotation_authors id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotation_authors ALTER COLUMN id SET DEFAULT nextval('public.annotation_authors_id_seq'::regclass);


--
-- Name: annotation_files id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotation_files ALTER COLUMN id SET DEFAULT nextval('public.annotation_files_id_seq'::regclass);


--
-- Name: annotations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotations ALTER COLUMN id SET DEFAULT nextval('public.annotations_id_seq'::regclass);


--
-- Name: dataset_authors id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dataset_authors ALTER COLUMN id SET DEFAULT nextval('public.dataset_authors_id_seq'::regclass);


--
-- Name: dataset_funding id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dataset_funding ALTER COLUMN id SET DEFAULT nextval('public.dataset_funding_id_seq'::regclass);


--
-- Name: runs id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.runs ALTER COLUMN id SET DEFAULT nextval('public.runs_id_seq'::regclass);


--
-- Name: tiltseries id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tiltseries ALTER COLUMN id SET DEFAULT nextval('public.tiltseries_id_seq'::regclass);


--
-- Name: tomogram_authors id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomogram_authors ALTER COLUMN id SET DEFAULT nextval('public.tomogram_authors_id_seq'::regclass);


--
-- Name: tomogram_voxel_spacings id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomogram_voxel_spacings ALTER COLUMN id SET DEFAULT nextval('public.tomogram_voxel_spacing_id_seq'::regclass);


--
-- Name: tomograms id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomograms ALTER COLUMN id SET DEFAULT nextval('public.tomograms_id_seq'::regclass);


--
-- Name: annotation_authors annotation_authors_annotation_id_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotation_authors
    ADD CONSTRAINT annotation_authors_annotation_id_name_key UNIQUE (annotation_id, name);


--
-- Name: annotation_authors annotation_authors_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotation_authors
    ADD CONSTRAINT annotation_authors_pkey PRIMARY KEY (id);


--
-- Name: annotation_files annotation_files_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotation_files
    ADD CONSTRAINT annotation_files_pkey PRIMARY KEY (id);


--
-- Name: annotation_files annotation_files_shape_type_annotation_id_format_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotation_files
    ADD CONSTRAINT annotation_files_shape_type_annotation_id_format_key UNIQUE (shape_type, annotation_id, format);


--
-- Name: annotations annotations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotations
    ADD CONSTRAINT annotations_pkey PRIMARY KEY (id);


--
-- Name: dataset_authors dataset_authors_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dataset_authors
    ADD CONSTRAINT dataset_authors_pkey PRIMARY KEY (id);


--
-- Name: dataset_funding dataset_funding_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dataset_funding
    ADD CONSTRAINT dataset_funding_pkey PRIMARY KEY (id);


--
-- Name: datasets datasets_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.datasets
    ADD CONSTRAINT datasets_pkey PRIMARY KEY (id);


--
-- Name: runs runs_dataset_id_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.runs
    ADD CONSTRAINT runs_dataset_id_name_key UNIQUE (dataset_id, name);


--
-- Name: runs runs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.runs
    ADD CONSTRAINT runs_pkey PRIMARY KEY (id);


--
-- Name: tiltseries tiltseries_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tiltseries
    ADD CONSTRAINT tiltseries_pkey PRIMARY KEY (id);


--
-- Name: tomogram_authors tomogram_authors_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomogram_authors
    ADD CONSTRAINT tomogram_authors_pkey PRIMARY KEY (id);


--
-- Name: tomogram_authors tomogram_authors_tomogram_id_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomogram_authors
    ADD CONSTRAINT tomogram_authors_tomogram_id_name_key UNIQUE (tomogram_id, name);


--
-- Name: tomogram_type tomogram_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomogram_type
    ADD CONSTRAINT tomogram_type_pkey PRIMARY KEY (value);


--
-- Name: tomogram_voxel_spacings tomogram_voxel_spacing_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomogram_voxel_spacings
    ADD CONSTRAINT tomogram_voxel_spacing_pkey PRIMARY KEY (id);


--
-- Name: tomograms tomograms_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomograms
    ADD CONSTRAINT tomograms_pkey PRIMARY KEY (id);


--
-- Name: annotation_files_annotation_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX annotation_files_annotation_id ON public.annotation_files USING btree (annotation_id);


--
-- Name: annotations_tomogram_voxel_spacing; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX annotations_tomogram_voxel_spacing ON public.annotations USING btree (tomogram_voxel_spacing_id);


--
-- Name: dataset_authors_dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX dataset_authors_dataset ON public.dataset_authors USING btree (dataset_id);


--
-- Name: dataset_funding_dataset; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX dataset_funding_dataset ON public.dataset_funding USING btree (dataset_id);


--
-- Name: tiltseries_run; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX tiltseries_run ON public.tiltseries USING btree (run_id);


--
-- Name: tomogram_voxel_spacing_run; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX tomogram_voxel_spacing_run ON public.tomogram_voxel_spacings USING btree (run_id);


--
-- Name: tomograms_tomogram_voxel_spacing_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX tomograms_tomogram_voxel_spacing_id ON public.tomograms USING btree (tomogram_voxel_spacing_id);


--
-- Name: annotation_authors annotation_authors_annotation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotation_authors
    ADD CONSTRAINT annotation_authors_annotation_id_fkey FOREIGN KEY (annotation_id) REFERENCES public.annotations(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: annotation_files annotation_files_annotation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotation_files
    ADD CONSTRAINT annotation_files_annotation_id_fkey FOREIGN KEY (annotation_id) REFERENCES public.annotations(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: annotations annotations_tomogram_voxel_spacing_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.annotations
    ADD CONSTRAINT annotations_tomogram_voxel_spacing_id_fkey FOREIGN KEY (tomogram_voxel_spacing_id) REFERENCES public.tomogram_voxel_spacings(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: dataset_authors dataset_authors_dataset_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dataset_authors
    ADD CONSTRAINT dataset_authors_dataset_id_fkey FOREIGN KEY (dataset_id) REFERENCES public.datasets(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: dataset_funding dataset_funding_dataset_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.dataset_funding
    ADD CONSTRAINT dataset_funding_dataset_id_fkey FOREIGN KEY (dataset_id) REFERENCES public.datasets(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: runs runs_dataset_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.runs
    ADD CONSTRAINT runs_dataset_id_fkey FOREIGN KEY (dataset_id) REFERENCES public.datasets(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: tiltseries tiltseries_run_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tiltseries
    ADD CONSTRAINT tiltseries_run_id_fkey FOREIGN KEY (run_id) REFERENCES public.runs(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: tomogram_authors tomogram_authors_tomogram_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomogram_authors
    ADD CONSTRAINT tomogram_authors_tomogram_id_fkey FOREIGN KEY (tomogram_id) REFERENCES public.tomograms(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: tomogram_voxel_spacings tomogram_voxel_spacing_run_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomogram_voxel_spacings
    ADD CONSTRAINT tomogram_voxel_spacing_run_id_fkey FOREIGN KEY (run_id) REFERENCES public.runs(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: tomograms tomograms_tomogram_voxel_spacing_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomograms
    ADD CONSTRAINT tomograms_tomogram_voxel_spacing_id_fkey FOREIGN KEY (tomogram_voxel_spacing_id) REFERENCES public.tomogram_voxel_spacings(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: tomograms tomograms_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tomograms
    ADD CONSTRAINT tomograms_type_fkey FOREIGN KEY (type) REFERENCES public.tomogram_type(value) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- PostgreSQL database dump complete
--
