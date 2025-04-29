-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 27/04/2025 às 15:12
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `mestrado`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cartografia`
--

CREATE TABLE `cartografia` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `descricao` text DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cartografia`
--

INSERT INTO `cartografia` (`id`, `titulo`, `descricao`, `link`) VALUES
(1, 'Mapa Interativo do Brasil', 'Mapa político e físico do Brasil.', 'https://cartografia.exemplo.com/mapa-brasilllllll');

-- --------------------------------------------------------

--
-- Estrutura para tabela `fichas_atividades`
--

CREATE TABLE `fichas_atividades` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `descricao` text DEFAULT NULL,
  `pdf` varchar(255) DEFAULT NULL,
  `caminhoPdf` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `fichas_atividades`
--

INSERT INTO `fichas_atividades` (`id`, `titulo`, `descricao`, `pdf`, `caminhoPdf`) VALUES
(1, 'Atividade de Ciências', 'Ficha com exercícios sobre ecossistemas.', 'atividade_cienciasaaa.pdf', ''),
(3, 'Eitaaa', 'AAAA', 'lista substituicoes bruna (1).pdf', 'uploads/fichasatividades/lista substituicoes bruna (1).pdf-Eitaaa');

-- --------------------------------------------------------

--
-- Estrutura para tabela `fichas_conteudos`
--

CREATE TABLE `fichas_conteudos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `descricao` text DEFAULT NULL,
  `pdf` varchar(255) DEFAULT NULL,
  `caminhoPdf` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `fichas_conteudos`
--

INSERT INTO `fichas_conteudos` (`id`, `titulo`, `descricao`, `pdf`, `caminhoPdf`) VALUES
(1, 'Conteúdo de Geografia', 'Resumo sobre bacias hidrográficas.', 'geografia_conteudo22.pdf', ''),
(3, 'dfgfh', 'sdfg', 'Como_Sair_do_SPC_Serasa_em_30_Dias.pdf', 'uploads/fichasconteudos/Como_Sair_do_SPC_Serasa_em_30_Dias.pdf-dfgfh');

-- --------------------------------------------------------

--
-- Estrutura para tabela `fotos`
--

CREATE TABLE `fotos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `imagem` varchar(255) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `caminhoImagem` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `fotos`
--

INSERT INTO `fotos` (`id`, `titulo`, `imagem`, `descricao`, `caminhoImagem`) VALUES
(1, 'Eeeeettttaaa', 'Aeeeee', 'EEEEE', ''),
(8, 'TEsteeeasdasd12312312', 'asfassa', 'AGDS', ''),
(9, 'dsfg', 'download.jpeg', 'sdgfd', 'uploads/fotos/download.jpeg');

-- --------------------------------------------------------

--
-- Estrutura para tabela `livros`
--

CREATE TABLE `livros` (
  `Id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `autor` varchar(255) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `pdf` varchar(255) NOT NULL,
  `caminhoPdf` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `livros`
--

INSERT INTO `livros` (`Id`, `titulo`, `autor`, `descricao`, `pdf`, `caminhoPdf`) VALUES
(1, 'Um livro aí', 'Teste ', 'Descrevendo um livro', 'sei lá', ''),
(5, 'stringEEE|E', 'Gustavo', 'asd', 'Como_Sair_do_SPC_Serasa_em_30_Dias.pdf', 'uploads/livros/Como_Sair_do_SPC_Serasa_em_30_Dias.pdf');

-- --------------------------------------------------------

--
-- Estrutura para tabela `livros_vida`
--

CREATE TABLE `livros_vida` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `descricao` text DEFAULT NULL,
  `pdf` varchar(255) DEFAULT NULL,
  `caminhoPdf` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `livros_vida`
--

INSERT INTO `livros_vida` (`id`, `titulo`, `descricao`, `pdf`, `caminhoPdf`) VALUES
(1, 'A Vida em Movimento', 'Livro sobre desenvolvimento pessoal.', 'vida_movimento02.pdf', '');

-- --------------------------------------------------------

--
-- Estrutura para tabela `referencias`
--

CREATE TABLE `referencias` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `autor` varchar(255) DEFAULT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  `referencia` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `referencias`
--

INSERT INTO `referencias` (`id`, `titulo`, `autor`, `descricao`, `referencia`, `link`) VALUES
(2, 'vish', 'embacou', 'fooii', 'boaaa', 'aaaeeee'),
(4, 'testando insercao', 'testando insercao', 'testando insercao', 'testando insercao', 'testando insercao'),
(5, 'Embaçado', '', '', '', '');

-- --------------------------------------------------------

--
-- Estrutura para tabela `videos`
--

CREATE TABLE `videos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `descricao` text DEFAULT NULL,
  `video` varchar(255) DEFAULT NULL,
  `caminhoVideo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `videos`
--

INSERT INTO `videos` (`id`, `titulo`, `descricao`, `video`, `caminhoVideo`) VALUES
(2, 'Teste', 'Teste', 'Teste.mp4', '');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cartografia`
--
ALTER TABLE `cartografia`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `fichas_atividades`
--
ALTER TABLE `fichas_atividades`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `fichas_conteudos`
--
ALTER TABLE `fichas_conteudos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `fotos`
--
ALTER TABLE `fotos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `livros`
--
ALTER TABLE `livros`
  ADD PRIMARY KEY (`Id`);

--
-- Índices de tabela `livros_vida`
--
ALTER TABLE `livros_vida`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `referencias`
--
ALTER TABLE `referencias`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `videos`
--
ALTER TABLE `videos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cartografia`
--
ALTER TABLE `cartografia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `fichas_atividades`
--
ALTER TABLE `fichas_atividades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `fichas_conteudos`
--
ALTER TABLE `fichas_conteudos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `fotos`
--
ALTER TABLE `fotos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `livros`
--
ALTER TABLE `livros`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `livros_vida`
--
ALTER TABLE `livros_vida`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `referencias`
--
ALTER TABLE `referencias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `videos`
--
ALTER TABLE `videos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
