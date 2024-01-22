import { Text, Pressable } from "react-native"
import Icon from "react-native-vector-icons/MaterialIcons";
import styles from "./styles"

const Action = ({ iconName,label,action = ()=>{} }) =>{
    return(
        <Pressable style={styles.iconBox} onPress={action} >
            <Icon name={iconName} size={24} style={styles.icon} />
            <Text style={styles.iconLabel}> {label} </Text>
        </Pressable>
    )
}

export default Action