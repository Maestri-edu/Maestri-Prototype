import { TouchableOpacity,Text } from "react-native"
import styles from "../styles"


const ButtonSignUp = () => { 
    return (
        <TouchableOpacity style={styles.button}>
            <Text style={styles.buttonText}> Sing Up </Text>
        </TouchableOpacity>
    )
}

export default ButtonSignUp