CREATE TABLE test.test_table(
  member_id int ENCODE zstd,
  is_address_invalid int ENCODE zstd
)
DISTKEY(member_id)
SORTKEY(member_id)
;
