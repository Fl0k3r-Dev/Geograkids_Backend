-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 21/05/2025 às 21:26
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

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
  `link` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cartografia`
--

INSERT INTO `cartografia` (`id`, `titulo`, `descricao`, `link`) VALUES
(3, 'Teste', 'Teste', '<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d118135.81435070686!2d-49.172949552664925!3d-22.287677713298617!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94bf689c0ddaa221%3A0x251c368f6fa134a0!2sBauru%2C%20SP!5e0!3m2!1spt-BR!2sbr!4v1747599016418!5m2!1spt-BR!2sbr\" width=\"600\" height=\"450\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>');

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
(4, 'Teste', 'Teste', 'a arte de enganar - kevin mitnick.pdf', 'uploads/fichasatividades/Teste_a arte de enganar - kevin mitnick.pdf');

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
(4, 'TEstee', 'TEstee', 'a arte de enganar - kevin mitnick.pdf', 'uploads/fichasconteudos/TEstee-a arte de enganar - kevin mitnick.pdf');

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
(10, 'Um gato', 'transferir.jpeg', 'Sei lá', 'uploads/fotos/transferir.jpeg-Um gato');

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
(6, 'Qualquer coisa', 'Qualquer coisa', 'Qualquer coisa', 'a arte de enganar - kevin mitnick.pdf', 'uploads/livros/a arte de enganar - kevin mitnick.pdf');

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
(5, 'A arte de enganar', 'Kevin Mitnik', 'a arte de enganar - kevin mitnick.pdf', 'uploads/livrosvida/A arte de enganar-a arte de enganar - kevin mitnick.pdf');

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
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `status` bit(1) NOT NULL DEFAULT b'1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password`, `status`) VALUES
(1, 'ranci', '202cb962ac59075b964b07152d234b70', b'1');

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
(8, 'Vídeo screen', 'Gravando random', 'Gravando.mp4', 'uploads/videos/Gravando.mp4-Vídeo screen');

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
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `fichas_atividades`
--
ALTER TABLE `fichas_atividades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `fichas_conteudos`
--
ALTER TABLE `fichas_conteudos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `fotos`
--
ALTER TABLE `fotos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `livros`
--
ALTER TABLE `livros`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `livros_vida`
--
ALTER TABLE `livros_vida`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `referencias`
--
ALTER TABLE `referencias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `videos`
--
ALTER TABLE `videos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
