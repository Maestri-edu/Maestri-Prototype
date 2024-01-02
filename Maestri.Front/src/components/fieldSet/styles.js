import { StyleSheet } from "react-native";
import colors from "../../design-System/global-styles";

const styles = StyleSheet.create({
    label:{
        fontSize:20,
        fontWeight:"500",
        color:colors.softWhite,
        alignSelf:"flex-start",
        marginStart:50
    },

    input:{
        borderWidth:0,
        borderBottomWidth:2,
        borderColor:colors.softWhite,
        width: "80%",
        height: 50,
        color:colors.mediumGray
    },

    invalidFeedBack:{
        color:colors.accentRed,
        fontSize:12,
        alignSelf:"flex-start",
        marginStart:32
    },

    filedSet:{
        width: "100%",
        display:"flex",
        justifyContent:"center",
        alignItems:"center",
    }
})

export default styles