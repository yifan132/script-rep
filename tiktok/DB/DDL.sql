-- dbmeteor.navy.hot_topics_in_7_d definition

-- Drop table

-- DROP TABLE dbmeteor.navy.hot_topics_in_7_d;

CREATE TABLE dbmeteor.navy.hot_topics_in_7_d (
	id int NULL,
	topic_type_uid int NULL,
	topic_type_cn nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	[rank] int NULL,
	topic nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	tk_notes nvarchar(256) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	my_notes nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	account_position nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	search_keyword_cn nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	search_keyword_en nvarchar(64) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	topic_subtype_uid int NULL,
	topic_subtype_cn nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	weights real NULL,
	topic_subtype_en nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	topic_type_en nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


-- dbmeteor.navy.topic_subtype definition

-- Drop table

-- DROP TABLE dbmeteor.navy.topic_subtype;

CREATE TABLE dbmeteor.navy.topic_subtype (
	topic_subtype_uid int NULL,
	topic_subtype_cn nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	toppic_type_uid int NULL,
	comments nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	area nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	topic_subtype_en nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


-- dbmeteor.navy.topic_type definition

-- Drop table

-- DROP TABLE dbmeteor.navy.topic_type;

CREATE TABLE dbmeteor.navy.topic_type (
	topic_type_uid int NULL,
	topic_type_cn nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	comments nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	area nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	topic_type_en nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


-- dbmeteor.navy.user_baseinfo definition

-- Drop table

-- DROP TABLE dbmeteor.navy.user_baseinfo;

CREATE TABLE dbmeteor.navy.user_baseinfo (
	user_uid int NULL,
	gmail_user nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	gmail_password nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	gmail_recovery_email nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	tiktok_user_nm nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	tiktok_birth_year int NULL,
	tiktok_birth_month int NULL,
	tiktok_birth_day int NULL,
	head_portrait nvarchar(MAX) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	gender nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	account_status nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	account_type nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	comments nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	user_brief nvarchar(128) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


-- dbmeteor.navy.user_tag definition

-- Drop table

-- DROP TABLE dbmeteor.navy.user_tag;

CREATE TABLE dbmeteor.navy.user_tag (
	user_tag_uid int NULL,
	user_tag_cn nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	user_tag_en nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	comments nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	area nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


-- dbmeteor.navy.user_tag_group definition

-- Drop table

-- DROP TABLE dbmeteor.navy.user_tag_group;

CREATE TABLE dbmeteor.navy.user_tag_group (
	user_tag_group_uid int NULL,
	user_tag_uid nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	user_tag_group_cn nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	user_tag_group_en nvarchar(128) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	comments nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	area nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


-- dbmeteor.navy.user_tag_topics_subtype_mapping definition

-- Drop table

-- DROP TABLE dbmeteor.navy.user_tag_topics_subtype_mapping;

CREATE TABLE dbmeteor.navy.user_tag_topics_subtype_mapping (
	t_t_m_uid int NULL,
	user_tag_uid int NULL,
	topoc_subtype_uid int NULL,
	area nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);


-- dbmeteor.navy.usertag_rel definition

-- Drop table

-- DROP TABLE dbmeteor.navy.usertag_rel;

CREATE TABLE dbmeteor.navy.usertag_rel (
	usertag_rel_uid int NULL,
	user_uid int NULL,
	spread_type nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	attributes1_uid nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	attributes2_uid nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	comments nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	area nvarchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
);