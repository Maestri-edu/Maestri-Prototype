import { StyleSheet } from "react-native";
import colors from "../../../design-System/global-styles";
import { Colors } from "react-native/Libraries/NewAppScreen";

const styles = StyleSheet.create({
    button:{
        width: "70%",
        height: 50,
        backgroundColor:colors.darkBlue,
        display:"flex",
        alignItems:"center",
        justifyContent:"center",
        borderRadius:20,
        opacity:0.8,
        marginVertical:20
    },

    buttonText:{
        color:colors.softWhite,
        fontSize:20,
        fontWeight:"bold",
    }
})

export default styles