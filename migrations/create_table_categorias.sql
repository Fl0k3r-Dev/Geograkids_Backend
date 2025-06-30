-- Criar tabela de categorias
CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL UNIQUE,
    descricao TEXT NOT NULL,
    tipo ENUM('LUGAR', 'PAISAGEM', 'TERRITORIO', 'REGIAO') NOT NULL,
    texto TEXT,
    pdf_path VARCHAR(255),
    slides_path VARCHAR(255),
    video_path VARCHAR(255),
    foto_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Índices
    INDEX idx_categorias_titulo (titulo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Adicionar comentários na tabela e colunas (MySQL 8.0+)
ALTER TABLE categorias
    COMMENT = 'Tabela para armazenar categorias geográficas',
    MODIFY COLUMN id INT AUTO_INCREMENT COMMENT 'Identificador único da categoria',
    MODIFY COLUMN titulo VARCHAR(255) NOT NULL COMMENT 'Título da categoria (único)',
    MODIFY COLUMN descricao TEXT NOT NULL COMMENT 'Descrição detalhada da categoria',
    MODIFY COLUMN tipo ENUM('LUGAR', 'PAISAGEM', 'TERRITORIO', 'REGIAO') NOT NULL COMMENT 'Tipo da categoria (LUGAR, PAISAGEM, TERRITORIO, REGIAO)',
    MODIFY COLUMN texto TEXT COMMENT 'Conteúdo em HTML da categoria (opcional)',
    MODIFY COLUMN pdf_path VARCHAR(255) COMMENT 'Caminho do arquivo PDF (opcional)',
    MODIFY COLUMN slides_path VARCHAR(255) COMMENT 'Caminho do arquivo de slides (opcional)',
    MODIFY COLUMN video_path VARCHAR(255) COMMENT 'Caminho do arquivo de vídeo (opcional)',
    MODIFY COLUMN foto_path VARCHAR(255) COMMENT 'Caminho do arquivo de foto (opcional)',
    MODIFY COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Data e hora de criação do registro',
    MODIFY COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Data e hora da última atualização do registro'; 