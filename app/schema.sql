drop table if exists entries;
create table entries (
  query integer not null,
  intent text not null,
  need text not null,
  summary text not null,
  rating integer not null
);
