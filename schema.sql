DROP TABLE IF EXISTS history;

CREATE TABLE history (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	query TEXT NOT NULL,
	answer TEXT NOT NULL
);