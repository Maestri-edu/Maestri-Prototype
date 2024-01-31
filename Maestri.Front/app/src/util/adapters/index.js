import safeRegex from "safe-regex";
import { InvalidRegexError } from "../exceptions";
const BrazilStates = {
    AC: "Acre",
    AL: "Alagoas",
    AP: "Amapá",
    AM: "Amazonas",
    BA: "Bahia",
    CE: "Ceará",
    DF: "Distrito Federal",
    ES: "Espírito Santo",
    GO: "Goiás",
    MA: "Maranhão",
    MT: "Mato Grosso",
    MS: "Mato Grosso do Sul",
    MG: "Minas Gerais",
    PA: "Pará",
    PB: "Paraíba",
    PR: "Paraná",
    PE: "Pernambuco",
    PI: "Piauí",
    RJ: "Rio de Janeiro",
    RN: "Rio Grande do Norte",
    RS: "Rio Grande do Sul",
    RO: "Rondônia",
    RR: "Roraima",
    SC: "Santa Catarina",
    SP: "São Paulo",
    SE: "Sergipe",
    TO: "Tocantins",
};

export function isSafeRegex(regex) {
    if (safeRegex(regex)) {
        return true
    }
    throw new InvalidRegexError(regex);
}

export async function sendRequestViaCep(cep) {
    try {
      const data = await fetch(`https://viacep.com.br/ws/${cep}/json/`); // Correção na URL
      const jsonData = await data?.json();
      // requisições do via cep quando dão sucesso "error" não existe na resposta, logo undefined
      // caso existir é por que deu erro
      if(jsonData.error == undefined){
        return {
          statusCode: 200,
          rua: jsonData.logradouro,
          complemento: jsonData.complemento,
          bairro: jsonData.bairro,
          cidade: jsonData.localidade,
          estado: BrazilStates[jsonData.uf],
        };
      }else{
        return {
          statusCode: 400,
        }
      }
    } catch (error) {
      return {
        statusCode: 400,
      };
    }
  }
  