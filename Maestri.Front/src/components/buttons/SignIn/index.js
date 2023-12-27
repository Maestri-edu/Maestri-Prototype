import { TouchableOpacity, Text } from "react-native";
import { useNavigation } from "@react-navigation/native";

import styles from "../styles";

const ButtonSignIn = () => {
  const navigation = useNavigation();

  function navigateToSingIn(){
    navigation.navigate("SingIn")
  }

  return (
    <TouchableOpacity style={styles.button} onPress={navigateToSingIn}>
      <Text style={styles.buttonText}> Sing In </Text>
    </TouchableOpacity>
  );
};

export default ButtonSignIn;
