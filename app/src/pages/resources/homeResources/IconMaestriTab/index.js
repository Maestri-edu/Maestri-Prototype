import { Image, View } from "react-native"
import styles from "./styles"
import TabImage from "../../../../../../assets/logoMaestri.png"

const IconMaestriTab = () => {
    return(
        <View style={styles.iconMaestri}>
            <Image style={{width:42,height:50}} source={TabImage}/>
        </View>
    ) 
}

export default IconMaestriTab