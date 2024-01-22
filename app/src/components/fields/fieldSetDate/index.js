import { useEffect, useState } from "react"
import { View, Text } from "react-native"
import DateTimePicker from '@react-native-community/datetimepicker';
import styles from "./styles";

const FieldSetDate = ({ label,placeholder, setState, showFeedBack, validationFn = () => ({ isValid: true, message: null }) }) => {
  const [valueInput, setValueInput] = useState(null);
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [messageFeedBack, setMessageFeedBack] = useState("");
  const [isValid, setIsValid] = useState(false);

  useEffect(() => {
    const { isValid, message } = validationFn(valueInput);
    setIsValid(isValid && valueInput != null);
    setMessageFeedBack(message || `o campo é obrigátorio`);
  }, [showFeedBack])

  const onChange = (_, selectedDate) => {
    const currentDate = selectedDate || valueInput;
    setShowDatePicker(false);
    setValueInput(currentDate);
    setState(currentDate);
  };

  const getDateTime = () => valueInput != null ? new Date(valueInput).toLocaleDateString() : "";

  return (
    <View style={styles.fieldSet}>
      <Text style={styles.label}> {label} </Text>
      <View style={styles.boxArea}>
        <Text style={styles.placeholder} onPress={() => {
          setShowDatePicker(true)
        }}> {getDateTime() || placeholder } </Text>
      </View>

      {showDatePicker && (
        <DateTimePicker
          testID="dateTimePicker"
          value={valueInput || new Date()}
          mode="date"
          is24Hour={true}
          display="default"
          onChange={onChange}
        />
      )}
      {showFeedBack && isValid == false && (
        <Text style={styles.invalidFeedBack}>
          {messageFeedBack}
        </Text>
      )}
    </View>
  );
}

export default FieldSetDate