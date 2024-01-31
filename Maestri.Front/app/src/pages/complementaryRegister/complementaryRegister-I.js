import { View, TouchableOpacity, Text } from "react-native";
import { useNavigation } from "@react-navigation/native"

import stylesComponent from "../../design-System/components-styles.js";
import Form from "../../components/form";
import BackGround from "../../components/backgroud";
import { useEffect, useState } from "react";
import FieldSetDate from "../../components/fields/fieldSetDate/index.js";
import FieldSetSelect from "../../components/fields/fieldSetSelect/index.js";
import Title from "../../components/title/index.js";

import { validateRG } from "../../util/validationsFunctions/index.js";
import formComplementionRegisterState from "./formState.js";

const ComplementaryRegisterI = () => {
    const navigation = useNavigation();

    const [RG, setRG] = useState();
    const [nameMon, setNameMon] = useState();
    const [dateNasc, setDateNasc] = useState();
    const [stateNasc, setStateNasc] = useState();
    const [cityNasc, setCityNasc] = useState();
    const [maritalStatus, setMaritalStatus] = useState();
    const [submitButtomIsClicked, setSubmitButtomIsClicked] = useState(false);

    const fieldSets = [
        {
            label: "RG",
            placeholder: "informe seu rg ex:123456789",
            setState: setRG,
            showFeedBack: submitButtomIsClicked,
            keyBoardtype: "numeric",
            validationFn: validateRG
        },
        {
            label: "nome da mãe",
            setState: setNameMon,
            showFeedBack: submitButtomIsClicked,
            placeholder: "nome",
        },
        {
            Component: FieldSetDate,
            label: "data de nascimento",
            setState: setDateNasc,
            showFeedBack: submitButtomIsClicked,
            placeholder: "data de nascimento"
        },
        {
            Component: FieldSetSelect,
            label: "estado de nascimento",
            setState: setStateNasc,
            showFeedBack: submitButtomIsClicked,
            data: [
                { key: 1, label: "AC", value: "Acre" },
                { key: 2, label: "AL", value: "Alagoas" },
                { key: 3, label: "AP", value: "Amapá" },
                { key: 4, label: "AM", value: "Amazonas" },
                { key: 5, label: "BA", value: "Bahia" },
                { key: 6, label: "CE", value: "Ceará" },
                { key: 7, label: "DF", value: "Distrito Federal" },
                { key: 8, label: "ES", value: "Espírito Santo" },
                { key: 9, label: "GO", value: "Goiás" },
                { key: 10, label: "MA", value: "Maranhão" },
                { key: 11, label: "MT", value: "Mato Grosso" },
                { key: 12, label: "MS", value: "Mato Grosso do Sul" },
                { key: 13, label: "MG", value: "Minas Gerais" },
                { key: 14, label: "PA", value: "Pará" },
                { key: 15, label: "PB", value: "Paraíba" },
                { key: 16, label: "PR", value: "Paraná" },
                { key: 17, label: "PE", value: "Pernambuco" },
                { key: 18, label: "PI", value: "Piauí" },
                { key: 19, label: "RJ", value: "Rio de Janeiro" },
                { key: 20, label: "RN", value: "Rio Grande do Norte" },
                { key: 21, label: "RS", value: "Rio Grande do Sul" },
                { key: 22, label: "RO", value: "Rondônia" },
                { key: 23, label: "RR", value: "Roraima" },
                { key: 24, label: "SC", value: "Santa Catarina" },
                { key: 25, label: "SP", value: "São Paulo" },
                { key: 26, label: "SE", value: "Sergipe" },
                { key: 27, label: "TO", value: "Tocantins" }
            ],
            placeholder: "estado de nascimento ex:PR"
        },
        {
            label: "cidade de nascimento",
            setState: setCityNasc,
            showFeedBack: submitButtomIsClicked,
            placeholder: "cidade"
        },
        {
            Component: FieldSetSelect,
            label: "estado civil",
            setState: setMaritalStatus,
            showFeedBack: submitButtomIsClicked,
            data: [
                { key: 1, label: "Solteiro", value: "solteiro" },
                { key: 2, label: "Casado", value: "casado" },
                { key: 3, label: "Divorciado", value: "divorciado" },
                { key: 4, label: "Viúvo", value: "viuvo" },
                { key: 5, label: "Amasiado", value: "amasiado" },
            ],
            placeholder: "estado cívil"
        },
    ]

    useEffect(() => {
        setSubmitButtomIsClicked(false);
    }, [RG, nameMon, dateNasc, stateNasc, cityNasc, maritalStatus])

    const goNextForm = () => {
        setSubmitButtomIsClicked(true);
        if (true) {
            formComplementionRegisterState.addValues({ RG, nameMon, dateNasc, stateNasc, cityNasc, maritalStatus });
            navigation.navigate("ComplementaryRegister/PersonLocation")
        }
    }

    const isValidInputs = () => {
        return validateRG(RG).isValid &&
            isNotEmpty(nameMon) &&
            isNotEmpty(dateNasc) &&
            isNotEmpty(stateNasc) &&
            isNotEmpty(maritalStatus) &&
            isNotEmpty(cityNasc)
    }

    const isNotEmpty = (value) => value != "";

    return (
        <View style={stylesComponent.container}>
            <BackGround />
            <View style={stylesComponent.contentBox}>
                <Title title={"Dados pessoais"}/>
                <Form fieldsSets={fieldSets} showFeedBack={submitButtomIsClicked} />
                <TouchableOpacity style={stylesComponent.button} onPress={goNextForm}>
                    <Text style={stylesComponent.buttonText}> Proximo </Text>
                </TouchableOpacity>
            </View>
        </View>
    )
}

export default ComplementaryRegisterI