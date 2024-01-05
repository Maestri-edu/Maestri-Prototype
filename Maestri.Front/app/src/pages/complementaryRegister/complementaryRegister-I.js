import { View, TouchableOpacity, Text } from "react-native";
import { useNavigation } from "@react-navigation/native"

import stylesComponent from "../../design-System/components-styles.js";
import Form from "../../components/form";
import LogoMaestri from "../../components/iconMaestri";
import BackGround from "../../components/backgroud";
import { Component, useEffect, useState } from "react";
import FieldSetDate from "../../components/fields/fieldSetDate/index.js";


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
            placeholder: "informe seu cpf ex: 123.456.678-99",
            setState: setRG,
            showFeedBack: submitButtomIsClicked,
            keyBoardtype: "numeric",
        },
        {
            label: "nome da mãe",
            setState: setNameMon,
            showFeedBack: submitButtomIsClicked,
            placeholder: "nome",
        },
        {
            Component:FieldSetDate,
            label: "data de nascimento",
            setState: setDateNasc,
            showFeedBack: submitButtomIsClicked,
            placeholder: "nome",
        },
    ]

    useEffect(() => {
        setSubmitButtomIsClicked(false);
    }, [, RG, nameMon, dateNasc, stateNasc, cityNasc, maritalStatus])

    const goNextForm = () => {
        setSubmitButtomIsClicked(true);
        //navigation.navigate("")
    }

    return (
        <View style={stylesComponent.container}>
            <BackGround />
            <View style={stylesComponent.contentBox}>
                <LogoMaestri />
                <Form fieldsSets={fieldSets} showFeedBack={submitButtomIsClicked} />
                <TouchableOpacity style={stylesComponent.button} onPress={goNextForm}>
                    <Text style={stylesComponent.buttonText}> Proximo </Text>
                </TouchableOpacity>
            </View>
        </View>
    )
}

export default ComplementaryRegisterI