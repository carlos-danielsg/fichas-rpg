CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,          -- sem contas repetidas
    senha_hash TEXT NOT NULL,           -- só o hash, nunca a senha
    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS campanhas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    sistema TEXT NOT NULL,              -- 'dnd5e', 'daggerheart', 'kob'
    codigo TEXT NOT NULL UNIQUE,        -- texto: não perde zeros e pode misturar letras
    mestre_id INTEGER NOT NULL,
    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (mestre_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS fichas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    pv_atual INTEGER NOT NULL DEFAULT 0 CHECK (pv_atual >= 0),
    pv_max INTEGER NOT NULL DEFAULT 0,
    dados TEXT NOT NULL DEFAULT '{}',   -- JSON (atributos, habilidades) como texto
    dono_id INTEGER NOT NULL,
    campanha_id INTEGER NOT NULL,
    atualizado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dono_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (campanha_id) REFERENCES campanhas(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS rolagens (
    id INTEGER PRIMARY KEY,
    ficha_id INTEGER NOT NULL,
    campanha_id INTEGER NOT NULL,       -- redundante de propósito: facilita o histórico do painel
    expressao TEXT NOT NULL,            -- ex.: '2d6+3'
    resultado TEXT NOT NULL,            -- ex.: '4,2' (os dados individuais)
    total INTEGER NOT NULL,
    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ficha_id) REFERENCES fichas(id) ON DELETE CASCADE,
    FOREIGN KEY (campanha_id) REFERENCES campanhas(id) ON DELETE CASCADE
);