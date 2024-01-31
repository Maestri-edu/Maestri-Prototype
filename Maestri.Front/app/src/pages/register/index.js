import React, { useEffect } from "react";
import { useState } from "react";
import { View } from "react-native";
import { useNavigation } from "@react-navigation/native";

import BackGround from "../../components/backgroud";
import Form from "../../components/form";
import ButtonSignUp from "../../components/buttons/SignUp";
import stylesComponent from "../../design-System/components-styles";

import { validateEmail, validatePassword, validatePhone, validateCPF,confirmPassword } from "../../util/validationsFunctions";

const Register = () => {
  const [name, setName] = useState(null);
  const [cpf, setCpf] = useState("000.000.000-00");
  const [password, setPassword] = useState("");
  const [passwordconfirmed,setPasswordconfirmed] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [submitButtomIsClicked, setSubmitButtomIsClicked] = useState(false);
  const navigation = useNavigation();

  const ObjectPassaword = {
    password:password
  }

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
      validationFn: validateCPF
    },
    {
      label: "senha",
      placeholder: "insira sua senha",
      setState: setPassword,
      showFeedBack: submitButtomIsClicked,
      isSecure: true,
      validationFn: validatePassword
    },
    {
      label: "confirme a senha",
      placeholder: "insira sua senha",
      setState: setPasswordconfirmed,
      showFeedBack: submitButtomIsClicked,
      isSecure: true,
      validationFn: confirmPassword(ObjectPassaword)
    },
  ];

  useEffect(() => {
    setSubmitButtomIsClicked(false);
    ObjectPassaword.password = password;
  }, [name, cpf, password, email, phone,passwordconfirmed])

  const submitSignUp = () => {
    setSubmitButtomIsClicked(true);
    //execute fetch to signUp
    navigation.navigate("ComplementaryRegister/personData");
    // if(isValidInputs()){
    // }
  }

  const isValidInputs = () => {
    return validateCPF(cpf).isValid &&
      validateEmail(email).isValid &&
      validatePassword(password).isValid &&
      validatePhone(phone).isValid &&
      confirmPassword(ObjectPassaword)(passwordconfirmed).isValid
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

export default Register;
