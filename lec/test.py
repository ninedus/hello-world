a = """
insert into tad_job_pool_log
(
    select evnt_dt, crane_no, pool_name, vvd, queue, avg_tt, min_tt, max_tt, combine_yn, ldb_deck, ldb_hold
    from tad_job_pool
    where 1=1
    and mod(ref_seq,60) = 10
)
;
"""

s = a.upper()
print(s)