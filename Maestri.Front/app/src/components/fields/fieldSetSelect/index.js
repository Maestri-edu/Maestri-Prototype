import React, { useEffect, useState } from 'react';
import { View, Text, FlatList } from 'react-native';
import styles from './styles';

const FieldSetSelect = ({ label, setState, showFeedBack, data, validationFn = () => ({ isValid: true, message: null }) }) => {

    const [isValid, setIsValid] = useState(false);
    const [messageFeedBack, setMessageFeedBack] = useState("");
    const [valueInput, setValueInput] = useState(`informe seu ${label}`);
    const [showDropDown, setShowDropDown] = useState(false);

    useEffect(() => {
        const { isValid, message } = validationFn(valueInput);
        setIsValid(isValid && valueInput.trim() !== "");
        setMessageFeedBack(message || `O campo é obrigatório`);
    }, [showFeedBack]);

    return (
        <View style={styles.fieldSet}>
            <Text style={styles.label}> {label}: </Text>

            <View style={styles.boxArea}>
                <Text style={styles.placeholder} onPress={() => {
                    setShowDropDown(!showDropDown)
                }}> {valueInput} </Text>
            </View>
            {showDropDown &&
                <FlatList
                    style={styles.selectList}
                    data={data}
                    renderItem={({ item }) => <Item title={item.title} onPress={() => {
                        setState(item.title);
                        setValueInput(item.title);
                        setShowDropDown(false);
                    }} />}
                    keyExtractor={item => item.id}
                />
            }


            {showFeedBack && !isValid && (
                <Text style={styles.invalidFeedBack}>
                    {messageFeedBack}
                </Text>
            )}
        </View>
    );
};

const Item = ({ title, onPress }) => {
    return (
        <Text style={styles.itemList} onPress={onPress} >{title}</Text>
    )
};

export default FieldSetSelect;
