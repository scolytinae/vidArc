drop table if exists films;

create table films(
  id integer primary key autoincrement,
  title text not null,
  story text,
  director text,
  filename text not null,
  torrent_file text not null,
  page_name text not null
);



