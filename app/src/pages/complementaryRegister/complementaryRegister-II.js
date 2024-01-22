import { View, TouchableOpacity, Text, NativeEventEmitter } from "react-native";
import { useNavigation } from "@react-navigation/native"

import stylesComponent from "../../design-System/components-styles.js";
import Form from "../../components/form";
import BackGround from "../../components/backgroud";
import { useEffect, useState } from "react";
import Title from "../../components/title/index.js";

import formComplementionRegisterState from "./formState.js";
import { sendRequestViaCep } from "../../util/adapters";

const eventEmitter = new NativeEventEmitter();

const ComplementaryRegisterII = () => {
    const navigation = useNavigation();

    const [cep, setCep] = useState();
    const [street, setStreet] = useState();
    const [number, setNumber] = useState();
    const [neighborhood, setNeighborhood] = useState();
    const [state, setState] = useState();
    const [city, setCity] = useState();
    const [complement, setComplement] = useState();
    const [submitButtomIsClicked, setSubmitButtomIsClicked] = useState(false);

    useEffect(() => {
        setSubmitButtomIsClicked(false);
    }, [cep, street, number, neighborhood, state, city, complement]);

    useEffect(() => {
        const timeoutId = setTimeout(requestToViaCep, 1000);
        return () => clearTimeout(timeoutId);
    }, [cep])

    const fieldSets = [
        {
            label: "CEP",
            placeholder: "informe seu cep: 87654321",
            setState: setCep,
            showFeedBack: submitButtomIsClicked,
            keyBoardtype: "numeric",
        },
        {
            label: "numero",
            placeholder: "informe seu numero",
            setState: setNumber,
            showFeedBack: submitButtomIsClicked,
            keyBoardtype: "numeric",
        },
        {
            label: "bairro",
            placeholder: "informe seu bairro",
            setState: setNeighborhood,
            showFeedBack: submitButtomIsClicked,
            onEvent: true
        },
        {
            label: "rua",
            placeholder: "informe sua rua",
            setState: setStreet,
            showFeedBack: submitButtomIsClicked,
            onEvent: true
        },
        {
            label: "estado",
            placeholder: "informe seu estado atual",
            setState: setState,
            showFeedBack: submitButtomIsClicked,
            onEvent: true
        },
        {
            label: "cidade",
            placeholder: "informe sua cidade atual",
            setState: setCity,
            showFeedBack: submitButtomIsClicked,
            onEvent: true
        },
        {
            label: "complemento",
            placeholder: "complemento",
            setState: setComplement,
            showFeedBack: submitButtomIsClicked,
            onEvent: true
        },
    ]

    const goNextForm = () => {
        setSubmitButtomIsClicked(true);
        if (isValidInputs()) {
            formComplementionRegisterState.addValues({ cep, street, number, neighborhood, state, city, complement });
        }
    }

    const isValidInputs = () => {
        return isNotEmpty(cep) &&
            isNotEmpty(street) &&
            isNotEmpty(number) &&
            isNotEmpty(neighborhood) &&
            isNotEmpty(state) &&
            isNotEmpty(city) &&
            isNotEmpty(complement)
    }

    const requestToViaCep = async () => {
        const { statusCode, ...address } = await sendRequestViaCep(cep);
        if (statusCode == 200) {
            for (const { label } of fieldSets) {
                if (!["CEP", "numero"].includes(label)) {
                    eventEmitter.emit(label, address[label]);
                    setSubmitButtomIsClicked(false)
                }
            }
        }
    }

    const isNotEmpty = (value) => value != "";

    return (
        <View style={stylesComponent.container}>
            <BackGround />
            <View style={stylesComponent.contentBox}>
                <Title title={"Dados de residencia"} />
                <Form fieldsSets={fieldSets} showFeedBack={submitButtomIsClicked} />
                <TouchableOpacity style={stylesComponent.button} onPress={goNextForm}>
                    <Text style={stylesComponent.buttonText}> Proximo </Text>
                </TouchableOpacity>
            </View>
        </View>
    )
}

export default ComplementaryRegisterII