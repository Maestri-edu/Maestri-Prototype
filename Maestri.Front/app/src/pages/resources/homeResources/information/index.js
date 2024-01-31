import { Text, TouchableOpacity, View } from "react-native"
import styles from "./styles";
import Icon from "react-native-vector-icons/MaterialIcons";
import { useState } from "react";

const Information = ({ name = "Luiz", saldo = "2354.82" }) => {
    const [showSaldo, setShowSaldo] = useState(false);
    const wellcomeMessage = new Date().getHours() < 12 ? "Bom dia" : new Date().getHours() > 18 ? "Boa noite" : "Boa tarde";

    return (
        <View style={styles.informationBox}>
            <View style={{ flexDirection: "row" }}>
                <View>
                    <Text style={styles.textInformation}> {wellcomeMessage} </Text>
                    <Text style={styles.TitleInformation}> {name} </Text>
                </View>
                <View style={{ marginStart: "auto" }}>
                    <Text style={styles.userIcon}> {name[0]} </Text>
                </View>
            </View>
            <View style={styles.boxSaldo}>
                <Text style={styles.textSaldo}> Saldo </Text>
                <Text style={styles.saldo}> R$ {showSaldo ? saldo : '****.**'} </Text>
                <TouchableOpacity style={styles.iconButton} onPress={() => {
                    setShowSaldo(!showSaldo)
                }}>
                    <Icon name={showSaldo ? 'visibility-off' : 'visibility'} size={24} style={styles.icon} />
                </TouchableOpacity>
            </View>
            <View style={styles.BoxAfterSaldo}>
                <Text style={styles.textAfterSaldo}> Ver extrato </Text>
                <Icon name={"keyboard-arrow-right"} size={24} style={styles.icon} />
            </View>
        </View>
    )
}


export default Information