import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, TextInput, TouchableOpacity, Keyboard } from 'react-native';
import styles from './styles';
import colors from '../../../design-System/global-styles';

const FieldSetSelect = ({ label, placeholder, setState, showFeedBack, data, validationFn = () => ({ isValid: true, message: null }) }) => {
    const [isValid, setIsValid] = useState(false);
    const [messageFeedBack, setMessageFeedBack] = useState("");
    const [valueInput, setValueInput] = useState("");
    const [showDropDown, setShowDropDown] = useState(false);
    const MAX_ITEMS_RENDERING = 6;
    let itemsCount = 0;

    useEffect(() => {
        const { isValid, message } = validationFn(valueInput);
        setIsValid(isValid && valueInput.trim() !== "");
        setMessageFeedBack(message || "O campo é obrigatório");
    }, [showFeedBack]);

    const filterPerNameState = (item) => item.label.toUpperCase().includes(valueInput.toUpperCase()) || item.value.toUpperCase().includes(valueInput.toUpperCase());

    const renderItems = ({ item }) => {
        if (filterPerNameState(item) && itemsCount < MAX_ITEMS_RENDERING) {
            itemsCount++;
            return renderStateItem(item);
        } else if (itemsCount === MAX_ITEMS_RENDERING) {
            itemsCount++;
            return renderLastItem();
        }
    };

    const renderStateItem = ({ label, value,key }) => (
        <Item key={key} title={label} onPress={() => handleItemPress(value)} />
    );

    const renderLastItem = () => <Item key={"last"} title={"....."} onPress={() => {}} />;

    const handleItemPress = (value) => {
        setState(value);
        setValueInput(value);
        setShowDropDown(false);
        Keyboard.dismiss();
    };

    return (
        <View style={styles.fieldSet}>
            <Text style={styles.label}>{label}:</Text>
            <TextInput
                onFocus={() => setShowDropDown(true)}
                onChangeText={(value) => setValueInput(value)}
                style={styles.input}
                value={valueInput}
                placeholder={placeholder}
                keyboardType="default"
                placeholderTextColor={colors.mediumGray}
            />

            {showDropDown && (
                <FlatList
                    style={styles.selectList}
                    data={data}
                    renderItem={renderItems}
                    keyExtractor={(item) => item.key}
                />
            )}

            {showFeedBack && !isValid && (
                <Text style={styles.invalidFeedBack}>
                    {messageFeedBack}
                </Text>
            )}
        </View>
    );
};

const Item = ({ title, onPress }) => (
    <TouchableOpacity onPress={onPress}>
        <Text style={styles.itemList}>{title}</Text>
    </TouchableOpacity>
);

export default FieldSetSelect;
