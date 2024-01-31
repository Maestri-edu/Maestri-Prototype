import { View,Text } from "react-native"
import styles from "./styles"
import Action from "../../../../components/action"

const Actions = ()=>{
    return(
        <View style={styles.actionsBox}>
            <Action label={"Extrato"} iconName={"receipt"} />
            <Action label={"Cartão"} iconName={"payment"} />
            {/* <Action label={"cadastrar"} iconName={"add"} / */}
            <Action label={"transferir"} iconName={"send"} />
            <Action label={"pendências"} iconName={"book"} />
        </View>
    )
}

export default Actions