drop view [navy].[user_wide_table] ;

CREATE VIEW [navy].[user_wide_table] AS
with vt_hot_topics_in_7_d as (
SELECT
	topic_type_uid,
	topic_subtype_uid,
	(
	SELECT
		topic,
		tk_notes,
		my_notes,
		account_position
	FROM
		dbmeteor.navy.hot_topics_in_7_d AS ht1
	WHERE
		ht1.topic_type_uid = ht2.topic_type_uid
		and ht1.topic_subtype_uid = ht2.topic_subtype_uid
        FOR JSON PATH
    ) AS topics_json
FROM
	dbmeteor.navy.hot_topics_in_7_d ht2
GROUP BY
	ht2.topic_type_uid,
	ht2.topic_subtype_uid)
select
	user_uid,
	gmail_user,
	gmail_password,
	gmail_recovery_email,
	tiktok_user_nm,
	tiktok_birth_year,
	tiktok_birth_month,
	tiktok_birth_day,
	head_portrait,
	gender,
	account_status,
	account_type,
	area,
	max(topic_type_en) as topic_type_en,
	max(topic_type_cn) as topic_type_cn,
	max(topic_subtype_en) as topic_subtype_en,
	max(topic_subtype_cn) as topic_subtype_cn,
	max(topic_message) as topic_message,
	max(user_tag_en) as user_tag_en,
	max(user_tag_cn) as user_tag_cn
from
	(
	select
		t1.user_uid,
		t1.gmail_user,
		t1.gmail_password,
		t1.gmail_recovery_email,
		t1.tiktok_user_nm,
		t1.tiktok_birth_year,
		t1.tiktok_birth_month,
		t1.tiktok_birth_day,
		t1.head_portrait,
		t1.gender,
		t1.account_status,
		t1.account_type,
		t2.area,
		t3.topic_type_en as topic_type_en,
		t3.topic_type_cn as topic_type_cn,
		t4.topic_subtype_en as topic_subtype_en,
		t4.topic_subtype_cn as topic_subtype_cn,
		t5.topics_json as topic_message,
		null as user_tag_en,
		null as user_tag_cn
	FROM
		dbmeteor.navy.user_baseinfo t1
	inner join dbmeteor.navy.usertag_rel t2
	CROSS APPLY
	STRING_SPLIT(REPLACE(REPLACE(t2.attributes1_uid , '{', ''), '}', ''),
		',') AS t2_1
	CROSS APPLY
	STRING_SPLIT(REPLACE(REPLACE(t2.attributes2_uid , '{', ''), '}', ''),
		',') AS t2_2
	on
		t1.user_uid = t2.user_uid
	inner join dbmeteor.navy.topic_type t3
	on
		t3.topic_type_uid = cast(t2_1.value AS INT)
	inner join dbmeteor.navy.topic_subtype t4
	on
		t4.topic_subtype_uid = cast(t2_2.value AS INT)
	left join vt_hot_topics_in_7_d t5
	on
		t3.topic_type_uid = t5.topic_type_uid
			and t4.topic_subtype_uid = t5.topic_subtype_uid
		where
			t2.spread_type = 'topic'
	union all
		select
			t1.user_uid,
			t1.gmail_user,
			t1.gmail_password,
			t1.gmail_recovery_email,
			t1.tiktok_user_nm,
			t1.tiktok_birth_year,
			t1.tiktok_birth_month,
			t1.tiktok_birth_day,
			t1.head_portrait,
			t1.gender,
			t1.account_status,
			t1.account_type,
			t2.area,
			null as topic_type_en,
			null as topic_type_cn,
			null as topic_subtype_en,
			null as topic_subtype_cn,
			null as topic_message,
			t3.user_tag_en as user_tag_en,
			t3.user_tag_cn as user_tag_cn
		FROM
			dbmeteor.navy.user_baseinfo t1
		inner join dbmeteor.navy.usertag_rel t2
	CROSS APPLY
	STRING_SPLIT(REPLACE(REPLACE(t2.attributes1_uid , '{', ''), '}', ''),
			',') AS t2_1
	on
			t1.user_uid = t2.user_uid
		inner join dbmeteor.navy.user_tag t3
	on
			t3.user_tag_uid = cast(t2_1.value AS INT)
		where
			t2.spread_type = 'tag') v
group by
	user_uid,
	gmail_user,
	gmail_password,
	gmail_recovery_email,
	tiktok_user_nm,
	tiktok_birth_year,
	tiktok_birth_month,
	tiktok_birth_day,
	head_portrait,
	gender,
	account_status,
	account_type,
	area