CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    idade INTEGER DEFAULT 18
);