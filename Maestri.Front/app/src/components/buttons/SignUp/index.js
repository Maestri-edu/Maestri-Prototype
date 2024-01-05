import { TouchableOpacity, Text } from "react-native";
import stylesComponent from "../../../design-System/components-styles";

const ButtonSignUp = ({ onPress }) => {
  return (
    <TouchableOpacity style={stylesComponent.button} onPress={onPress}>
      <Text style={stylesComponent.buttonText}> Sing Up </Text>
    </TouchableOpacity>
  );
};

export default ButtonSignUp;
