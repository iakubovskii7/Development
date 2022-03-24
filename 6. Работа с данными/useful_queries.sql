--Проверить процессы, которые блокируют действия
select pid, pg_blocking_pids(pid) as blocked_by, query as blocked_query
from pg_stat_activity
where pg_blocking_pids(pid)::text != '{}';

