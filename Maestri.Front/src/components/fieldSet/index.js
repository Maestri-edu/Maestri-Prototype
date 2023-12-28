import React, { useState } from "react";
import { Text, TextInput, View } from "react-native";
import styles from "./styles";
import colors from "../../../design-System/global-styles";

const FieldSet = ({ label, placeholder, setState, showFeedBack }) => {
  const [isValid, setIsValid] = useState(false);

  function inputChanged(value) {
    setState(value.trim());
  }

  return (
    <View style={styles.filedSet}>
      <Text style={styles.label}> {label}: </Text>
      <TextInput
        style={styles.input}
        placeholderTextColor={colors.mediumGray}
        placeholder={placeholder}
        onChangeText={(value) => {
          setIsValid(value.trim() != "");
          inputChanged(value);
        }}
      />
      {showFeedBack && isValid == false && (
        <Text style={styles.invalidFeedBack}>
          {" "}
          o campo {label} é obrigatórios{" "}
        </Text>
      )}
    </View>
  );
};

export default FieldSet;
