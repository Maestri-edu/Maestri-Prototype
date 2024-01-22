import { StyleSheet } from "react-native";
import colors from "../../../design-System/global-styles";

const styles = StyleSheet.create({
    label:{
        fontSize:20,
        fontWeight:"500",
        color:colors.softWhite,
        alignSelf:"flex-start",
        marginStart:30,
        marginTop:5
    },

    inputEditable:{
        borderWidth:0,
        borderBottomWidth:2,
        borderColor:colors.softWhite,
        width: "80%",
        height: 30,
        color:colors.mediumGray
    },
    inputNotEditable:{
        borderWidth:0,
        borderBottomWidth:2,
        borderColor:colors.softWhite,
        width: "80%",
        height: 30,
        color:colors.mediumGray,
        opacity:0.4
    },

    invalidFeedBack:{
        color:colors.accentRed,
        fontSize:12,
        alignSelf:"flex-start",
        marginStart:32
    },

    fieldSet:{
        width: "100%",
        display:"flex",
        justifyContent:"center",
        alignItems:"center",
    }
})

export default styles