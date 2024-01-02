import React, { useEffect, useState } from "react";
import { Text, TextInput, View } from "react-native";
import styles from "./styles.js";
import colors from "../../design-System/global-styles.js";

const FieldSet = ({ label, placeholder, setState, showFeedBack, keyBoardtype = "default", isSecure = false, validationFn = () => ({isValid:true,message:null}) }) => {
  const [isValid, setIsValid] = useState(false);
  const [messageFeedBack, setMessageFeedBack] = useState("");
  const [valueInput,setValueInput] = useState("");

  function inputChanged(value) {
    setState(value.trim());
    setValueInput(value.trim());
  }

  useEffect(() => {
    const { isValid,message } = validationFn(valueInput);
    setIsValid(isValid && valueInput.trim() != "");
    setMessageFeedBack(message || `o campo ${label} é obrigátorio`);
  }, [showFeedBack])

  return (
    <View style={styles.filedSet}>
      
      <Text style={styles.label}> {label}: </Text>
      <TextInput
        style={styles.input}
        placeholderTextColor={colors.mediumGray}
        placeholder={placeholder}
        onChangeText={inputChanged}
        keyboardType={keyBoardtype}
        secureTextEntry={isSecure}
      />
      {showFeedBack && isValid == false && (
        <Text style={styles.invalidFeedBack}>
          {messageFeedBack}
        </Text>
      )}
    </View>
  );
};

export default FieldSet;
