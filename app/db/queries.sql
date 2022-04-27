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