<template>
    <div class="container mt-5">
        <h1 class="text-center">Buscar Registros</h1>
        <div class="d-flex flex-column justify-content-center align-items-center mt-5">
            <div class="card p-4 shadow-lg w-50">
                <form @submit.prevent="buscarOperadora" class="text-center">
                    <input type="text" class="form-control" placeholder="Buscar Registros" v-model="buscaTextual"
                        required />
                    <button class="btn btn-primary mt-2" type="submit">Buscar</button>
                </form>
            </div>

            <div class="spinner-border text-primary mt-5" role="status" v-if="!carregando && buscaTextual.length > 0">
            </div>

            <div v-if="erro" class="alert alert-danger mt-5" role="alert">
                <p class="text-danger">{{ erro }}</p>
            </div>
        </div>
        <div v-if="registros.length > 0 && !erro" class="list-group mt-5">
            <div class="list-group-item">
                <div class="table-responsive">
                    <table class="table table-striped table-bordered">
                        <thead>
                            <tr>
                                <th v-for="(coluna, index) in colunas" :key="index">
                                    {{ coluna }}
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(registro, index) in registros" :key="index">
                                <td>{{ registro.Registro_ANS }}</td>
                                <td>{{ registro.CNPJ }}</td>
                                <td>{{ registro.Razao_Social }}</td>
                                <td>{{ registro.Nome_Fantasia }}</td>
                                <td>{{ registro.Modalidade }}</td>
                                <td>{{ registro.Logradouro }}</td>
                                <td>{{ registro.Número }}</td>
                                <td>{{ registro.Complemento }}</td>
                                <td>{{ registro.Bairro }}</td>
                                <td>{{ registro.Cidade }}</td>
                                <td>{{ registro.UF }}</td>
                                <td>{{ registro.CEP }}</td>
                                <td>{{ registro.DDD }}</td>
                                <td>{{ registro.Telefone }}</td>
                                <td>{{ registro.Fax }}</td>
                                <td>{{ registro.Endereço_Eletronico }}</td>
                                <td>{{ registro.Representante }}</td>
                                <td>{{ registro.Cargo_Representante }}</td>
                                <td>{{ registroRegiao_de_Comercializacao }}</td>
                                <td>{{ registro.Data_Registro_ANS }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div class="logo">
            <img src="../assets/Logo_Matheus_Damacena_preto.png" class="logo" alt="">
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            buscaTextual: "",
            registros: [],
            colunas: [
                "Registro ANS", "CNPJ", "Razão Social", "Nome Fantasia", "Modalidade",
                "Logradouro", "Número", "Complemento", "Bairro", "Cidade", "UF",
                "CEP", "DDD", "Telefone", "Fax", "Endereço Eletrônico",
                "Representante", "Cargo Representante", "Região de Comercialização",
                "Data Registro ANS"
            ],
            carregando: false,
            erro: "",
        };
    },
    methods: {
        async buscarOperadora() {
            try {
                this.carregando = true;

                const response = await axios.get('http://localhost:8000/buscar-registros', {
                    params: {
                        buscaTextual: this.buscaTextual,
                    },
                });
                if (response.status == 200) {
                    this.erro = "";
                    this.registros = response.data;
                }
            } catch (error) {
                this.buscaTextual = "";
                this.carregando = false;

                this.erro = error.response.data.detail;
            } finally {
                this.buscaTextual = "";
                this.carregando = false;
            }
        },
    },
};
</script>

<style>
body {
    background-color: rgb(141, 223, 248);
    font-family: 'Arvo', serif;
}

.container {
  display: flex;
  flex-direction: column;
  min-height: 90vh;
}

.logo {
    text-align: right;
    margin-top: auto;
    margin-right: -40px;
}

.logo img {
    width: 200px;
    height: auto;
}
</style>
