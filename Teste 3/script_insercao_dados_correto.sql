-- Inserção do CSV Realatorio Cadop --

COPY operadoras_ativas FROM 'C:\Teste_Intuitive_Care\Teste 3\Relatorio_cadop.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

SELECT * FROM operadoras_ativas

-- Criação de uma tabela temporária para receber os arquivos trimestrais --

CREATE TEMP TABLE tabela_temporaria (
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil VARCHAR(10),
    descricao TEXT,
    vl_saldo_inicial TEXT,
    vl_saldo_final TEXT
);

drop table tabela_temporaria

SELECT * FROM tabela_temporaria

-- Criação de uma função para inserção dos dados na tabela final --

CREATE OR REPLACE FUNCTION inserir_na_tabela_final()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO registros_trimestrais (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
    VALUES (
        NEW.data,
        NEW.reg_ans,
        NEW.cd_conta_contabil,
        NEW.descricao,
        REPLACE(NEW.vl_saldo_inicial, ',', '.')::NUMERIC,
        REPLACE(NEW.vl_saldo_final, ',', '.')::NUMERIC
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criação de um Gatilho para sempre inserir os dados após a inserção na tabela temporaria -- 

CREATE OR REPLACE TRIGGER trigger_inserir_tabela_final
AFTER INSERT ON tabela_temporaria
FOR EACH ROW
EXECUTE FUNCTION inserir_na_tabela_final();

-- Inserção do CSV 1T2023 --

COPY tabela_temporaria FROM 'C:\Teste_Intuitive_Care\Teste 3\2023\1T2023\1T2023.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

-- Inserção do CSV 2T2023 --

COPY tabela_temporaria FROM 'C:\Teste_Intuitive_Care\Teste 3\2023\2T2023\2t2023.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

-- Inserção do CSV 3T2023 --

COPY tabela_temporaria FROM 'C:\Teste_Intuitive_Care\Teste 3\2023\3T2023\3T2023.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

-- Inserção do CSV 4T2023 --

COPY tabela_temporaria FROM 'C:\Teste_Intuitive_Care\Teste 3\2023\4T2023\4T2023.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

-- Inserção do CSV 1T2024 --

COPY tabela_temporaria FROM 'C:\Teste_Intuitive_Care\Teste 3\2024\1T2024\1T2024.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

-- Inserção do CSV 2T2024 --

COPY tabela_temporaria FROM 'C:\Teste_Intuitive_Care\Teste 3\2024\2T2024\2T2024.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

-- Inserção do CSV 3T2024 --

COPY tabela_temporaria FROM 'C:\Teste_Intuitive_Care\Teste 3\2024\3T2024\3T2024.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

-- Inserção do CSV 4T2024 --

COPY tabela_temporaria FROM 'C:\Teste_Intuitive_Care\Teste 3\2024\4T2024\4T2024.csv' 
DELIMITER ';' 
CSV HEADER
ENCODING 'UTF8';

SELECT * FROM registros_trimestrais