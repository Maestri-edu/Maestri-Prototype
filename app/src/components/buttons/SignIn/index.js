import { TouchableOpacity, Text } from "react-native";
import stylesComponent from "../../../design-System/components-styles";

const ButtonSignIn = ({ onPress }) => {

  return (
    <TouchableOpacity style={stylesComponent.button} onPress={onPress}>
      <Text style={stylesComponent.buttonText}> Sing In </Text>
    </TouchableOpacity>
  );
};

export default ButtonSignIn;
