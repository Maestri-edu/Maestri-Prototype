import { Text,View } from "react-native";
import styles from "./styles.js";
import ButtonSignIn from "../../components/buttons/Sign-In/";
import ButtonSignUp from "../../components/buttons/Sign-Up/";
import BackGround from "../../components/backgroud/";
import LogoMaestri from "../../components/iconMaestri"


const Home = () => {
  return (
    <View style={styles.container}>
      <BackGround />
      <View style={styles.contentBox}>
        <LogoMaestri />
        <Text style={styles.title}> Seja bem vindo a Maestri </Text>
        <ButtonSignIn />
        <ButtonSignUp />
      </View>
    </View>
  );
};

export default Home