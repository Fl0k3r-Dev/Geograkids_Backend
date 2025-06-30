-- Remover trigger
DROP TRIGGER IF EXISTS update_categorias_updated_at ON categorias;

-- Remover função
DROP FUNCTION IF EXISTS update_updated_at_column();

-- Remover tabela
DROP TABLE IF EXISTS categorias;

-- Remover tipo enum
DROP TYPE IF EXISTS tipo_categoria; 