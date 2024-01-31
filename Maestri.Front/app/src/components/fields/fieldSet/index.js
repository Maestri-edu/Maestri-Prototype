import React, { useEffect, useState } from "react";
import { Text, TextInput, View } from "react-native";
import styles from "./styles.js";
import colors from "../../../design-System/global-styles.js";
import { NativeEventEmitter } from "react-native";



const FieldSet = ({ label, placeholder, setState, showFeedBack, keyBoardtype = "default", isSecure = false,onEvent = false, validationFn = () => ({isValid:true,message:null}) }) => {
  const [isValid, setIsValid] = useState(false);
  const [messageFeedBack, setMessageFeedBack] = useState("");
  const [valueInput,setValueInput] = useState("");
  const [isEditable,setIsEditable] = useState(true);

  useEffect(() => {
    if (onEvent) {
      setIsEditable(false);
      const eventEmitter = new NativeEventEmitter();
      const listener = (value) => {
        setState(value);
        setValueInput(value);
        eventEmitter.removeAllListeners(label);
        setIsEditable(true);
      };

      eventEmitter.addListener(label, listener);

      return () => {
        eventEmitter.removeAllListeners(label);
      };
    }
  }, []);

  
  useEffect(() => {
    const { isValid,message } = validationFn(valueInput);
    setIsValid(isValid && valueInput?.trim() != "");
    setMessageFeedBack(message || `o campo é obrigátorio`);
  }, [showFeedBack])
  
  function inputChanged(value) {
    setState(value?.trim());
    setValueInput(value?.trim());
  }

  return (
    <View style={styles.fieldSet}>
      
      <Text style={{ ...styles.label, opacity: isEditable ? 1 : 0.4 }}> {label}: </Text>
      <TextInput
        style={isEditable?styles.inputEditable:styles.inputNotEditable}
        placeholderTextColor={colors.mediumGray}
        placeholder={placeholder}
        onChangeText={inputChanged}
        keyboardType={keyBoardtype}
        secureTextEntry={isSecure}
        value={valueInput}
        editable={isEditable}
        
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
