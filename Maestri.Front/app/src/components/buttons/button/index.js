import { TouchableOpacity, Text } from "react-native";
import stylesComponent from "../../../design-System/components-styles";
import { Children } from "react";

// const ButtonChad = ({ onPress, text }) => {
export default function ButtonChad (onPress){
    return (
    <TouchableOpacity style={stylesComponent.button} onPress={onPress} >
      <Text style={stylesComponent.buttonText}>{Children}</Text>
    </TouchableOpacity>
  );
};