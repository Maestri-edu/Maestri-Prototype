import React, { useEffect } from "react";
import { useState } from "react";
import { View } from "react-native";

import BackGround from "../../components/backgroud";
import Form from "../../components/form";
import ButtonSignUp from "../../components/buttons/SignUp";
import stylesComponent from "../../design-System/components-styles";

import { validateEmail, validatePassword, validatePhone,validateCPF } from "../../util/validationsFunctions/";

const SignUp = () => {
  const [name, setName] = useState(null);
  const [cpf, setCpf] = useState(null);
  const [password, setPassword] = useState(null);
  const [email, setEmail] = useState(null);
  const [phone, setPhone] = useState(null);
  const [submitButtomIsClicked, setSubmitButtomIsClicked] = useState(false);

  const fieldSets = [
    {
      label: "nome",
      placeholder: "informe seu nome",
      setState: setName,
      showFeedBack: submitButtomIsClicked,
    },
    {
      label: "email",
      placeholder: "informe seu email ex: example@gmail.com",
      setState: setEmail,
      showFeedBack: submitButtomIsClicked,
      keyBoardtype: "email-address",
      validationFn: validateEmail
    },
    {
      label: "telefone",
      placeholder: "informe seu telefone ex: 0000-0000",
      setState: setPhone,
      showFeedBack: submitButtomIsClicked,
      keyBoardtype: "numeric",
      validationFn: validatePhone
    },
    {
      label: "Cpf",
      placeholder: "informe seu cpf ex: 123.456.678-99",
      setState: setCpf,
      showFeedBack: submitButtomIsClicked,
      keyBoardtype: "numeric",
      validationFn:validateCPF
    },
    {
      label: "senha",
      placeholder: "insira sua senha",
      setState: setPassword,
      showFeedBack: submitButtomIsClicked,
      isSecure: true,
      validationFn: validatePassword
    },
  ];

  useEffect(() => {
    setSubmitButtomIsClicked(false);
  }, [name, cpf, password, email, phone])

  const submitSignUp = () => {
    setSubmitButtomIsClicked(true);
    //execute fetch to signUp
  }


  return (
    <View style={stylesComponent.container}>
      <BackGround />
      <View style={stylesComponent.contentBox}>
        <Form fieldsSets={fieldSets} showFeedBack={submitButtomIsClicked} />
        <ButtonSignUp onPress={submitSignUp} />
      </View>
    </View>
  );
};

export default SignUp;
