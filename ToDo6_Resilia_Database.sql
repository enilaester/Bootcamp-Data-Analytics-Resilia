CREATE TABLE EmpresaParceira (
	id_empresa SERIAL PRIMARY KEY,
	CNPJ CHAR(18),
	nome_fantasia VARCHAR(100),
	telefone CHAR(14),
	email VARCHAR(100),
	nome_contato VARCHAR(255)
);


CREATE TABLE Tecnologia(
	id_tech SERIAL PRIMARY KEY,
	nome_tech VARCHAR (50),
	nome_area VARCHAR (50)
);

CREATE TABLE Relatório(
	id_registro SERIAL PRIMARY KEY,
	data_registro DATE NOT NULL,
	id_empresa INTEGER,
	id_tech INTEGER,
	CONSTRAINT fk_Empresa_Relatório FOREIGN KEY (id_empresa) REFERENCES EmpresaParceira (id_empresa),
	CONSTRAINT fk_Tecnologia_Relatório FOREIGN KEY (id_tech) REFERENCES Tecnologia (id_tech)
);


INSERT INTO EmpresaParceira (CNPJ,nome_fantasia,telefone,email,nome_contato) VALUES
		('11.111.111/1111-11','Code Together','(11)11111-1111','mariafernanda@codetogether','Maria Fernanda'),
		('22.222.222/2222-22','Consultoria FX','(21)22222-2222','robertoleal@fx','Roberto Leal'),
        ('33.333.333/3333-33','Pet Love','(31)33333-3333','livia@petlove','Lívia Lima'),
        ('44.444.444/4444-44','Stone Pagamentos','(31)44444-4444','pietrobraga@stone','Pietro Braga');
		
INSERT INTO TECNOLOGIA (nome_tech,nome_area) VALUES
		('Google Ads', 'Marketing'),
		('SEO', 'Marketing'),
		('Google Analytics', 'Marketing'),
		('JavaScript', 'WebDev'),
		('Node.js','WebDev'),
		('PHP','WebDev'),
		('CSS','WebDev'),
		('HTML','WebDev'),
		('Django','WebDev'),
		('C++','WebDev'),
		('Ruby','WebDev'),
		('Julia','WebDev'),
		('Python','Dados'),
		('PostgreSQL', 'Dados'),
		('MySQL', 'Dados'),
		('SQL Server','Dados'),
		('R', 'Dados'),
		('NoSQL','Dados'),
		('Google Colaboratory', 'Dados'),
		('Google BigQuery','Dados'),
		('Power BI','Dados'),
		('Tableau','Dados'),
		('Flourish','Dados'),
		('Figma','Design'),
		('Adobe Illustrator','Design'),
		('Adobe Photoshop','Design'),
		('Adobe XD', 'Design'),
		('DaVinci', 'Design'),
		('Microsoft Azure', 'Dados'),
		('Amazon Web Services', 'Dados');
		
INSERT INTO Relatório (data_registro,id_empresa,id_tech) VALUES
		('2021-06-01','1','3'),
		('2021-06-01','1','15'),
		('2021-06-01','1','19'),
		('2021-06-01','1','22'),
		('2021-06-01','1','10'),
		('2021-06-01','2','2'),
		('2021-06-01','2','11'),
		('2021-06-01','2','15'),
		('2021-06-01','2','17'),
		('2021-06-01','2','26'),
		('2021-06-01','3','1'),
		('2021-06-01','3','4'),
		('2021-06-01','3','13'),
		('2021-06-01','3','18'),
		('2021-06-01','3','25'),
		('2021-06-01','4','3'),
		('2021-06-01','4','5'),
		('2021-06-01','4','6'),
		('2021-06-01','4','15'),
		('2021-06-01','4','24'),
		('2022-01-05','1','3'),
		('2022-01-05','1','15'),
		('2022-01-05','1','19'),
		('2022-01-05','1','22'),
		('2022-01-05','1','10'),
		('2022-01-05','1','13'),
		('2022-01-05','1','4'),
		('2022-01-05','1','5'),
		('2022-01-05','1','6'),
		('2022-01-05','1','7'),
		('2022-01-05','1','8'),
		('2022-01-05','2','2'),
		('2022-01-05','2','11'),
		('2022-01-05','2','15'),
		('2022-01-05','2','17'),
		('2022-01-05','2','26'),
		('2022-01-05','2','3'),
		('2022-01-05','2','13'),
		('2022-01-05','2','21'),
		('2022-01-05','2','25'),
		('2022-01-05','2','30'),
		('2022-01-05','3','1'),
		('2022-01-05','3','4'),
		('2022-01-05','3','13'),
		('2022-01-05','3','18'),
		('2022-01-05','3','25'),
		('2022-01-05','3','2'),
		('2022-01-05','3','3'),
		('2022-01-05','3','5'),
		('2022-01-05','3','14'),
		('2022-01-05','3','21'),
		('2022-01-05','3','26'),
		('2022-01-05','3','28'),
		('2022-01-05','3','30'),
		('2022-01-05','4','3'),
		('2022-01-05','4','5'),
		('2022-01-05','4','6'),
		('2022-01-05','4','15'),
		('2022-01-05','4','24'),
		('2022-01-05','4','1'),
		('2022-01-05','4','2'),
		('2022-01-05','4','4'),
		('2022-01-05','4','9'),
		('2022-01-05','4','13'),
		('2022-01-05','4','21'),
		('2022-01-05','4','18'),
		('2022-01-05','4','30');

_______________________________________________________________________________________________________________________________________________________________________________________________

QUERIES

/* 1. Qual empresa utiliza o maior número de tecnologias na última pesquisa (1/2022)?  */

select empresaparceira.nome_fantasia as "Empresa", count(id_tech) as "Quantidade de Tecnologias - 1º semestre 2022" from relatório
inner join empresaparceira on relatório.id_empresa = empresaparceira.id_empresa
where relatório.data_registro = '20220105' 
group by empresaparceira.nome_fantasia
order by count (id_tech) desc;


/* 2. Qual empresa utilizava o menor número de tecnologias na pesquisa anterior (2/2021)? */

select empresaparceira.nome_fantasia as "Empresa", count(id_tech) as "Quantidade de Tecnologias - 2º semestre 2021" from relatório
inner join empresaparceira on relatório.id_empresa = empresaparceira.id_empresa
where relatório.data_registro = '20210601' 
group by empresaparceira.nome_fantasia
order by count (id_tech);

/* 3. Quantas empresas utilizam tecnologias da área de “Dados” atualmente? */

select count(distinct id_empresa)as "Quantidade de empresas", tecnologia.nome_area as "Área" from relatório
inner join tecnologia on relatório.id_tech = tecnologia.id_tech
where relatório.data_registro = '20220105' 
group by tecnologia.nome_area
having tecnologia.nome_area = 'Dados';


/* 4. Quantas empresas utilizam tecnologias que não são da área de “Dados” atualmente? */

select count(distinct id_empresa)as "Quantidade de empresas", tecnologia.nome_area as "Área" from relatório
inner join tecnologia on relatório.id_tech = tecnologia.id_tech
where relatório.data_registro = '20220105' 
group by tecnologia.nome_area
having tecnologia.nome_area <> 'Dados';

_______________________________________________________________________________________________________________________________________________________________________________________________________________________
