SELECT code, estrato, sexo, m_grado, m_activo, m_tesis, per_cancelados, per_matriculados, bajos_rendimientos, trans_type_code, count(trans_type_code)
FROM public.copytransaction, public.student, public.transactiontype
WHERE trans_borrower_code = student.id and trans_type_id = transactiontype.id and trans_location_code_id = 5 and trans_type_code = 'ISS'
GROUP BY code, estrato, sexo, m_grado, m_activo, m_tesis, per_cancelados, per_matriculados, bajos_rendimientos, trans_type_code


-- prestamos vs bajos
SELECT code, bajos_rendimientos, trans_type_code, count(trans_type_code)
FROM public.copytransaction, public.student, public.transactiontype
WHERE trans_borrower_code = student.id and trans_type_id = transactiontype.id and trans_location_code_id = 5 and trans_type_code = 'ISS'
GROUP BY code, bajos_rendimientos, trans_type_code

-- with age
SELECT code, estrato,
DATE_PART('year', to_date(SUBSTRING(code::text, 1, 4)::text, 'YYYY')) - DATE_PART('year', student.birth_date::date) as age,
sexo, m_grado, m_activo, m_tesis, per_cancelados, per_matriculados, bajos_rendimientos, trans_type_code, count(trans_type_code)
FROM public.copytransaction, public.student, public.transactiontype, public.date
WHERE trans_borrower_code = student.id
	AND trans_type_id = transactiontype.id
	AND trans_location_code_id = 5
	AND trans_type_code = 'ISS'
	AND trans_date_id = date.id
GROUP BY code, estrato, sexo, m_grado, m_activo, m_tesis, per_cancelados, age, per_matriculados, bajos_rendimientos, trans_type_code


-- prestamos algoritmo apriori
SELECT code, trans_date_id, copy.id as copy_id
FROM public.copytransaction, public.copy, public.student, public.title, public.transactiontype
WHERE
	trans_borrower_code = student.id and
	trans_copy_code_id = copy.id and
	trans_tittle_code_id = title.id and
	trans_type_id = transactiontype.id and
	trans_location_code_id = 5 and
	trans_type_code = 'ISS'
GROUP BY code, trans_date_id, copy.id LIMIT 10000

-- rules
SELECT
	consequents, copy_title, author_name, medium_type, pr_classmark, shelfmark, bar_code, location,
	antecedent_support, consequent_support, support, confidence, lift, leverage, conviction
FROM public.rule, public.copy
WHERE antecedents = 7698 AND consequents = copy.id


-- clustering (exploring data)
SELECT
	trans_date_id, day_name, day_week, day_month, month, semester, year, trans_type_code,
	trans_type_description, trans_copy_code_id, medium_type, code,
	program, sede, jornada, bajos_rendimientos, bajos_rendimientos, per_cancelados, m_tesis,
	m_activo, m_grado, sexo, birth_date, estrato
FROM
	public.copytransaction, public.transactiontype, public.copy, public.student, public.date
WHERE
trans_date_id = date.id AND
trans_copy_code_id = copy.id AND
trans_borrower_code = student.id AND
trans_type_id = transactiontype.id AND
trans_location_code_id = 5


--SELECT count(id) FROM public.student;
--SELECT count(id) FROM public.copy;
--SELECT count(id) FROM public.title;
--SELECT count(id) FROM public.copytransaction;


-- Clustering
WITH tmp_data AS (SELECT
		code, year, month, day_month, count(trans_copy_code_id) as books
	FROM
		public.copytransaction, public.transactiontype, public.copy, public.student, public.date
	WHERE
	trans_location_code_id = 5 AND
	trans_type_code = 'ISS' AND
	--code = 199713183 AND
	trans_date_id = date.id AND
	trans_copy_code_id = copy.id AND
	trans_borrower_code = student.id AND
	trans_type_id = transactiontype.id

	GROUP BY code, year, month, day_month)

SELECT
code, year, month, count(day_month) as frecuency, sum(books) as total
FROM tmp_data
GROUP BY code, year, month


SELECT
	code, trans_copy_code_id, trans_date_id, trans_type_code
FROM
	public.copytransaction, public.transactiontype, public.copy, public.student, public.date
WHERE
	trans_location_code_id = 5 AND
	code IN (199428135, 199330628) AND
	--trans_copy_code_id = 217052 AND
	--trans_type_code IN ('ISS', 'RET', 'REN') AND
	trans_date_id = date.id AND
	trans_copy_code_id = copy.id AND
	trans_borrower_code = student.id AND
	trans_type_id = transactiontype.id

ORDER BY code, trans_copy_code_id, trans_date_id, trans_type_code



SELECT DISTINCT
iss.code, iss.trans_copy_code_id, iss.trans_date_id as iss_date, ret.trans_date_id as ret_date
FROM (SELECT
	code, trans_copy_code_id, trans_date_id, trans_type_code
FROM
	public.copytransaction, public.transactiontype, public.copy, public.student, public.date
WHERE
	trans_location_code_id = 5 AND
	code IN (199428135, 199330628) AND
	--trans_copy_code_id = 217052 AND
	trans_type_code IN ('ISS') AND
	trans_date_id = date.id AND
	trans_copy_code_id = copy.id AND
	trans_borrower_code = student.id AND
	trans_type_id = transactiontype.id

ORDER BY code, trans_copy_code_id, trans_date_id, trans_type_code) iss,

(SELECT
	code, trans_copy_code_id, trans_date_id, trans_type_code
FROM
	public.copytransaction, public.transactiontype, public.copy, public.student, public.date
WHERE
	trans_location_code_id = 5 AND
	code IN (199428135, 199330628) AND
	--trans_copy_code_id = 217052 AND
	trans_type_code IN ('RET') AND
	trans_date_id = date.id AND
	trans_copy_code_id = copy.id AND
	trans_borrower_code = student.id AND
	trans_type_id = transactiontype.id

ORDER BY code, trans_copy_code_id, trans_date_id, trans_type_code) ret

WHERE
iss.code = ret.code AND
iss.trans_copy_code_id = ret.trans_copy_code_id AND
iss.trans_date_id <= ret.trans_date_id AND
ret.trans_type_code = 'RET'

ORDER BY code, trans_copy_code_id, iss_date

