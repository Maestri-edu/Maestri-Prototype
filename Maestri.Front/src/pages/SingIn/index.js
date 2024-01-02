import { View } from "react-native";
import { useEffect, useState } from "react";

import LogoMaestri from "../../components/iconMaestri";
import BackGround from "../../components/backgroud/";
import ButtonSignIn from "../../components/buttons/SignIn";
import Form from "../../components/form";
import stylesComponent from "../../design-System/components-styles";

const Login = () => {
  const [cpf, setCpf] = useState(null);
  const [password, setPassword] = useState(null);
  const [submitButtomIsClicked, setSubmitButtomIsClicked] = useState(false);

  useEffect(() => {
    setSubmitButtomIsClicked(false)
  }, [password, cpf])

  function submitLogin() {
    setSubmitButtomIsClicked(true);
    //execute fetch to API

  }

  const fieldSets = [
    {
      label: "Cpf",
      placeholder: "inform your cpf ex: 123.456.678-99",
      setState: setCpf,
      showFeedBack: submitButtomIsClicked,
      keyBoardtype: "numeric",
      isSecure: false
    },
    {
      label: "Password",
      placeholder: "infrom your password",
      setState: setPassword,
      showFeedBack: submitButtomIsClicked,
      isSecure: true
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
