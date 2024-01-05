import { View } from "react-native";
import { useEffect, useState } from "react";
import { useNavigation } from "@react-navigation/native";

import LogoMaestri from "../../components/iconMaestri";
import BackGround from "../../components/backgroud/";
import ButtonSignIn from "../../components/buttons/SignIn";
import Form from "../../components/form";
import stylesComponent from "../../design-System/components-styles";
import { validateCPF, validatePassword } from "../../util/validationsFunctions";

const Login = () => {
  const [cpf, setCpf] = useState("");
  const [password, setPassword] = useState("");
  const [submitButtomIsClicked, setSubmitButtomIsClicked] = useState(false);
  const navigation = useNavigation();

  useEffect(() => {
    setSubmitButtomIsClicked(false)
  }, [password, cpf])

  function submitLogin() {
    setSubmitButtomIsClicked(true);
    //execute fetch to API
    navigation.navigate("ComplementaryRegister/personData");
    // if (isValidInputs()) {
    // }
  }

  const isValidInputs = () => {
    return validateCPF(cpf).isValid && validatePassword(password).isValid
  }

  const fieldSets = [
    {
      label: "Cpf",
      placeholder: "informe seu cpf ex: 123.456.678-99",
      setState: setCpf,
      showFeedBack: submitButtomIsClicked,
      keyBoardtype: "numeric",
      validationFn: validateCPF
    },
    {
      label: "Password",
      placeholder: "informe sua senha",
      setState: setPassword,
      showFeedBack: submitButtomIsClicked,
      isSecure: true,
      validationFn: validatePassword
    }
  ]

  return (
    <View style={stylesComponent.container}>
      <BackGround />
      <View style={stylesComponent.contentBox}>
        <LogoMaestri />
        <Form fieldsSets={fieldSets} showFeedBack={submitButtomIsClicked} />
        <ButtonSignIn onPress={submitLogin} />
      </View>
    </View>
  );
};

export default Login;
