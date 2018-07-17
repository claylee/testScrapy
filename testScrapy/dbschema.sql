drop table piccategory if exists;
create table piccategory(
  cateid integer PRIMARY KEY autoincrease not null,
  pictitle string(100),
  picurl string(300),
  categoryno string(100),
  categoryname string(200),
  categoryurl string(280),
  tags string(200)
);

drop table picdocument if exists;
create table picdocument(
  did integer PRIMARY KEY autoincrease not null,
  pictitle string(100),
  cateid integer,
  docno string(100),
  docname string(200),
  docurl string(280),
  tags string(200)
);


drop table picfile if exists;
create table picfile(
  pid integer PRIMARY KEY autoincrease not null,
  did integer,
  cateid integer,
  fileno integer,
  pictitle string(100),
  picurl string(300),
  md5code string(100),
  tags string(200)
);
