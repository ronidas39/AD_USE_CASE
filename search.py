import pyad.adquery
q = pyad.adquery.ADQuery()

q.execute_query(
attributes = ["distinguishedName", "description"],
where_clause = "sAMAccountName = 'abc'",
base_dn = "OU=test,DC=totaltechnology,DC=com"
)

print(q.get_row_count())

