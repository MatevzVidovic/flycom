id	created_at	updated_at	created_by	updated_by	gid	geom	__mod	id_posla	model_posla	trzni_segment	sestava	pog_cena	ef_cena	vrsta_posla_etn	vrsta_posla	status_pregleda	modeli	podr_raba_dst	tip_stavbe	poseb_zgs	upor_povr	neto_povr	gost_vrt_v_ceni	vrsta_nasada	id_elektrika	leto_obn_strehe	leto_obn_fasade	leto_obn_oken	leto_obn_inst	id_dvigalo	id_vodovod	id_kanalizacija	id_plin	rk	odprtost	pov_nakl_parc	boniteta	model_podposla	dej_raba_dst	leto_izg	zps_dst	id_lega	nadstropje	kakovost_dst	st_stanovanj	st_etaz	grad_faza	id_konstrukcije	neto_prost	visina_etaze_rzd	kakovost_mikrolok	id_podposla	atr_povr	gl_podposel	id_rel_podposla	valid_from	valid_to	geom_posla	dat_pri	ddv_stopnja	podmodel_stz	ko_stst_stdst	zemlj_povr	zemlj_vv_povr	delez_vrednosti	primerno_zgs	datum_prve_uveljavitve_posla	vir_podatka	vrednost	izmera


Plan:

- to DF
- drop all cols except  dat_pri as dp and datum_prve_uveljavitve_posla as dpus
- Group by dp, select (dp, count(dp == dpus) as on_time, count(dp < dpus) as later, count(dp > dpus) as earlier)
- order by dp
- assert  earlier == 0
- create col coef, is (later / (on_time / later))

- take last year, put into its own csv, remove from main csv
- on main csv, select AVG(coef), multiply with dp of the last year csv


Questions:

- do I just take the year of deals, or do I go for (28.2.year - 28.2.(year+1))