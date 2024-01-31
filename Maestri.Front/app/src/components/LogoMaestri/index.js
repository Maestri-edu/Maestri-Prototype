import { Image } from "react-native";
import logoMaestri from "../../../../assets/logoMaestri.png"
import styles from "./styles.js";

const LogoMaestri = () =>{
    return (
       <Image
       style={styles.logo}
       source={logoMaestri}
       />
    )
}

export default LogoMaestri;