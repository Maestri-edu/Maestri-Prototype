import { Text, View, TouchableOpacity } from "react-native";
import { useNavigation } from "@react-navigation/native";
import BackGround from "../../components/backgroud/";
import LogoMaestri from "../../components/iconMaestri/";
import stylesComponent from "../../design-System/components-styles.js";
import Title from "../../components/title/index.js";

const Home = () => {
  const navigation = useNavigation();
  const toSignIn = () => {
    navigation.navigate("SignIn");
  };
  const toSignUp = () => {
    navigation.navigate("SignUp");
  };

  return (
    <View style={stylesComponent.container}>
      <BackGround />
      <View style={stylesComponent.contentBox}>
        <LogoMaestri />
        <Title title={"Seja bem vindo a Maestri"}/>
        <TouchableOpacity style={stylesComponent.button} onPress={toSignIn}>
          <Text style={stylesComponent.buttonText}> Sing In </Text>
        </TouchableOpacity>

        <TouchableOpacity style={stylesComponent.button} onPress={toSignUp}>
          <Text style={stylesComponent.buttonText}> Sing Up </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default Home;
