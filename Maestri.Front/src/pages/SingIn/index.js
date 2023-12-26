import { TouchableOpacity, View,Text } from "react-native";
import BackGround from "../../components/backgroud/";
import LogoMaestri from "../../components/iconMaestri";
import styles from "./styles";
import FieldSet from "../../components/fieldSet";
import { useState } from "react";

const Login = () => {

    const [cpf,setCpf] = useState(null)
    const [password,setPassword] = useState(null);
    const [submitButtomIsClicked,setSubmitButtomIsClicked] = useState(false);

    function Login(){
        setSubmitButtomIsClicked(true);
    }

    return (
    <View style={styles.container}>
      <BackGround />
      <View style={styles.contentBox}>
        <LogoMaestri />

        <FieldSet
          label={"CPF"}
          placeholder={"informe seu cpf ex: 123.456.678-99"}
          showFeedBack={submitButtomIsClicked}
          setState={setCpf}
        />

        <FieldSet
          label={"Password"}
          placeholder={"informe sua senha "}
          showFeedBack={submitButtomIsClicked}
          setState={setPassword}
        />

        <TouchableOpacity style={styles.button} onPress={Login}>
            <Text style={styles.buttonText}> Login </Text>
        </TouchableOpacity>
        
      </View>
    </View>
  );
};

export default Login;
